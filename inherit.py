# ## Base class (can consider this a Parent Class)
# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         print(f"{self.name} makes a sound.")
#
# ## Derived class ( child Class )
#
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} barks loudly.")
#
# ## Instance of animal
#
# # animal = Animal("Generic Animal")
# # animal.speak()
#
# #creating instance of Dog
# dog = Dog("Tyson")
# dog.speak()


#------ SUPER ------

class Animal:
    def __init__(self):
        self.name = "Tyson"

    def speak(self):
        print(f"{self.name} makes a sound.")

## Derived class

class Dog(Animal):
    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak() ## Call base class method
        print(f"{self.name} barks. It is a {self.breed}")

## Creating instance of a dog
dog = Dog("Lab")
dog.speak()
