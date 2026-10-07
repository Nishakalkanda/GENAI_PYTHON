name = "Nisha"

print(f"Hello, {name}! Welcome to Python.")


#Daily Assignment: Building a calculator with input validation

a = input("Enter the first number: ")
b = input("Enter the second number: ")

operation = input("Enter the operation( +, -, *, /): ")

if operation == "+":
    result = int(a) + int(b)
    print(f"The sum of {a} and {b} is {result}")
elif operation == "-":
    result = int(a) - int(b)
    print(f"The difference of {a} and {b} is {result}")
elif operation == "*":
    result = int(a) * int(b)
    print(f"The product of {a} and {b} is {result}")
elif operation == "/":
    result = int(a) / int(b)
    print(f"The quotient of {a} and {b} is {result}")
else:
    print("Invalid operation. Please enter a valid operation.")
    
    
#Hands-On Practice
# Practice Exercises:
# Store user’s name, age, and city using input() and print a welcome message.
# Perform and print results of arithmetic operations using input values.
# Convert string inputs to appropriate data types.
# Display data using all three string formatting methods
    
  
#1 : Store user’s name, age, and city using input() and print a welcome message.    
    
    
name = input("Enter your Name : ")
age =  int(input("Enter your Age: "))
city = input("Enter your city name: ")

while not city.isalpha():
    print("please enter correct city name")
    city = input("Enter your city name: ")
    
print(f"Hello your username is {name}, you are {age}yrs old and you live in {city}")


#2: Convert string inputs to appropriate data types.

age = input("Enter your Age: ")
type_of_age = type(age)
print(f"Your age is {age} and its data type is {type_of_age}")
age = int(input("enter your age: "))
type_of_age = type(age)
print(type_of_age)


#3 : Display data using all three string formatting methods

name = "NISHA"
age = 25
city = "Noida"

#f-strings

print(f"Hi {name}, you are {age}yrs old and you are living in {city}")

#concatenation

print("Hi " +name+", you are "+str(age)+ "yrs old and you are living in "+ city)

# formatting

print("Hi {}, you are {}yrs old and you are living in {}".format(name, age, city))