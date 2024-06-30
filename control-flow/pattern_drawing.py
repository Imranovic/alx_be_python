size = int(input("Enter the size of the pattern: "))
# Ensure the input is a positive integer
if size > 0:
    row = 0
    while row < size:
        
        for _ in range(size):
            print("*", end="")
        print()
        row += 1
else:
    print("Please enter a positive integer.")