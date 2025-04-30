# Functions with input


# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# Functions with more than one input

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")
greet_with("Gloria" , "Kumasi")


# #adding keyword argument
greet_with( name="Emma", location="Techiman")
greet_with( location="Techiman", name="Emma")

# count1 = 0