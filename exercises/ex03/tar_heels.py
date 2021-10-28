"""An exercise in remainders and boolean logic."""

__author__ = "730245854"


num_choice: int = int(input("Enter an int: "))
tar: int = int(num_choice % 2)
heels: int = int(num_choice % 7) 


if heels != tar == int(0):
    print("TAR") 

if tar != heels == int(0):
    print("HEELS")

if tar == heels == int(0):
    print("TAR HEELS")

if tar != int(0) and heels != int(0):  
    print("CAROLINA")
