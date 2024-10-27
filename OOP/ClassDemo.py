class Animal:
    # some behaviour / functionality
    def eat(self):
        print("Animal is earing")
    def walk(self):
        print("Animal is walking")

    #  some peoperties / attributes
    noOfLegs = 4
    color = "Black"

dog1  = Animal()
print(dog1.color)
print(dog1.noOfLegs)
dog1.walk()

dog2  = Animal()
print(dog2.color)
print(dog2.noOfLegs)
dog2.walk()
