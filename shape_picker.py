def shape(question):
  error = "you have not selected one of the advible shapes"
  valid = False
  while not valid:
      shape = input(question).lower()

      if shape == "square":
        shape = "square"
        return shape
      elif shape == "triangle":
        shape = "triangle"
        return shape
      elif shape == "rectangle":
        shape = "rectangle"
        return shape
      else:
            print(error)
picker = shape("please pick either square triangle or rectangle:")
print(picker)