# Simple calc

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x*y

# Function to devide two numbers
def devide(x, y):
    return x/y

print("Select an operation")
print("1 Add")
print("2 Subtract")
print("3 Multiply")
print("4 Devide")

# User input
choise = input("Input number operation(1/2/3/4): ")
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))

if choise == '1':
    print(num1, "+", num2, "=", add(num1,num2))

elif choise == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choise == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choise == '4':
    print(num1,"/",num2,"=", devide(num1,num2))

else:
    print("Incompatible input")