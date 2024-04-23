// Submits email from the user.
function SubmitEmail()
    {
        let email = document.getElementById("Input1").value.toLowerCase();
        document.getElementById("thanks").innerHTML = "Thank you, " + email + "!<br/>I will gladly answer you!";
        document.getElementById("Input1").style.backgroundColor = "green";
    };
// Submits feedback from the user.
function SubmitFeedback()
    {
        let email = document.getElementById("Input1").value.toLowerCase();
        document.getElementById("thanks").innerHTML = "Thank you for your feedback!<br/>I will read it carefully!";
        document.getElementById("Input2").style.backgroundColor = "green";
    };