def choice():
  choice = input("what would you like to calculate area or permiter:")
  error = ("please answer with area or perimeter")
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

option = choice("please enter area or peremeter")
print(option)