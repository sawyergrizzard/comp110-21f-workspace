"""Choose your own adventure."""

__author__ = "730245854"

player: str
points: int


def greet() -> None:
    """Welcomes player."""
    global player
    player = input("What is your name? ")
    print(f"Welcome to the Treasure Hunt {player}! If you gain 3 points, you win! Find the treasure...")


def room1() -> None: 
    """Search Room 1."""
    global player
    global points
    points = 1
    print(f"You have {points} point!")
    room1: str = input(f"Ok {player}, the booty is getting closer. Enter a, b, or c: Would you like to (a) Look under the bed, (b) Look in the dresser drawer, or (c) Exit game? ")
    answered = False

    while not answered:

        if room1 == str("a"):
            bed()
            answered = True
        if room1 == str("b"):
            dresser()
            answered = True 
        if room1 == str("c"):
            print(f"Oh well, thanks for playing! You gained {points} points")
            answered = True


def room2() -> None:
    """Search Room 2.""" 
    global player
    global points
    points = 1
    print(f"You have {points} points!")
    room2: str = input(f"Ok {player}, the booty could be here somewhere. Enter a, b, or c: Would you like to (a) Look behind the couch, (b) Look on the bookshelf, or (c) Exit game? ")
    answered = False

    while not answered:

        points = 2
        if room2 == str("a"):
            print(f"You have {points} points!")
            print("Sorry, you did not find the treasure. Better luck next time!")
            answered = True 
        if room2 == str("b"):
            print(f"You have {points} points!")
            print("Sorry, you did not find the treasure. Better luck next time!")
            answered = True
        if room2 == str("c"):
            print(f"Oh well, thanks for playing! You gained {points} points")
            answered = True


def bed() -> None: 
    """Search under bed."""
    global player 
    global points
    points = 2
    print(f"You have {points} points!")
    bed: str = input(f"{player}, you found items under the bed! Enter a, b, or c: Would you like to (a) Look in the shoebox, (b) Look in the mysterious chest, or (c) Exit game? ")
    answered = False

    while not answered:

        if bed == str("a"):
            y: int = 3
            z: int = treasure(y)
            print(f"You have {z} points!")
            print(f"Ahoy matey, you found the treasure! Use it wisely {player}!")
            answered = True
        if bed == str("b"):
            print(f"You have {points} points!")
            print("Sorry, you did not find the treasure. Better luck next time!")
            answered = True
        if bed == str("c"):
            print(f"Oh well, thanks for playing! You gained {points} points")
            answered = True


def dresser() -> None:
    """Search in dresser drawer."""
    global player
    global points
    points = 2
    print(f"You have {points} points!")
    print("Sorry, you did not find the treasure. Better luck next time!")


def treasure(a: int) -> int:
    """Treasure found.""" 
    return a 


def main() -> None:
    """Starts function."""
    global player
    global points
    points: int = 0 
    
    greet()

    answered = False
    while not answered:
        q1: str = input("Enter a, b, or c: Would you like to (a) Search Room 1, (b) Search Room 2, or (c) Exit game? ")
        if q1 == str("a"):
            room1()
            answered = True
        if q1 == str("b"): 
            room2()
            answered = True
        if q1 == str("c"):
            print(f"Oh well, thanks for playing! You gained {points} points")
            answered = True


if __name__ == "__main__":
    main()     