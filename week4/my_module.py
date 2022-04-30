from math import pi, pow

def rectangle(a, b):
    return round(a*b, 2)
def triangle(a, h):
    return round(0.5 * a *h , 2)
def circle(r):
    return round(pi * pow(r, 2), 2) 



# FOLLOWING SHOULD BE CONTAINED IN THE CALLING FILE:

import my_module
print(my_module.rectangle(2, 3))

#or

from my_module import rectangle, triangle, circle
print(circle(3))

#or 

from my_module import * #same as the previous


import json
print(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))
#'["foo", {"bar": ["baz", null, 1.0, 2]}]'
print(json.dumps("\"foo\bar"))
#"\"foo\bar"
print(json.dumps('\u1234'))
#"\u1234"
print(json.dumps('\\'))
#"\\"

#json dumps creates a string