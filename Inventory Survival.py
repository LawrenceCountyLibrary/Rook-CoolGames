import time
import sys

def type_out(text, delay=0.025):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
    print(char, end="", flush=True)
    time.sleep(delay)
    print()

type_out("You have woke up in the forest.\nYou're lost, find your way out.\nTo help you, you can purchase items.\nYou get 5 points.\n")

#points for items

points = 5


type_out("Shop:\n Flashlight $2 - You can light up your way! Really useful at night time. ")
type_out(" Pizza $1 - Heals you! Really useful at low health. ")
type_out(" Sword $2 - Attacks enemies! Really useful when you're being attacked. ")
type_out(" Gold $1 - Gives you another currency to worry about! Really useful if you're at a shop. ")