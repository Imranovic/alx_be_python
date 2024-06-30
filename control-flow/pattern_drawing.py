size = int(input("Enter the size of the pattern: "))
# Ensure the input is a positive integer
if size > 0:
    # Initialize the row counter
    row = 0
    
    # Iterate through each row of the pattern
    while row < size:
        # Print asterisks side by side for the current row
        for _ in range(size):
            print("*", end="")
        # Print a newline character to move to the next row
        print()
        # Increment the row counter
        row += 1
else:
    print("Please enter a positive integer.")