""" 
Name: M03 Lab - Lists, Functions, and Classes
By: Enoch E Jacobs

Description: Asks for information regarding a car and then prints it. 

Variables: 
    Vehicle     = a class that holds basic information about a vehicle (Class)
    Automobile  = a subclass that holds information regarding a car spesifically (Class)
    done        = a simple check to see if the user is satisfied with their input 
"""


# Vehicle class, holds the type of vehicle.
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# A subclass of the Vehicle class which adds additional information. 
# Including the year, make, model, number of doors, and roof style.
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# The start of the main loop. Returns back to this point 
# if the user decides they messed up and want to reenter their info.
while True:
    #Create an instence of Vehicle labled "Our_Car".
    Our_Car = Vehicle("Car")
    #Ask for information regaurding it.
    print("\nTell us about your car.")
    Our_Car.year    = input("What was the year that your car was made? ")
    Our_Car.make    = input("What is the make of your car? ")
    Our_Car.model   = input("What is the model of your car? ")
    Our_Car.doors   = input("How many doors does your car have? ")
    Our_Car.roof    = input("What type of roof does your car have? ")
    
    #Print out the information given and ask if it is correct.
    print(f"""\nAlright, please look this over and make sure that the information presented is accurate.
        
Vehicle Type: {Our_Car.vehicle_type}
Year: {Our_Car.year}
Make: {Our_Car.make}
Model: {Our_Car.model}
Number of Doors: {Our_Car.doors}
Type of Roof: {Our_Car.roof}""")
    # Ask the user for confermaion. If yes, break out of the loop and end the program. 
    # If no, loop back and reenter the information.
    done = input("\nIs this correct? Type yes/y if so.")
    if done.lower() in ["yes", "y",]: break