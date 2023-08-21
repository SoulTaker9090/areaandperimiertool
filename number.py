def num_check(question):
  error = ("Please enter an integer")
  while True:
    try:
      response = int(input(question))
      return response
    except ValueError:
      print(error)