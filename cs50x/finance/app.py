import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    # Show portfolio of stocks
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
    SUM = 0
    portfolio = db.execute("SELECT symbol, number FROM stocks WHERE person_id = ? ORDER BY symbol", session["user_id"])
    for row in portfolio:
        StockQuote = lookup(row["symbol"])
        row["name"] = StockQuote["name"]
        row["total"] = StockQuote["price"] * float(row["number"])
        SUM += row["total"]
        row["total"] = usd(StockQuote["price"] * float(row["number"]))
        row["price"] = usd(StockQuote["price"])
    SUM += cash
    return render_template("index.html", portfolio=portfolio, cash=usd(cash), SUM=usd(SUM))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    # Buy shares of stock
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if (not request.form.get("shares").isdigit()) or int(request.form.get("shares")) <= 0:
            return apology("Number of shares must be a possitive int", 400)
        StockQuote = lookup(request.form.get("symbol"))
        if StockQuote == None:
            return apology("invalid symbol", 400)
            #flash("No such stock. Try again!")
            # return render_template("buy.html")
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]
        if StockQuote["price"] * float(request.form.get("shares")) > cash:
            flash("Not enough cash!")
            return render_template("buy.html")
        cash -= float(request.form.get("shares")) * StockQuote["price"]
        db.execute("UPDATE users SET cash= ? WHERE id = ?", cash, session["user_id"])
        if len(db.execute("SELECT person_id FROM stocks WHERE person_id = ? AND symbol = ? ", session["user_id"], request.form.get("symbol").upper())) == 0:
            db.execute("INSERT INTO stocks (person_id, symbol, number) VALUES(?, ?, ?)",
                       session["user_id"], request.form.get("symbol").upper(), request.form.get("shares"))
        else:
            db.execute("UPDATE stocks SET number=number + ? WHERE person_id = ? AND symbol = ?",
                       request.form.get("shares"), session["user_id"], request.form.get("symbol").upper())

        db.execute("INSERT INTO history (person_id, symbol, number, change, date) VALUES(?, ?, ?, ?, ?)", session["user_id"], request.form.get(
            "symbol").upper(), request.form.get("shares"), usd(float(request.form.get("shares")) * StockQuote["price"]), datetime.now())
        flash("Bought!")
        return index()
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    history = db.execute("SELECT symbol, number, change, date FROM history WHERE person_id = ? ORDER BY date", session["user_id"])
    return render_template("history.html", history=history)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("logged in")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    #flash("logged out")
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    # Get stock quote.
    if request.method == "POST":
        if request.form.get("symbol") == "":
            return apology("Blank ticker entered!", 400)
        StockQuote = lookup(request.form.get("symbol"))
        if StockQuote == None:
            #flash("No such stock. Try again!")
            # return render_template("quote.html")
            return apology("No such stock. Try again!", 400)
        flash("Found!")
        return render_template("quoted.html", name=StockQuote["name"], symbol=StockQuote["symbol"], price=usd(StockQuote["price"]))
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    render_template("register.html")
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # If username exists
        elif len(db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))) == 1:
            return apology("Username already exists", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide confirmation", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("password must be equal to confirmation", 400)

        # Query database for creating a new username
        session["user_id"] = db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password")))

        # Redirecting to home page after registration
        flash("Registered!")
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    # Sell shares of stock
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        if (not request.form.get("shares").isdigit()) or int(request.form.get("shares")) <= 0:
            return apology("Number of shares must be a possitive int", 400)
        portfolio = db.execute("SELECT symbol FROM stocks WHERE person_id = ? ORDER BY symbol", session["user_id"])
        symbols = []
        for row in portfolio:
            symbols.append(row["symbol"])
        if request.form.get("symbol") not in symbols:
            return apology("This symbol isn't in your portfolio", 400)
        StockQuote = lookup(request.form.get("symbol"))

        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]["cash"]

        SharesInPortfolio = db.execute("SELECT number FROM stocks WHERE person_id = ? AND symbol = ?",
                                       session["user_id"], request.form.get("symbol"))[0]["number"]

        if SharesInPortfolio == request.form.get("shares"):
            db.execute("DELETE FROM stocks WHERE person_id = ? AND symbol = ?", session["user_id"], request.form.get("symbol"))
        elif int(SharesInPortfolio) < int(request.form.get("shares")):
            return apology("Don't have enought shares of that type", 400)
        else:
            db.execute("UPDATE stocks SET number=number - ? WHERE person_id = ? AND symbol = ?",
                       request.form.get("shares"), session["user_id"], request.form.get("symbol").upper())

        cash += float(request.form.get("shares")) * StockQuote["price"]
        db.execute("UPDATE users SET cash= ? WHERE id = ?", cash, session["user_id"])

        db.execute("INSERT INTO history (person_id, symbol, number, change, date) VALUES(?, ?, ?, ?, ?)", session["user_id"], request.form.get(
            "symbol").upper(), "-" + request.form.get("shares"), usd(float(request.form.get("shares")) * StockQuote["price"]), datetime.now())

        flash("Bought!")
        return index()
    else:
        portfolio = db.execute("SELECT symbol FROM stocks WHERE person_id = ? ORDER BY symbol", session["user_id"])
        symbols = []
        for row in portfolio:
            symbols.append(row["symbol"])
        return render_template("sell.html", symbols=symbols)


@app.route("/change", methods=["GET", "POST"])
@login_required
def change():
    # Allows user to change his password
    if request.method == "POST":
        if not request.form.get("oldpassword"):
            return apology("Must provide old password", 400)

        elif not request.form.get("newpassword"):
            return apology("Must provide new password", 400)

        elif not request.form.get("confirmation"):
            return apology("Must provide confirmation", 400)

        elif not (request.form.get("newpassword") == request.form.get("confirmation")):
            return apology("New password must be equal to confirmation", 400)

        elif not check_password_hash(db.execute("SELECT hash FROM users WHERE id = ?", session["user_id"])[0]["hash"], request.form.get("oldpassword")):
            return apology("Wrong old password", 403)

        # If old password is correct and all inputs are filled, we update password
        db.execute("UPDATE users SET hash= ? WHERE id= ? ", generate_password_hash(
            request.form.get("newpassword")), session["user_id"])

        # Redirecting to home page after changing password
        flash("Password has been changed!")
        return redirect("/")
    else:
        return render_template("change.html")

# export API_KEY=pk_f272cb1a247c41559414da46a4323b57