
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
          one_side = num_check("Please input one of the sides mesurement from you square: ")
          list1.append(one_side)
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
        for i in range(2):
          length = num_check("Please enter the value of legth of the rectangle: ")
          list3.append(length)
        perimeter = list3[0] + list3[0] + list3[1] + list3[1]
        return perimeter
      elif shape == "triangle":
        Tbase = num_check("Please enter the base of your trinagle: ").strip()
        Theight = num_check("Please enter your height of the tringle: ").strip()
        perimeter = perimeter + (0.5 * Tbase * Theight)
        return perimeter
      elif shape == "parrallelagram":
        Pbase = num_check("Please enter the base of the parrallelagram: ").strip()
        Pheight = num_check("Please enter the height of your parrallelagram :").strip()
        perimeter = perimeter + ( Pbase * Pheight)
        return perimeter
    except ValueError:
        print(error)  
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram: ").lower().strip()
print(picker)
perimeter = perimeter_calculator(picker)
print("{:.2f}".format(perimeter))
  
