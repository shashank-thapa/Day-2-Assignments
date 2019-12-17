#Create a class named Dog with an attribute name. Now, define a constructor to this class that takes the name of dog as an argument and then initialize the name 
# field of the class Dog. Also, define a function named bark that displays the message I am a dog. My name is ... with its corresponding name. 
# Now, define two more classes named Labrador and GermanShepherd that inherit from the class Dog. Both of these classes must have a new attribute called owner and also a 
# constructor to initialize it. Inside the Labrador class, override the bark method with new definition to override the parent and then display the message I am Labrador. 
# My master is ... with its owner's name.Now from outside the class, create objects of all three classes Dog, Labrador and GermanShepherd and then call bark method using that object.

class Dog:

    def __init__(self, name):
        self.name = name
    def bark(self):
        print('I am a dog. My name is ', self.name)

class Labrador(Dog):

    def __init__(self, name ,owner):
        self.name = name 
        self.owner = owner
    def bark(self):
        print('I am Labrador. My master is ', self.owner)

class GermanShepherd(Dog):

    def __init__(self, name ,owner):
        self.name = name 
        self.owner = owner

d = Dog('Jack')
d.bark()

l = Labrador('Luna', 'Sagyan')
l.bark()

g = GermanShepherd('Tony', 'Bigyan')
g.bark()