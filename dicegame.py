import random

def roll_dice():
    return random.randint(1,6)

def dice_roll_game():
    player_score=roll_dice()
    computer_score=roll_dice()

    +
    if player_score>computer_score:
        return "You Win!"
    elif player_score<computer_score:
        return "Computer Wins!"
    else:
        return "It's a tie!"