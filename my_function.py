def greet():
    """
    A simple function that prints Hello!
    :return: None
    """
    print("Hello!")

greet()
greet()

def greet2(name):
    """
    A more advanced greet function that returns Hello with a parameter
    :param name: Name of the person to greet
    :return: None
    """
    print(f"Hello {name}!")

greet2("Jaime")

def average(a, b):
    """
    Average of two numbers
    :param a: first number
    :param b: second number
    :return: float, average of a and b
    """
   # average = (a*b)/2 used to store the value but not necessary
    return (a*b)/2 #this is how a function gives back a value
print(average(10,5))

def divide(x, y):
    """
    Divide x by y
    :param x: first number
    :param y: second number
    :return: float, division of x and y
    """
    if y == 0:
        return None
    return x/y
print(divide(10, 20))
print(divide(10, 0))
print(divide(10, 1))
print(divide(y = 1, x = 10)) #another way of using the function defining the values yourself

def dividefix(x, y=2):
    """
    Divide x by 2 all the time
    :param x: first number
    :param y: second number
    :return: float, division of x and y
    """
    if y == 0:
        return None
    return x/y
print(dividefix(30)) #no need to introduce the y because its already fixed as a 2
print(dividefix(30, 20 )) #you can still give a value to y if needed

#James bond inspired examples example
def bond(first_name, last_name):
    return f"{last_name}, {first_name} {last_name}"
def introduce(name):
    print(f"The name is {name}")

print(bond("James", "Smith"))
introduce(bond("James", "Smith"))

#Automatization of James Bond example
def bond(first_name = "James", last_name = "Bond"):
    return f"{last_name}, {first_name} {last_name}"
def introduce(name):
    print(f"The name is {name}")
introduce(bond()) #If not specified it will return the original line
introduce(bond(first_name="Jaime", last_name="Matesanz"))