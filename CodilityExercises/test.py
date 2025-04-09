txt = "We are the so-called \"Vikings\" from the north."
print(txt)


x = 15
y= 10
print(x//y)

value = 10
result = value << 3
print(result)


evenSquares = [x**2 for x in range(10) if x % 2 == 0]
print(evenSquares)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana", 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print(thislist[-1])
# Convert this list into a string before sorting
newlist = [str(x) for x in thislist]
newlist.sort()
#thislist.sort()
print(newlist)


# Generate a list of factorials using list comprehension without math module
#factorials = [1 if i == 0 else i * factorials[i-1] for i in range(10)]
#print(factorials)  # Output: [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

fibonacci = [0, 1]
[fibonacci.append(fibonacci[-1] + fibonacci[-2]) for _ in range(8)]
print(fibonacci)  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


mylist = ['apple', 'banana', 'cherry']
print(mylist)
mylist[0] = 'kiwi'
print(mylist)
print(mylist[1])

fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits
print("Unpacking a tuple")
print("green = " + green)
print("yellow = " + yellow)
print("red = " + red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print("green = " + green)
print("yellow = " + yellow)
print("red = " + str(red))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

print(p1)



p1 = Person("John", 36)
p1.myfunc()

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    self.b = 2
    return self

  def __next__(self):
    x = self.b
    self.b ^= 4
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


import platform

x = platform.system()
print(x)

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

x = datetime.datetime(2020, 5, 17)

print(x)

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))


import re

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.split("\s", txt)
print(x)

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object
print(x.span()) #this will print a tuple containing the start and end positions of the match.
print(x.string) #this will print the string passed into the function
print(x.group()) #this will print the part of the string where there was a match

txt = f"The price is 49 dollars"
print(txt)


price = 59
txt = f"It is very {'Expensive' if price>50 else 'Cheap'}"

print(txt)

price = 59000
txt = f"The price is {price:,} dollars"
print(txt)

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

print(arr)

print(type(arr))


for i in range(10, 0, -1):
    print(i)
