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
option = choice("what would you like to calculate area or permiter:")
print(option)