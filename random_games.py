import random

def roll_dice(sides=6,count=1):
    """
    Roll 'count' number of dice with 'sides' side.
    return a list of integers representing each roll die
    """

    if sides<2:
        raise ValueError("Dice must have atleast two sides")
    if count<1:
        raise ValueError("Must roll the dice atleast one time")
    return [random.randint(1,sides) for i in range(count)]
def flip_coin():
    """
    Flip a coin and return Heads or Tails
    """
    return random.choice(['Heads','Tails'])
if __name__ == "__main__":
    print("Rolling 3 dice with 6 sides:", roll_dice(sides=6, count=3))
    print("Flipping a coin:", flip_coin())