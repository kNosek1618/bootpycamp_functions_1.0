
from random import random

def flip_coin():
    # Generate random number 0-1
    r = random()
    if r > 0.5:
        return "Heads"
    else:
        return "Tails"

def flip_coin():
    if random() > 0.5:
        return "HEADS"
    else:
        return "TAILS"

print(flip_coin()) # TAILS OR HEADS ACCORDING RANDOM NUMBER

# # # RESULT # # #
# only the last function is printed

def speak_pig():
    return 'oink'

print(speak_pig())



