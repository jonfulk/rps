#!/usr/bin/env python
# -*- coding: utf-8 -*-
from random import randint
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/<int:user_choice>')
def chooser(user_choice):
    winner = None
    cpu_choice = randint(1, 3)
    winner = determine_winner(user_choice, cpu_choice)
    return render_template('results.html', winner=winner, user=user_choice, cpu=cpu_choice)

def determine_winner(player, cpu):
    """Determine winner by comparing player choice to computer random int.

    Rock = 1, Paper = 2, Scissors = 3
    Player wins when diff is 1 or -2
    """

    if player not in (1, 2, 3):
        return redirect(url_for('index'))
    else:
        diff = player - cpu
        if diff == 0:
            winner = None
        elif diff == 1 or diff == -2:
            winner = 'You are '
        else:
            winner = 'Root is '
        return winner

if __name__ == '__main__':
    app.run(debug=True)
