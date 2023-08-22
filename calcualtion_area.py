
# ask you what shaper you would like to calculate the area or permiter of 
def shape(question):
  error = "you have not selected one of the advible shapes"
  valid = False
  while not valid:
    
    shape = input(question).lower().strip()
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
# check if number is within 1 and 100
def num_check(question):
  error = "Please enter a number between 1 and 100"
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

# area calculator
def area_calculator(shape):
  error = "please enter a integer"
  area = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        one_side = num_check("Please input one of the sides mesurement from you square: ").strip()
        area = one_side ** 2
        return area
      elif shape == "circle":
        radius = num_check("Please enter the value of your radius of your circle: ").strip()
        area = area + (pi * radius ** 2)
        return area
      elif shape == "rectangle":
        length = num_check("Please enter the value of legth of the rectangle: ").strip()
        width = num_check("Please enter the value of the width of the rectangle: ").strip()
        area = area + (length * width)
        return area
      elif shape == "triangle":
        Tbase = num_check("Please enter the base of your trinagle: ").strip()
        Theight = num_check("Please enter your height of the tringle: ").strip()
        area = area + (0.5 * Tbase * Theight)
        return area
      elif shape == "parrallelagram":
        Pbase = num_check("Please enter the base of the parrallelagram: ").strip()
        Pheight = num_check("Please enter the height of your parrallelagram :").strip()
        area = area + ( Pbase * Pheight)
        return area
    except ValueError:
        print(error)  
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram: ").lower().strip()
print(picker)
area = area_calculator(picker)
print("{:.2f}".format(area))
  
