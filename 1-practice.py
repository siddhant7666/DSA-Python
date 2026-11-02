print("Hello")


def add(a, b):
    return a + b

print(add(10, 20))

###############################################
#formatting code:
x =5 
y=10
if x<y:
    print("x is smaller")


x=5
y=15
if x>y: print("new")



#################### VARIABLES

name = "Raj"
age = 25
city = "Mumbai"
print(f"my name is {name}, and my age is {age}, and my city is {city}")

##################### Strings

name = "raj"
print(f"my name is {name}, and my age is {age}, and my city is {city}")

# we can also reassign different value to same variable, it wont give error

name = 25
print(name)
#Python executes code from top to bottom. Every time you assign a new value to name, the previous value gets replaced.

#Python variables are dynamically typed. You can:
# Declare a variable.
#- Assign a new value to the same variable.
#- Change its data type.
#- Reuse it whenever needed.
name = "Raj"       # String
name = "Shivam"    # New string
name = 25          # Integer
name = 25.5        # Float
name = True        # Boolean

print(name) # True will be printed

# f-strings are used to insert variables into text 

name = "Raj"
age = 25
print(f"My name is {name} and I am {age} years old")



#String methods - tomorrow 