#!/usr/bin/python3

class Family:
    def __init__(self, age, fname, catch):
        self.age = age
        self.fname = fname
        self.catch = catch

    def walk(self):
        print(self.fname + " is walking ...")
        print(self.fname + " is " + str(self.age) + " years old.")
        print(self.fname + " likes to say, " + "'" + str(self.catch) + "'")

    def run(self):
        print(self.fname + " is not running...")

p1 = Family(98, "Tyr", "Yeah.")
p1.walk()
p1.run()

p2 = Family(63, "Frig", "So...")
p2.walk()
p2.run()

age = input("What is your age? ")
name = input("What is your name? ")
catch = input("What is your catchphrase? ")
p3 = Family(age, name, catch)
p3.walk()
p3.run()

print("##########")
for i in p1, p2:
    p1.walk()
    print("----------")
    p2.walk()
    print("----------")
    p3.walk()
    print("----------")
