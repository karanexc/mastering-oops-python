## Initiating a class

class Employee:
    #special method/magic method -> constructor
    # this will run as soon as method is initiated (sam = Employee())
    def __init__(self):
        print("Started executing attributes/data")
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        print("attributes/data have been initiated")

    ## Method
    def travel(self, destination):
        print("This travel function was called manually")
        print(f"Employee is now travelling to {destination}")


# Creating an OBJECT/instance of the class
sam = Employee()

## Printing the attributes
# print(sam.designation)

## Calling a METHOD manually
# sam.travel("Monaco")
print(type(sam))