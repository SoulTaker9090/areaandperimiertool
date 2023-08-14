import random

def yes_no(question):
    valid = False
    while not valid:
        responce = input(question).lower()

        if responce == "area" or responce == "a":
            responce = "area"
            return responce
        elif responce == "perimeter" or responce == "p":
            responce = "perimeter"
            return responce

        else:
            print("please answer with area or perimeter")
