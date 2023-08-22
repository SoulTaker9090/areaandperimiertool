
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
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram: ").lower().strip()
print(picker)
perimeter = perimeter_calculator(picker)
print("{:.2f}".format(perimeter))
  
