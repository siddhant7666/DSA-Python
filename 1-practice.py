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

print("hey",name)
print("hey " + name) #concatenation
print(len(name))
print("Line1\nLine2") #escape sequence
print("Line1\tLine2") #escape sequence
print("Line1\"Line2\"") #escape sequence


#STRING METHODS

text = " Hello, World! "
print(text.upper()) # converts to uppercase
print(text.lower()) # converts to lowercase
print(text.strip()) # removes whitespace from both ends
print(text.replace("Hello", "Hi")) # replaces substring
print(text.find("World")) # finds substring and returns index
print(text.split(",")) # splits string into list


print(10//3) # integer division or Floor division
print(10%3) # modulus or remainder
print(2**3) # 2 raised to the power of 3

#TYPE CONVERSION
age = "25"
#print(age+5) # This will cause an error because you're trying to concatenate a string and an integer
print(age+"5") # This will concatenate the string "25" and "5", resulting in "255"
age_num = int(age) # convert string to integer
print(age_num + 5) # will print 30

price = 99.99
price_str = str(price) # convert float to string
print(price_str + " is the price") # will print "99.99 is the price


print(5==5) # True
print(5!=5) # False
print(5<10) # True
print(5>10) # False
print(5<=10) # True
print(5>=10) # False

marks = 86

if marks>=100:
    print("Excellent")
elif marks>=90:
    print("Very Good")
elif marks>=80:
    print("Good")
    if marks>=85:
        print("Average")
else:
    print("Needs Improvement")
    
    
    
#TERNARY OPERATOR

age = 20
status = "Adult" if age >=18 else "Minor"
print(status) # will print "Adult" because age is 20 which is greater than 18


has_id = True

if age>=18 or has_id:
    print("You can vote")
    
    
say = True
print(not say) # will print False because say is True and not operator negates it
    
    
    
    


a = 5   # Binary: 0101
b = 3   # Binary: 0011

print(a & b)   # AND:   0001 = 1  (Both bits 1)
print(a | b)   # OR:    0111 = 7  (Either bit 1)
print(a ^ b)   # XOR:   0110 = 6  (Bits are different)
print(~a)      # NOT:   -6       (Flips bits; ~5 = -6)
print(a << 1)  # Left:  1010 = 10 (Shift left by 1)
print(a >> 1)  # Right: 0010 = 2  (Shift right by 1)

#FOR LOOPS
print("For loop example:")

i=2
for i in range(5):
    print(i)  # will print numbers from 0 to 4
print(i)

for j in range(3,10,-1):
    print(j) # will not print anything because the step is negative and start is less than stop
    
    
for i in range(10, 0, -2):
    print(i)  # will print 10, 8, 6, 4, 2
    
    
for i in range(2,8):
    print(i)  # will print numbers from 2 to 7  
    
    
print(list(range(1,5))) # will print [1, 2, 3, 4]   

#print items in a list

fruits = ["apple", "banana", "cherry"]
print(fruits)  # will print the entire list
for f in fruits:
    print(f)  # will print each fruit in the list
    
print(fruits) # will print the entire list again


#FOR LOOP WITH ELSE 

for i in range(3):
    print(i)
else:
    print("Loop done!") # will print "Loop done!" after the loop finishes normally without a break statement
    
    
#FOR ELSE WITH BREAK
for i in range(5):
    if i==3:
        break
    print(i)
else:
    print("Loop done!") # will not print because the loop was exited with a break statement
    
    
    
#NESTED FOR LOOPS
for i in range(3):
    for j in range(2):
        print(i ,j)  # will print pairs of i and j values
        
#WHILE LOOP 

i = 1
while i<5:
    print(i)
    i += 1
    
#INFINITE LOOP
while True:
    print("This will run forever unless you break it")
    break  # This will exit the loop immediately


#function

def greet(name):
    print(f"Hello, {name}")# will print "Hello, Raj"
    
greet("Raj")



def my_func(a, b=5):
    return a + b

result = my_func(10)  # b will take the default value of 5
print(result)  # will print 15

result = my_func(10, 3)  # b will take the value of 3
print(result)  # will print 13


def my_func1(country="India"):
    print("I am from " + country)

my_func1("Sweden") #overrides default "India"
my_func1() # Uses default "India"



def my_func2(*kids):
    print("The youngest child is " + kids[2])

my_func2("Emil", "Tobias", "Linus")

####################################################

#name = input("Enter your name: ")
#age = input("Enter your age: ")
#print(f"Hello {name}, you are {age} years old.")


a = int(input("Enter first digit: "))
b = int(input("Enter second digit: "))

operation = int(input("For addition, please Enter 1\nFor subtraction, please Enter 2\nFor multiplication, please Enter 3\nFor division, please Enter 4\n"))

try:
    match operation:
        case 1:
            print(f"The sum of {a} and {b} is {a+b}")
        case 2:
            print(f"The difference of {a} and {b} is {a-b}")
        case 3:
            print(f"The product of {a} and {b} is {a*b}")
        case 4:
            if b==0:
                print("Division by zero is not allowed")
            else:
                print(f"The division of {a} by {b} is {a/b}")
        case _:
            print("Invalid operation selected")
            
except ValueError:
    print("Invalid input. Please enter numeric values for digits and operation.")
# if a=10, b=5, operation = abc then it will print "Invalid input. Please enter numeric values for digits and operation."
        
            
    
    
num = int(input("Enter a number: "))
if num%2==0:
    print("Num is even")
else:
    print("num is odd")