
# Solutions to Practice Questions - Floating Point Numbers

print("=== SOLUTIONS TO PRACTICE QUESTIONS ===\n")

# Solution 1: Calculate the sum of three floating numbers
print("Solution 1: Sum of three floating numbers")
a = float(input("Enter 1st number: "))
b = float(input("Enter 2nd number: "))
c = float(input("Enter 3rd number: "))
sum_result = a + b + c
print(f"Sum of {a}, {b}, and {c} is: {sum_result}\n")

# Solution 2: Calculate the product of two floating numbers
print("Solution 2: Product of two floating numbers")
x = float(input("Enter 1st number: "))
y = float(input("Enter 2nd number: "))
product = x * y
print(f"Product of {x} and {y} is: {product}\n")

# Solution 3: Calculate the difference between two floating numbers
print("Solution 3: Difference between two floating numbers")
num1 = float(input("Enter 1st number: "))
num2 = float(input("Enter 2nd number: "))
difference = num1 - num2
print(f"Difference of {num1} - {num2} is: {difference}\n")

# Solution 4: Calculate the quotient of two floating numbers
print("Solution 4: Quotient of two floating numbers")
dividend = float(input("Enter dividend: "))
divisor = float(input("Enter divisor: "))
if divisor != 0:
    quotient = dividend / divisor
    print(f"Quotient of {dividend} ÷ {divisor} is: {quotient}\n")
else:
    print("Error: Division by zero is not allowed!\n")

# Solution 5: Calculate the area of a rectangle
print("Solution 5: Area of a rectangle")
length = float(input("Enter length: "))
width = float(input("Enter width: "))
area = length * width
print(f"Area of rectangle with length {length} and width {width} is: {area}\n")

# Solution 6: Calculate the perimeter of a rectangle
print("Solution 6: Perimeter of a rectangle")
l = float(input("Enter length: "))
w = float(input("Enter width: "))
perimeter = 2 * (l + w)
print(f"Perimeter of rectangle with length {l} and width {w} is: {perimeter}\n")

# Solution 7: Calculate the average of four floating numbers
print("Solution 7: Average of four floating numbers")
n1 = float(input("Enter 1st number: "))
n2 = float(input("Enter 2nd number: "))
n3 = float(input("Enter 3rd number: "))
n4 = float(input("Enter 4th number: "))
average = (n1 + n2 + n3 + n4) / 4
print(f"Average of {n1}, {n2}, {n3}, and {n4} is: {average}\n")

# Solution 8: Calculate the square of a floating number
print("Solution 8: Square of a floating number")
number = float(input("Enter a number: "))
square = number ** 2
print(f"Square of {number} is: {square}\n")

# Solution 9: Calculate the cube of a floating number
print("Solution 9: Cube of a floating number")
num = float(input("Enter a number: "))
cube = num ** 3
print(f"Cube of {num} is: {cube}\n")

# Solution 10: Calculate the percentage
print("Solution 10: Calculate percentage")
part = float(input("Enter the part: "))
total = float(input("Enter the total: "))
if total != 0:
    percentage = (part / total) * 100
    print(f"{part} is {percentage:.2f}% of {total}\n")
else:
    print("Error: Total cannot be zero!\n")

print("=== ALL SOLUTIONS COMPLETED ===")
