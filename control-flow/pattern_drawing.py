try:

  size_string = input("Enter the size of the pattern: ")
  size = int(size_string)

  if size <= 0:
      print("Please enter positive interger for the pattern size.")
  else: 
      current_row = 0

      while current_row < size:
          for _ in range (size):
              print("*", end="")

          print()
        
          current_row += 1
except ValueError:
    # Handle cases where the user inputs something that is not an integer
    print("Invalid input. Please enter an integer.")