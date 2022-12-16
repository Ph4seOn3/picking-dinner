import sys
import random

while True:
    question = input("Are you hungry?: ")
    
    answers = random.randint(1, 8)

    if question == "yes":
        if answers == 1:
            print("You should eat at Panera Bread.")
        elif answers == 2:
            print("You should eat at Rangoli.")
        elif answers == 3:
            print("You should eat at Sagebrush.")
        elif answers == 4:
            print("You should eat at G's Pizza.")
        elif answers == 5:
            print("You should eat at Olive Garden.")
        elif answers == 6:
            print("You should eat at a SteakHouse.")
        elif answers == 7:
            print("You should eat at Sushi Thai.")
        elif answers == 8:
            print("You should eat at PitaWay.")
        elif answers == 9:
            print("You should eat at Home, Cook next roll.")
        elif answers == 10:
            print("You should eat at Red Knapps.")
        elif answers == 11:
            print("You should eat at Chillis.")
        elif answers == 12:
            print("You should eat at Five Guys.")
        elif answers == 13:
            print("You should eat at Jimmy Johns.")
        elif answers == 14:
            print("You should trust me, roll again.")
        elif answers == 15:
            print("You should eat Salad & Veggies.")
            

    elif question == "no":
        sys.exit()
    else:
        print("Please answer yes or no.")
        continue

