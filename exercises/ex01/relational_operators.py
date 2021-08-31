"""Relational operators program."""
author: str("730245854")

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))
exponent: int = left < right
division: int = left >= right 
integer_division: int = left == right
remainder_modulo: int = left != right
print(str(left) + " < " + str(right) + " is " + str(exponent))
print(str(left) + " >= " + str(right) + " is " + str(division))
print(str(left) + " == " + str(right) + " is " + str(integer_division)) 
print(str(left) + " != " + str(right) + " is " + str(remainder_modulo))