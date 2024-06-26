size= int(input("Enter the size of the pattern: "))

if size <= 0:
    print("Enter a positive number.")
else:
    row=0
    while size > row:
        for i in range(size):
            print("*", end="")
        print()
        row += 1
