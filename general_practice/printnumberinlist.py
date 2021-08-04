#!/usr/bin/python3

## LISTS

# get numbers from list greater than some value:
ages = [7, 12, 44, 63, 98]

# Get list of ages if i > 15:
for i in ages:
    if i > 15:
        print(i)

# Get list of ages if i > 15 and < 48:
for i in ages:
    if i > 15 and i < 48:
        print(i)

# With Boolean not:
for i in ages:
    if not i >= 44:
        print(i)

## TUPLES

family_names = ("Thor", "Loki", "Frigg", "Odin", "Tyr")

for i in family_names:
    print(i)

for i in family_names:
    if i != "Tyr":
        print(i)

family_ages = (7, 12, 44, 63, 98)

for i in family_ages:
    if i > 15:
        print(i)

for i in family_ages:
    if not i >= 12:
        print(i)

for i in family_ages:
    if i > 15 and i < 48:
        print(i)

for i in family_ages:
    if not i >= 12 and i < 98:
        print(i)

for i in family_ages:
    if not i == 12 and not i == 44:
        print(i)

## DICTIONARIES

familydict = {
        "Thor": 7,
        "Loki": 12,
        "Odin": 44,
        "Frig": 63,
        "Tyr": 98
        }

# Get keys
for i in familydict:
    print(i)

# Get values; the following two are the same
for i in familydict:
    print(familydict[i])

for i in familydict.values():
    print(i)

# Get keys that meet some condition
for i in familydict:
    if familydict[i] > 44:
        print(i)

# Get values that meet some condition 
for i in familydict:
    if familydict[i] > 44:
        print(familydict[i])

for i in familydict.values():
    if i > 44:
        print(i)

## List Comprehension
## https://blog.finxter.com/python-one-line-for-loop-lambda/
## Formula is: [ expression + context ]
## https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

ages = [7, 12, 44, 63, 98]

# print ages greater than 18
adults = [ x for x in ages if x >= 18 ]
print(adults)

# print ages less than 18
minors = [ x for x in ages if x < 18 ]
print(minors)

# List of tuples
family = [("Thor", 7),
          ("Loki", 12),
          ("Odin", 44),
          ("Frig", 63),
          ("Tyr", 98)]

adults = [ x for x, y in family if y >= 18 ]
print(adults)

minors = [ x for x, y in family if y < 18 ]
print(minors)

minors = [ x for x, y in family if y > 12 and y < 98 ]
print(minors)

minors = [ x.lower() for x, y in family if y > 1 and y < 9 ]
print(minors)

## Dictionary Comprehension

family = {"Thor": 7, "Loki": 12, "Odin": 44, "Frig": 63, "Tyr": 98}

print(family.keys())
print(family.values())

minors = { x:y <= 18 for (x, y) in family.items()}
adults = { x:y > 18 for (x, y) in family.items()}
minors = { x.lower():y <= 18 for (x, y) in family.items()}
minors = { x.upper():y <= 18 for (x, y) in family.items()}

