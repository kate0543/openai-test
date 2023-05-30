# Welcome to Cursor



# 1. Try generating with command K on a new line. Ask for a pytorch script of a feedforward neural network
# 2. Then, select the outputted code and hit chat. Ask if there's a bug. Ask how to improve.
# 3. Try selecting some code and hitting edit. Ask the bot to add residual layers.
# 4. To try out cursor on your own projects, go to the file menu (top left) and open a fol# Import necessary libraries
from flask import Flask, render_template, request, redirect, url_for

# Initialize the Flask app
app = Flask(__name__)

# Tic-tac-toe board
board = [["" for _ in range(3)] for _ in range(3)]

@app.route("/", methods=["GET", "POST"])
def index():
    global board
    if request.method == "POST":
        row = int(request.form["row"])
        col = int(request.form["col"])
        player = request.form["player"]

        # Update the board
        board[row][col] = player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            return render_template("winner.html", winner=winner)
        else:
            return redirect(url_for("index"))

    return render_template("index.html", board=board)

def check_winner(board):
    # Check rows, columns, and diagonals for a winner
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "":
            return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "":
        return board[0][2]

    return None

if __name__ == "__main__":
    app.run(debug=True)