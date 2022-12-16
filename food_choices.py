import sys
import random

while True:
    question = input("Are you hungry?: ")
    
    answers = random.randint(1, 8)

    if question == "yes":
        if answers == 1:
            print("You should eat a Sandwich.")
        elif answers == 2:
            print("You should eat Indian.")
        elif answers == 3:
            print("You should eat a Taco.")
        elif answers == 4:
            print("You should eat Italian.")
        elif answers == 5:
            print("You should eat a Pizza.")
        elif answers == 6:
            print("You should eat Chicken Wings.")
        elif answers == 7:
            print("You should eat Ramen Noodles.")
        elif answers == 8:
            print("You should eat at PitaWay.")

    elif question == "no":
        sys.exit()
    else:
        print("Please answer yes or no.")
        continue

