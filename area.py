# ask you what shaper you would like to calculate the area or permiter of 
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

# ask you if you want to calculate the area or perimeter of "X" shape
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

# used when asking a yes or no question
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
      return responce
    else:
        print(error)

# prints instructions if user wants to view them
def instructions():
  print("***** This is how to use the program *****\n")
  print("first please enter what what you will use")
  print("arfter you have selected the shape please import the numbers we ask for")

# asks user to select what unit there shape is mesured in
def unit(question):
  error = "you have not selected the advalible units:"
  valid = False
  while not valid:
    unit = input(question).lower().strip()
    if unit == "meters" or unit == "m":
      unit = "meters"
      return unit
    elif unit == "centimeter" or unit == "cm":
      unit = "centimeter"
      return unit
    elif unit == "millimeters" or unit == "mm":
      unit = "millimeters"
      return unit
    else:
      print(error)

# area calculator
def area_calculator(shape):
  error = "please enter a integer"
  area = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        one_side = num_check("Please input one of the sides mesurement from you square: ".strip())
        area = one_side ** 2
        return area
      elif shape == "circle":
        radius = num_check("Please enter the value of your radius of your circle: ".strip())
        area = area + (pi * radius ** 2)
        return area
      elif shape == "rectangle":
        length = num_check("Please enter the value of legth of the rectangle: ".strip())
        width = num_check("Please enter the value of the width of the rectangle: ".strip())
        area = area + (length * width)
        return area
      elif shape == "triangle":
        Tbase = num_check("Please enter the base of your trinagle: ".strip())
        Theight = num_check("Please enter your height of the tringle: ".strip())
        area = area + (0.5 * Tbase * Theight)
        return area
      elif shape == "parrallelagram":
        Pbase = num_check("Please enter the base of the parrallelagram: ".strip())
        Pheight = num_check("Please enter the height of your parrallelagram :".strip())
        area = area + ( Pbase * Pheight)
        return area
    except ValueError:
        print(error) 

# perimeter calculator
def perimeter_calculator(shape):
  error = "please enter a integer"
  perimeter = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        list1 = []
        for i in range(1):
          sside = num_check("Please input one of the sides mesurement from you square: ")
          list1.append(sside)
        perimeter = 4 * list1[0]
        return perimeter
      elif shape == "circle":
        list2 = []
        for i in range(1):
          radius = num_check("Please enter the value of your radius of your circle: ")
          list2.append(radius)
        perimeter = 2 * pi * list2[0]
        return perimeter
      elif shape == "rectangle":
        list3 = []
        for i in range(4):
          rsides = num_check("Please each the value of each side from your rectangle: ")
          list3.append(rsides)
        perimeter = list3[0] + list3[1] + list3[2] + list3[3]
        return perimeter
      elif shape == "triangle":
        list4 = []
        for i in range(3):
          Tsides = num_check("Please enter the base of your trinagle: ")
          list4.append(Tsides)
        perimeter = list4[0] + list4[1] + list4[2]
        return perimeter
      elif shape == "parrallelagram":
        list5 = []
        for i in range(2):
          Psides = num_check("Please enter the base of the parrallelagram: ")
          list5.append(Psides)
        perimeter = (list5[0] * 2) + (list5[1] * 2)
        return perimeter
    except ValueError:
        print(error)  
# check if number is within 1 and 100
def num_check(question):
  error = "Please enter a number between 1 and 10"
  try:
    number=int(input(question))
    if number <1:
      print(error)
    elif number > 100:
      print(error)
    else:
      return number
  except ValueError: 
    print("Enter a number: ").strip().lower()
  
show_instructions = yes_no ("would you like to view the instructions:")
if show_instructions == "yes":
  instructions()
# checks what users mesurements is 
measurement = unit("what unit would you like to use millimeters, centimeter, meters:")
print(measurement)
# loop to pick shape and calculation
valid = False
while not valid:
  option = choice("what would you like to calculate area or permiter: ").lower().strip()
  print("you have chosen {} as your calculation we will now chose the shape: ".format(option))
  print()
  picker = shape("please pick either square triangle or rectangle: ".lower().strip())
  print(f"you have chosen {picker} as your shape that you want to calculate the {option} for:").lower().strip()
  print()
  ans = yes_no(f"are you sure you want {option} as you calculation and {picker} as you shape: ".strip().lower())
  if ans == "yes":
    valid = True
    continue
  elif ans == "no":
    valid = False
if choice == "area":
  area = area_calculator(picker)
  print("{:.2f}".format(area))
elif choice == "perimeter": 
  print("gfy")