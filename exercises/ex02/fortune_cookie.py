"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730245854"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


message: int = int(randint(1, 4))
print("Your fortune cookie says...")

if message == 1:
    print("Follow your dreams and you will find great prosperity.")
else: 
    if message == 2: 
        print("You will find a great companion when you least expect it.")
    if message == 3:
        print("HELP, I AM BEING HELD HOSTAGE IN A FORTUNE COOKIE FACTORY!")
        
    if message == 4:
        print("UNC Chapel Hill will win the 2022 NCAA basketball title.")

print("Now, go spread positive vibes!")
