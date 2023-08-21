
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
# area calculator
def area_calculator(shape):
  error = "please enter a integer"
  error2 = "you value has to be between 1 and 200"
  area = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        one_side = int(input("Please input one of the sides mesurement from you square:"))
        area = area + (one_side ** 2)
        if one_side > 200:
          print (error2)
        elif one_side < 1:
          print(error2)
        else:
          return area
      elif shape == "circle":
        radius = int(input("Please enter the value of your radius of your circle:"))
        area = area + (pi * radius ** 2)
        if radius > 200:
          print (error2)
        elif radius < 1:
          print(error2)
        else:
          return area
      elif shape == "rectangle":
        length = int(input("Please enter the value of legth of the rectangle:"))
        width = int(input("Please enter the value of the width of the rectangle:"))
        area = area + (length * width)
        if length > 200:
          print (error2)
        elif width < 1:
          print(error2)
        else:
          return area
      elif shape == "triangle":
        Tbase = int(input("Please enter the base of your trinagle:"))
        Theight = int(input("Please enter your height of the tringle:"))
        area = area + (0.5 * Tbase * Theight)
        if Tbase > 200:
          print (error2)
        elif Theight < 1:
          print(error2)
        else:
          return area
      elif shape == "parrallelagram":
        Pbase = int(input("Please enter the base of the parrallelagram:"))
        Pheight = int(input("Please enter the height of your parrallelagram:"))
        area = area + ( Pbase * Pheight)
        if Pbase > 200:
          print (error2)
        elif Pheight < 1:
          print(error2)
        else:
          return area
    except ValueError:
        print(error)  
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram:")
print(picker)
area = area_calculator(picker)
print("{:.2f}".format(area))
  
