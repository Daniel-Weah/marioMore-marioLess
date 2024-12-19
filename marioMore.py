height = int(input("Enter the Height: \n"))
result = "#"

for i in range(height):
    spaces = " " * (height - i - 1)
    row = result * (i + 1)
    print(spaces + row + "  " + row)