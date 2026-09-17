#!/usr/bin/python
from __future__ import division
from random import choice

"""
This script simulates the outcome of rolling Grime's dice and other
cycles of non-transitive dice

In this first version of the script, we calculate the
probability that the green Grime's die beats the Yellow one
either analytically or using Monte Carlo methods.

REVISION 2 notes

By abstracting our code into functions, it is much
easier to keep it compact, and to repeat our code
from one dice pairs for other dice pairs.

Don't Repeat Yourself
=====================

This principle is often called DRY for 'Don't Repeat Yourself'
If you find yourself writing similar code over and over
or copying and pasting code blocks, it is very likely
that you can save a lot of trouble by using a function
or for loop to avoid having to repeat yourself.

"""

def roll_die(sides=[1,2,3,4,5,6]):
    """Roll an equally-weighted die and return the result

    sides -- a list of sides of the die, typically
      integers
    """
    return choice(sides)


def play_highest_wins(die1_sides,die2_sides,n_trials):
    """Return the fraction of times die 1 wins in a highest-number wins game
    die1_sides -- a list of ints representing the sides of die 1
    die2_sides -- a list of ints representing the sides of die 2
    n_trials -- number of times to play the game
    """
    die1_wins = 0.0
    for i in range(n_trials):
        die1_roll = roll_die(die1_sides)
        die2_roll = roll_die(die2_sides)
        if die1_roll > die2_roll:
            die1_wins += 1.0

    return die1_wins/n_trials

def compare_dice(die1_sides,die2_sides):
    """Calculate the chances that die1 beats die2

    die1_sides -- a list of ints representing the first die's sides
    die2_sides -- a list of ints representing the second die's sides
    This function calculates the chances that die1 beats die2 analytically
    by enumerating possible outcomes
    """
    wins = 0.0
    total = 0.0
    for d1_side in die1:
        for d2_side in die2:
            if d1_side > d2_side:
                wins += 1.0
            total += 1
    return wins/total

#Create variable for each of our dice, representing each as a
#list of integers (one for each side)

green_die = [2,2,4,4,9,9]
yellow_die = [1,1,6,6,8,8]
pink_die = [3,3,5,5,7,7]

#Set the number of trials once
#(it will be the same for each trial)
n_trials = 100000

#Compare each die pair using a for loop
result_lines = []
for die1 in [green_die,yellow_die,pink_die]:
    for die2 in [green_die,yellow_die,pink_die]:
        #Skip dice that are the same
        if die1 == die2:
            continue

        #Calculate the Monte Carlo result for this pair of dice
        monte_carlo_result = play_highest_wins(die1,die2,n_trials)

        #Calculate the analytical result for this dice pair
        analytical_result = compare_dice(die1,die2)

        #Find the difference to get a sense of how wrong our Monte Carlo result
        #was
        monte_carlo_error = monte_carlo_result - analytical_result

        result_line= "\t".join(map(str,[die1,die2,monte_carlo_result,\
          analytical_result,monte_carlo_error]))

        result_lines.append(result_line)

print("Results:\n")
print("Die1\tDie2\tMonte Carlo Result\tAnalytical Result\tMonte Carlo error")
for result_line in result_lines:
    print(result_line)
