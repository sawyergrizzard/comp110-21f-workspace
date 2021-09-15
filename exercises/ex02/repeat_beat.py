"""Repeating a beat in a loop."""

__author__ = "730245854"


beat: str = input("What beat do you want to repeat? ")
repeat: int = int(input("How many times do you want to repeat it? "))
beat2: str = beat + str(" ") 
repeat2: int = repeat - 1 
if repeat > 0: 
    print((beat2 * repeat2) + beat) 
else:
    print("No beat...")