
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

# area calculator
def area_calculator(shape):
  error2 = "please enter a iniger between 1 and 100"
  area = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        one_side = int(input("Please input one of the sides mesurement from you square between 1 and 100 : ".strip()))
        if one_side <1:
          print(error2)
        elif one_side > 100:
          print(error2)
        else:
          area = one_side ** 2
          return area
      elif shape == "circle":
        radius = int(input("Please enter the value of your radius of your circle: ").strip())
        if radius <1:
          print(error2)
        elif radius > 100:
          print(error2)
        else:
          area = area + (pi * radius ** 2)
          return area
      elif shape == "rectangle":
        valid2 = False
        while not valid2:
          valid3 = False
          while not valid3:
            width = int(input("Please enter the value of the width of the rectangle: ").strip())
            if width <1:
              print(error2)
              valid3 = False
            elif width > 100:
              print(error2)
            else:
              valid3 = True
          length = int(input("Please enter the value of legth of the rectangle: ").strip())
          if length <1:
            print(error2)
          elif length > 100:
            print(error2)
            valid3 = False
          else:
            area = area + (length * width)
            return area
            continue
      elif shape == "triangle":
        valid2 = False
        while not valid2:
          valid3 = False
          while not valid3:
            Tbase = int(input("Please enter the base of your trinagle: ").strip())
            if Tbase <1:
              print(error2)
              valid2 = False
            elif Tbase > 100:
              print(error2)
            else:
              valid3 = True
          Theight = int(input("Please enter your height of the tringle: ").strip())
          if Theight <1:
              print(error2)
          elif Theight > 100:
            print(error2)
            valid2 = False
          else:
            area = area + (0.5 * Tbase * Theight)
            return area
      elif shape == "parrallelagram":
        valid2 = False
        while not valid2:
          valid3 = False
          while not valid3:
            Pbase = int(input("Please enter the base of the parrallelagram: ").strip())
            if Pbase <1:
              print(error2)
              valid2 = False
            elif Pbase > 100:
              print(error2)
            else: 
              valid3 = True
          Pheight = int(input("Please enter the height of your parrallelagram :").strip())
          if Pheight <1:
            print(error2)
          elif Pheight > 100:
            print(error2)
            valid2 = False
          else:
            area = area + ( Pbase * Pheight)
            return area
    except ValueError:
        print(error2)  
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram: ").lower().strip()
print(picker)
area = area_calculator(picker)
print("{:.2f}".format(area))
  
