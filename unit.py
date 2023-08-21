# asks user to select what unit there shape is mesured in
def unit(question):
  error = "you have not selected the advalible units:"
  valid = False
  while not valid:
    unit = input(question).lower().strip()
    if unit == "meters" or unit == "m":
      unit = "meters"
      return unit
    elif unit == "centimeters" or unit == "cm":
      unit = "centimeters"
      return unit
    elif unit == "millimeters" or unit == "mm":
      unit = "millimeters"
      return unit
    else:
      print(error)
# calls on the program
measurement = unit("what unit would you like to use millimeters, centimeter, meters:")
print(measurement)