#!bin/python
from random import randint
from flask import Flask

app = Flask(__name__)

@app.route('/<choice>', methods=['GET'])
def player(choice):
    choice = choice.lower()
    if choice == 'rock':
        return computer(1)
    elif choice == 'paper':
        return computer(2)
    elif choice == 'scissors':
        return computer(3)
    else:
        return 'Choose Rock, Paper, or Scissors'

def computer(opponent):
    roll = randint(1, 3)
    diff = opponent - roll

    if opponent == roll:
        return 'TIE! Play again?'
    elif diff == 1 or diff == -2:
        return 'You win! Play again?'
    else:
        return 'Sorry, you lose. Try again?'

if __name__ == '__main__':
    app.run(debug=True)
