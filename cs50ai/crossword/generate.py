import sys

from sqlalchemy import false

from crossword import *


class CrosswordCreator():

    def __init__(self, crossword):
        """
        Create new CSP crossword generate.
        """
        self.crossword = crossword
        self.domains = {
            var: self.crossword.words.copy()
            for var in self.crossword.variables
        }

    def letter_grid(self, assignment):
        """
        Return 2D array representing a given assignment.
        """
        letters = [
            [None for _ in range(self.crossword.width)]
            for _ in range(self.crossword.height)
        ]
        for variable, word in assignment.items():
            direction = variable.direction
            for k in range(len(word)):
                i = variable.i + (k if direction == Variable.DOWN else 0)
                j = variable.j + (k if direction == Variable.ACROSS else 0)
                letters[i][j] = word[k]
        return letters

    def print(self, assignment):
        """
        Print crossword assignment to the terminal.
        """
        letters = self.letter_grid(assignment)
        for i in range(self.crossword.height):
            for j in range(self.crossword.width):
                if self.crossword.structure[i][j]:
                    print(letters[i][j] or " ", end="")
                else:
                    print("█", end="")
            print()

    def save(self, assignment, filename):
        """
        Save crossword assignment to an image file.
        """
        from PIL import Image, ImageDraw, ImageFont
        cell_size = 100
        cell_border = 2
        interior_size = cell_size - 2 * cell_border
        letters = self.letter_grid(assignment)

        # Create a blank canvas
        img = Image.new(
            "RGBA",
            (self.crossword.width * cell_size,
             self.crossword.height * cell_size),
            "black"
        )
        font = ImageFont.truetype("assets/fonts/OpenSans-Regular.ttf", 80)
        draw = ImageDraw.Draw(img)

        for i in range(self.crossword.height):
            for j in range(self.crossword.width):

                rect = [
                    (j * cell_size + cell_border,
                     i * cell_size + cell_border),
                    ((j + 1) * cell_size - cell_border,
                     (i + 1) * cell_size - cell_border)
                ]
                if self.crossword.structure[i][j]:
                    draw.rectangle(rect, fill="white")
                    if letters[i][j]:
                        w, h = draw.textsize(letters[i][j], font=font)
                        draw.text(
                            (rect[0][0] + ((interior_size - w) / 2),
                             rect[0][1] + ((interior_size - h) / 2) - 10),
                            letters[i][j], fill="black", font=font
                        )

        img.save(filename)

    def solve(self):
        """
        Enforce node and arc consistency, and then solve the CSP.
        """
        self.enforce_node_consistency()
        self.ac3()
        return self.backtrack(dict())

    def enforce_node_consistency(self):
        """
        Update `self.domains` such that each variable is node-consistent.
        (Remove any values that are inconsistent with a variable's unary
         constraints; in this case, the length of the word.)
        """
        for variable in self.domains:
            CurrentDomain = self.domains[variable].copy()
            for word in self.domains[variable]:
                if variable.length != len(word):
                    CurrentDomain.remove(word)
            self.domains[variable] = CurrentDomain

    def revise(self, x, y):
        """
        Make variable `x` arc consistent with variable `y`.
        To do so, remove values from `self.domains[x]` for which there is no
        possible corresponding value for `y` in `self.domains[y]`.

        Return True if a revision was made to the domain of `x`; return
        False if no revision was made.
        """
        # Algorithm corresponds to that described in the lecture.
        if self.crossword.overlaps[x, y] == None:
            return False
        revised = False
        CurrentDomain = self.domains[x].copy()

        for wordX in self.domains[x]:
            found = False
            for wordY in self.domains[y]:
                if wordX[self.crossword.overlaps[x, y][0]] == wordY[self.crossword.overlaps[x, y][1]] and wordX != wordY:
                    found = True
            if not found:
                CurrentDomain.remove(wordX)
        if len(CurrentDomain) < len(self.domains[x]):
            revised = True
        self.domains[x] = CurrentDomain
        return revised

    def ac3(self, arcs=None):
        """
        Update `self.domains` such that each variable is arc consistent.
        If `arcs` is None, begin with initial list of all arcs in the problem.
        Otherwise, use `arcs` as the initial list of arcs to make consistent.

        Return True if arc consistency is enforced and no domains are empty;
        return False if one or more domains end up empty.
        """

        # We construct initial list of all arcs in the problem.
        if arcs == None:
            arcs = []
            for X in self.domains:
                for Y in self.crossword.neighbors(X):
                    arcs.append((X, Y))

        # Algorithm corresponds to that described in the lecture.
        while len(arcs) != 0:
            X = arcs[0][0]
            Y = arcs[0][1]
            arcs.remove((X, Y))
            if self.revise(X, Y):
                if len(self.domains[X]) == 0:
                    return False
                M = self.crossword.neighbors(X)
                M.discard(Y)
                for Z in M:
                    arcs.append((Z, X))
        return True

    def assignment_complete(self, assignment):
        """
        Return True if `assignment` is complete (i.e., assigns a value to each
        crossword variable); return False otherwise.
        """

        """
        print(f"-+{len(self.domains)}+-")
        print(f"~{self.domains}~")
        for variable in self.domains:
            print(f"{variable} || {self.domains[variable]}\n")
            assignment[variable] = self.domains[variable].pop()
            self.domains[variable].add(assignment[variable])
        return True
        """
        for variable in self.domains:
            if variable not in assignment:
                return False
        return True
        
    def consistent(self, assignment):
        """
        Return True if `assignment` is consistent (i.e., words fit in crossword
        puzzle without conflicting characters); return False otherwise.
        """
        A = set(assignment)
        for X in assignment:
            for Y in self.crossword.neighbors(X) & A:
                if assignment[X][self.crossword.overlaps[X, Y][0]] != assignment[Y][self.crossword.overlaps[X, Y][1]] or assignment[X] == assignment[Y]:
                    return False
        return True

    def order_domain_values(self, var, assignment):
        """
        Return a list of values in the domain of `var`, in order by
        the number of values they rule out for neighboring variables.
        The first value in the list, for example, should be the one
        that rules out the fewest values among the neighbors of `var`.
        """
        # We will make ordered tuples list, where in one tuple will be value (word) and number.
        ordered_tuples_list = []
        A = set(assignment)
        for value in self.domains[var]:
            # Number is for "the number of values they rule out".
            number = 0
            for Y in self.crossword.neighbors(var) & A:
                if value[self.crossword.overlaps[var, Y][0]] != assignment[Y][self.crossword.overlaps[var, Y][1]] or value == assignment[Y]:
                    number += 1
            ordered_tuples_list.append((value, number))

        ordered_tuples_list.sort(key=lambda tuple: tuple[1])
        # Now we convert ordered tuples list to just ordered list of values in the domain of 'var'.
        ordered_list = []
        for tuple in ordered_tuples_list:
            ordered_list.append(tuple[0])

        return ordered_list

    def select_unassigned_variable(self, assignment):
        """
        Return an unassigned variable not already part of `assignment`.
        Choose the variable with the minimum number of remaining values
        in its domain. If there is a tie, choose the variable with the highest
        degree. If there is a tie, any of the tied variables are acceptable
        return values.
        """
        unassigned_list = []
        for variable in self.domains:
            if variable not in assignment:
                unassigned_list.append((variable, len(self.domains[variable])))
        # We sort by the minimum remaining value:
        unassigned_list.sort(key=lambda tuple: tuple[1])
        
        min_value = unassigned_list[0][1]
        if len(unassigned_list) > 1:
            # If there is a tie between variables sorted by minimum remaining value:
            if unassigned_list[0][1] == unassigned_list[1][1]:
                for tuple in unassigned_list:
                    if tuple[1] != min_value:
                        unassigned_list.remove(tuple)
                    else:
                        tuple = (tuple[0], len(self.crossword.neighbors(unassigned_list[0][0])))
        elif len(unassigned_list) == 1:
            return unassigned_list[0][0]
        # We assume that at list one uassigned variable will be in the puzzle
        # and don not consider situation, when length of unassigned_list is 0.

        # Now sort by the lagest degree
        unassigned_list.sort(key=lambda tuple: tuple[1], reverse=True)

        # We just return the first variable in the list and do not check
        # if there is a tie, i.e we choose arbitrary (but not randomly in this case)
        return unassigned_list[0][0]

    def backtrack(self, assignment):
        """
        Using Backtracking Search, take as input a partial assignment for the
        crossword and return a complete assignment if possible to do so.

        `assignment` is a mapping from variables (keys) to words (values).

        If no assignment is possible, return None.
        """
        # Algorithm corresponds to that described in the lecture.
        if self.assignment_complete(assignment):
            return assignment
        variable = self.select_unassigned_variable(assignment)
        ordered_domain = self.order_domain_values(variable, assignment)
        for value in ordered_domain:
            assignment_copy = assignment.copy()
            assignment_copy[variable] = value
            if self.consistent(assignment_copy):
                assignment[variable] = value
                result = self.backtrack(assignment)
                if result != None:
                    return result
        return None


def main():

    # Check usage
    if len(sys.argv) not in [3, 4]:
        sys.exit("Usage: python generate.py structure words [output]")

    # Parse command-line arguments
    structure = sys.argv[1]
    words = sys.argv[2]
    output = sys.argv[3] if len(sys.argv) == 4 else None

    # Generate crossword
    crossword = Crossword(structure, words)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()

    # Print result
    if assignment is None:
        print("No solution.")
        print(creator.domains)
    else:
        creator.print(assignment)
        if output:
            creator.save(assignment, output)


if __name__ == "__main__":
    main()
