import random

def yes_no(question):
    valid = False
    while not valid:
        responce = input(question).lower()

        if responce == "yes" or responce == "y":
            responce = "yes"
            return responce
        elif responce == "no" or responce == "n":
            responce = "no"
            return responce

        else:
            print("please answer yes / no")
def instructions():
  print("***** How To Play *****\n")
show_instructions = yes_no ("would you like to view the instructions:")

if show_instructions == "yes":
  instructions()