#!/usr/bin/python3

# generate a random string of characters 
# that contain upper and lowercase letters
# Date: 8/3/2021

# For a much better example, see:
# https://docs.python.org/3/library/secrets.html

import string
import random

list_lower = string.ascii_lowercase
list_upper = string.ascii_uppercase

# random.sample converts the string above to a list
list_lower_rand = random.sample(list_lower, 26)
list_upper_rand = random.sample(list_upper, 26)

# create a single list from the two
for i in list_upper_rand:
    list_lower_rand.append(i)

# generate 9 items from the combined list
list_combo_rand = random.sample(list_lower_rand, 9)

# print the 9 item list as a single string
print(''.join(list_combo_rand))
