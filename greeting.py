# Make a function called greet.
# The function should take a name and print "Hello, [name]!"
# Ask the user for their name and use the function to greet them.
# Then call the function again with 3 different names.
# New thing to practice: giving information to a function using parameters.

def greet(name):
    print(f"Hello {name}")

p=0
while(p!=3):
    greet(input("What is your name?"))
    p+=1
