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
  print("***** This is how to use the program *****\n")
  print("first please enter what what you will use")
  print("arfter you have selected the shape please import the numbers we ask for")
show_instructions = yes_no ("would you like to view the instructions:")

if show_instructions == "yes":
  instructions()