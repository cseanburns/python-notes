#!/usr/bin/python3

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def some_name(self):
    print("Hello my name is " + self.name)

  def some_age(self):
      print("I am " + str(self.age) + " years old.")

p1 = Person("Eddie", 125)
p1.some_name()
p1.some_age()
