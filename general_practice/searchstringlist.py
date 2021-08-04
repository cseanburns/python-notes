#!/usr/bin/python3

# code used to search for a string, in this case the letter "n", in a
# list

import re

mainletter = "t"
kids = ["thor", "loki"]
results = re.compile(".*{}".format(mainletter))
updated_kids = list(filter(results.match, kids))
print(updated_kids)
