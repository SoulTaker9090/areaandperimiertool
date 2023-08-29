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
  print("***** First please enter what unit you will use *****\n")
  print("***** Second please enter what calculation you will use *****\n")
  print("***** Third please enter what shape you will use use *****\n")
  print("***** Arfter you have selected the shape calculation and unit please imput the numbers we ask for *****\n")
  print("we might ask you for each side of a triangle please input each side value\n")

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

# perimeter calculator
def perimeter_calculator(shape):
  error = "please enter a integer between 1 and 100"
  perimeter = 0
  pi = 3.14
  valid = False
  while not valid:
    try:
      if shape == "square":
        list1 = []
        for i in range(1):
          one_side = int(input("Please input one of the sides mesurement from you square: ").strip())
          if one_side < 1:
            print(error)
          elif one_side > 100:
            print(error)
          else:
            list1.append(one_side)
            perimeter = 4 * list1[0]
            return perimeter
      elif shape == "circle":
        list2 = []
        for i in range(1):
          radius = int(input("Please enter the value of your radius of your circle: ").strip())
          if radius < 1:
            print(error)
          elif radius > 100:
            print(error)
          else:
            list2.append(radius)
            perimeter = 2 * pi * list2[0]
            return perimeter
      elif shape == "rectangle":
        list3 = []
        for i in range(0,1):
          valid = False
          while not valid:
            length = int(input("Please enter the value of length of the rectangle: ").strip())
            if length < 1:
              print(error)
              valid = False
            elif length > 100:
              print(error)
              valid = False
            else:
              list3.append(length)
              width = int(input("please enter the width of your rectangle: ").strip()) 
              if width < 1:
                print(error)
                valid = False
              elif width > 100:
                print(error)
                valid = False
              else:
                list3.append(width)
                valid = True
        perimeter = (list3[0] * 2) + (list3[1] * 2)
        return perimeter
        
      elif shape == "triangle":
        list4 = []
        for i in range(0,3):
          valid = False
          while not valid:
            sidea = int(input("Please enter the side a of your trinagle: ").strip())
            if sidea < 1:
              print(error)
              valid = False
            elif sidea > 100:
              print(error)
              valid = False
            else:
              list4.append(sidea)
              sideb = int(input("Please enter your side b of the tringle: ").strip())
              if sideb < 1:
                  print(error)
                  valid = False
              elif sideb > 100:
                print(error)
                valid = False
              else:
                list4.append(sideb)
                sidec = int(input("Please enter your side c of the tringle: ").strip())
                if sidec < 1:
                  print(error)
                  valid = False
                elif sidec > 100:
                  print(error)
                  valid = False
                else:
                  list4.append(sidec)
                  valid = True
          perimeter = (list4[0] + list4[1] + list4[2])
          return perimeter
      elif shape == "parrallelagram":
        list5 = []
        for i in range(0,1):
          valid = False
          while not valid:
            base = int(input("Please enter the value of base of the parrallelagram: ").strip())
            if base < 1:
              print(error)
              valid = False
            elif base > 100:
              print(error)
              valid = False
            else:
              list5.append(base)
              side = int(input("please enter the side of your parrallelagram: ").strip()) 
              if side < 1:
                print(error)
                valid = False
              elif side > 100:
                print(error)
                valid = False
              else:
                list5.append(side)
                valid = True
        perimeter = (list5[0] * 2) + (list5[1] * 2)
        return perimeter
    except ValueError:
        print(error)  

# displays instrution if user enters yes when asked do you want to view the instructions
show_instructions = yes_no ("would you like to view the instructions: ").strip()
if show_instructions == "yes":
  instructions()
# loop to pick shape and calculation
exit_code = ""
while exit_code != "xxx":
  # checks what users mesurements is 
  measurement = unit("what unit would you like to use millimeters, centimeter, meters: ")
  print(measurement)
  # picks wheater user will choose area or perimiter
  option = choice("what would you like to calculate area or permiter: ").lower().strip()
  print("you have chosen {} as your calculation we will now chose the shape: ".format(option))
  print()
  # user picks what shape they will use
  picker = shape("Please pick either square triangle rectangle circle or parrallelagram:" .lower().strip())
  print(f"you have chosen {picker} as your shape that you want to calculate the {option} for:")
  print()
  # ask them if what the have picked is what they want
  ans = yes_no(f"are you sure you want {option} as your calculation and {picker} as your shape: ".strip().lower())
  # if they input yes continues into program
  if ans == "yes":
    # if what the user choose was area it will print the calculation for area
    if option == "area" or option == "a":
      error = "please enter yes or no"
      area = area_calculator(picker)
      print("{:.2f} {}²".format(area, measurement))
      # if input is no ends program if input is yes loops program
      again = yes_no ("would you like to use another shape :")
      if again == "yes":
        exit_code = "yes"
      elif again == "no":
        exit_code = "xxx"
        print("Thank you and goodbye")
      else:
        print(error)
  if ans == "yes":
    # if what the user choose was perimeter it will print the calculation for perimeter 
    if option == "perimeter" or option == "p":
      perimeter = perimeter_calculator(picker)
      print("{:.2f} {}".format(perimeter, measurement))
      # if input is no ends program if input is yes loops program
      again = yes_no ("would you like to use another shape :")
      if again == "yes":
        exit_code = ""
      elif again == "no":
        exit_code = "xxx"
        print("Thank you and goodbye")
      else:
        print(error)