
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
        for i in range(0):
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
              width = int(input("please enter the width of your rectangle").strip()) 
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
# calls on the program
picker = shape("Please pick either square triangle rectangle circle or parrallelagram: ").lower().strip()
print(picker)
perimeter = perimeter_calculator(picker)
print("{:.2f}".format(perimeter))
  
