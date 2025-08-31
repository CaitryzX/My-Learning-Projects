# Advanced Python Practice - New Concepts & Programs

print("=== ADVANCED PYTHON PRACTICE ===\n")

# 1. LIST COMPREHENSIONS (Advanced Python)
print("1. LIST COMPREHENSIONS")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares = [x**2 for x in numbers if x % 2 == 0]  # Even squares only
print(f"Original numbers: {numbers}")
print(f"Even squares: {squares}\n")

# 2. DICTIONARY COMPREHENSIONS
print("2. DICTIONARY COMPREHENSIONS")
word = "programming"
letter_count = {letter: word.count(letter) for letter in set(word)}
print(f"Word: {word}")
print(f"Letter frequency: {letter_count}\n")

# 3. LAMBDA FUNCTIONS (Anonymous functions)
print("3. LAMBDA FUNCTIONS")
add = lambda x, y: x + y
multiply = lambda x, y: x * y
print(f"Lambda add(5, 3): {add(5, 3)}")
print(f"Lambda multiply(4, 6): {multiply(4, 6)}\n")

# 4. MAP, FILTER, REDUCE
print("4. MAP, FILTER, REDUCE")
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Original: {numbers}")
print(f"Doubled: {doubled}")
print(f"Even numbers: {evens}\n")

# 5. ERROR HANDLING (Try-Except)
print("5. ERROR HANDLING")
def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except TypeError:
        return "Error: Please enter numbers only!"

print(f"10 / 2 = {safe_divide(10, 2)}")
print(f"10 / 0 = {safe_divide(10, 0)}")
print(f"10 / 'abc' = {safe_divide(10, 'abc')}\n")

# 6. FILE OPERATIONS
print("6. FILE OPERATIONS")
# Create a sample file
with open("sample.txt", "w") as file:
    file.write("Hello, this is a sample file!\n")
    file.write("Python is amazing for file handling.\n")
    file.write("Keep learning and growing!\n")

# Read the file
print("Reading from file:")
with open("sample.txt", "r") as file:
    content = file.read()
    print(content)

# 7. CLASSES AND OBJECTS (OOP)
print("7. CLASSES AND OBJECTS (OOP)")
class Calculator:
    def __init__(self, name):
        self.name = name
        self.history = []
    
    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result
    
    def show_history(self):
        print(f"{self.name}'s calculation history:")
        for calc in self.history:
            print(f"  {calc}")

# Create calculator object
my_calc = Calculator("My Calculator")
print(f"Calculator name: {my_calc.name}")
print(f"5 + 3 = {my_calc.add(5, 3)}")
print(f"10 + 20 = {my_calc.add(10, 20)}")
my_calc.show_history()

print("\n=== END OF ADVANCED PRACTICE ===")
