# Design condition-based decisions such as:
# Check if a number is positive, negative, or zero
# Determine voting eligibility based on age
# Categorize people based on age groups (child, teen, adult, senior)

#1 Check if a number is positive, negative, or zero

print("THSIS IS FOR +VE,-VE NUMBERS")

a = int(input("Enter a number: "))

if a > 0: 
    print(f"{a} is a +ve no.")
elif a < 0:
    print(f"{a} is -ve no.")
else:
    print(f"{a} is zero")
          


#2 Determine voting eligibility based on age

print("VOTING ELIGIBILITY PROGRAM")

age = int(input("Enter user age: "))

if age >= 18:
    print(f" user is eligible for voting")
else:
    print(f"user is not eligible for voting")
    
    
    
#3 Categorize people based on age groups (child, teen, adult, senior)   

print("AGE GROUP CATEGORY PROGRAM")           

age = int(input("Enter user age: "))

if age <= 15:
    print(f"user is child")
elif age <= 20:
    print(f"user is teen")
elif age <= 50:
    print(f"user is adult")
else:
    print(f"user is senior")
        

#DAILY ASSIGNMENT GRADING BASED ON MARKS


print("DAILY ASSIGNMENT GRADING BASED ON MARKS")


marks = int(input("Enter yoyr marks: "))

if marks >= 90:
    print(f"grade is A+")
elif marks >= 80:
    print(f"grade is A")
elif marks >= 70:
    print(f"grade is B")
elif marks >= 60:
    print(f"grade is C")
elif marks >= 50:
    print(f"grade is D")
else:
    print(f"grade is F")
            
            
            
            
# Writing loops to iterate over lists, strings, and numeric ranges

print("ITERATING LIST, TUPLES, STRINGS AND NUMERIC RANGES")
a = [1, 2, 33, 23]

for i in a:
    print(i)
    


b = ["Nisha", "Amitesh", "MS"]

for i in b:
    print(i)                      
                       
                       
                       
name = "NISHA"

for char in name:
    print(char)


for i in range(1, 6):
    print(i)
    
    
# Using nested loops for pattern generation

print("NESTED LOOPS")

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()
    
    
#Applying loop control statements in appropriate situations

print("LOOP CONTROL STATEMENTS")
for i in range(1, 6):
    if i == 5:
        break
    print(i)                     
    
    


for i in range(1, 6):
    if i == 3:
        continue
    print(i)    
    
    
    

print("MIN, MAX NUMBERS IN A LIST")


a = [10, 20, 30, 40, 50]

max_num = a[0]

for i in a:
    if i > max_num:
        max_num = i
print(f"max number in a list is {max_num}")    


print("THIS IS FOR MIN")

min_num = a[0]

for i in a:
    if i <min_num:
        min_num = i
print(f"min number in a list is {min_num}")



print("SUM OF NUMBERS IN A LIST")

total = 0

for i in a:
    total += i
print(f"sum of numbers in a list is {total}")
    
    
    
    
print("PATTERN GENERATION USING NESTED LOOPS")


# *
# **
# ***
# ****
# *****    

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end=" ")
    print()
        


for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end = " ")
    print()
    


for i in range(1, 6):
    for j in range(1, 6):
        print(j, end=" ")    
    print()