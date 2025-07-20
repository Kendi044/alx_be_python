try:
    number = int(input("Enter a number to see its multiplication table: "))
    #X = number
    
    for i in range (1, 11):
        #Y = i
        #Z = X * Y
        product = number * i
        print(f"{number} * {i} = {product}")

except ValueError:
    # Handle cases where the user inputs something that is not an integer
    print("Invalid input. Please enter an integer.")
