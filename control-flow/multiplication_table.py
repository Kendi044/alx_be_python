try:
    number = int(input("Enter a number to see its multiplication table: "))
    X = number
    
    for i in range (1, 11):
        Y = i
        Z = X * Y
  
        print(f"{X} * {Y} = {Z}")

except ValueError:
    # Handle cases where the user inputs something that is not an integer
    print("Invalid input. Please enter an integer.")