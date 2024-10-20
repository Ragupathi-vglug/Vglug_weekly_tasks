#single inheritance 
class Animal:  # Superclass
    def speak(self):
        return "Animal speaks"

class Dog(Animal):  # Subclass
    def bark(self):
        return "Woof!"

my_dog = Dog()
print(my_dog.speak())  
print(my_dog.bark())   
