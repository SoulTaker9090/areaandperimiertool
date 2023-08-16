
def shape(question):
  error = "you have not selected one of the advible shapes"
  valid = False
  while not valid:
    shape = input(question).lower()
  
    if shape == "square" or shape == "s":
      shape = "square"
      return shape
    elif shape == "triangle" or shape == "t":
      shape = "triangle"
      return shape
    elif shape == "rectangle" or shape == "r":
      shape = "rectangle"
      return shape
    elif shape == "circle" or shape == "c":
      shape = "circle"
      return shape
    elif shape == "parrallelagram" or shape == "p":
      shape = "parrallelagram"
      return shape
    else:
          print(error)

def choice(question):
  error = ("please answer with area or perimeter:")
  valid = False
  while not valid:
    choice = input(question).lower()

    if choice == "area" or choice == "a":
        choice = "area"
        return choice
    elif choice == "perimeter" or choice == "p":
        choice = "perimeter"
        return choice

    else:
      print(error)

def yes_no(question):
  error = "please enter yes or no"
  valid = False
  while not valid:
    responce = input(question).lower().strip()

    if responce == "yes" or responce == "y":
      responce = "yes"
      return responce
    elif responce == "no" or responce == "n":
      responce = "no"
      print("please retry and dont get it wrong")
      return responce
    else:
        print(error)


valid = False
while not valid:
  option = choice("what would you like to calculate area or permiter:")
  print("you have chosen {} as your calculation we will now chose the shape:".format(option))
  print()
  picker = shape("please pick either square triangle or rectangle:")
  print("you have chosen {} as your shape that you want to calculate the {} for:".format(picker, option))
  print()
  ans = yes_no("are you sure you want {} as you calculation and {} as you shape:".format(option, picker))
  if ans == "yes":
    valid = True
  elif ans == "no":
    valid = False

