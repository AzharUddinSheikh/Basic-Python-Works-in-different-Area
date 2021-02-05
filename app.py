# high_income = True
# good_credit = True
# student = True

# if high_income and good_credit and not student:
#     print('eligible')
# else:
#     print('not eligible')


# age = 25

# if age >= 18 and age <= 25:
#     print('eligible')
# else:
#     print('not eligible')


# if 18 <= age <= 25:
#     print('eligible')
# else:
#     print('not eligible')

# for number in range(3):
#     print('attempt', number+1, (number+1)*".")

# for number in range(1, 10, 3):
#     print('attempt', number)

'''for else'''

# successfull = False
# for number in range(3):
#     print('attempt')
#     if successfull:
#         print('successful')
#         break

#  else execute only when for loop work and break doesnot
# else:
#     print('attempted and failed to success')

'''nested loop'''

# for x in range(5):
#     for y in range(3):
#         print(f'({x,y})')

'''iterable'''

# print(type(ra/nge(5)))

# range function is iterable means we can iterate its inside value
# string are also iterable
# List

# for x in "Python":
#     print(x)


'''while loop'''
# its ll iterable until condition statisfied
# this will keep on interating if condition failed then while loops break

# number = 100
# while number > 0:
#     print(number)
#     number //= 2

# command = ""
# while command.lower() != "quit":
#     command = input('>')
#     print("echo", command)

'''infinite loop'''
#  now you dont need command variable as empty string bcoz we have infinit loop

# while True:
#     command = input('>')
#     if command.lower() == "quit":
#         break

# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)
# print(f'we have {count} even number in given range')


"""function"""


# def greet():
#     print('hi there')
#     print('welcome')


# greet()

#  difference between greet and print where print function take input and greet function may or maynot required input

'''arguments and parameter of the function'''

# first name and last name are parameter of the function which define your function
# def greet(first_name, last_name):
#     print(f'hi there {first_name} {last_name}')
#     print('welcome board')

'''where value of given parameter are called argument here azhar and sheikh are arguements
   and these values are required when parameter defined'''

# greet("Azhar", "Sheikh")

'''Type of functions'''

#  about examples are performing the task type function
#  now lets look on returing the task type functions


# def greet(first_name):
#     print(f'hi {first_name}')


# def greet2(first_name):
#     return f'hi {first_name}'


# message = greet2('Azhar')
# print(message)

'''which one is better ofcourse second one we can reuse, write it , send it etc '''


'''keyboard arguement'''


# def increment(number, by):
#     return number+by


# print(increment(2, by=1))
# # print(increment(by=2,2)) error positional arguments comes first

# where 2 is positional argument and by=1 is keyword arguments

'''default argument'''
# by is optional now bcoz we provided default values of by parameter
# also default arguemnt comes after required parameters

# def increment(number,by=2):
#     return number+by


# print(increment(2,2))

'''args'''
# name/variable followed by aster


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

'''**kwargs'''
#  its ll allow to provide user multiple varibale
#  and package them in dictionary

# def user(**details):
#     print(details)


# user(id=1, name="Azhar", age=22)


'''scope'''

#  local varible define in a function only
# its have a short life time
#  python allocatte memory when this fucntion called

# global variable it ll define any where in a code
#  to define in afunction we have to set gloabl before defining
#  avoid if you can donot define in afunction its not in a good practise

'''debuggin'''
# create breakpoint on print start fn+f9
# start debuggin fn+f5 it ll open pallete select first option currently active python file
# now check your code line by line fn+f10 to swtich line
#  fn + f11 to go inside function if define


# def multiple(*number):
#     total = 1
#     for num in number:
#         total *= num
#     return total


# print('start')

# multiple(1, 2, 3)

'''short cut '''
# alt + up/down to move line up and down
#  shift alt and up/down to duplicate the line

'''data structure'''
'''list'''

# list = ['a', 'b', 'c']
# matrix = [[0, 1], [1, 2]]

# zeros = [0]*10
# print(zeros)

# combine = zeros + list
# print(combine)

from abc import ABC, abstractmethod
import json
import  datetime
from timeit import timeit
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
number = list(range(20))
# print(number)

char = list('my name is azhar uddin sehikh')
# print(char)
# print(len(char))

letter = ['a', 'b', 'c']
# print(letter[1])
# print(letter[-1])
# letter[0] = 'A'
# print(letter)

# print(letter[::-1])


# number = list(range(20))
# print(number(::2))

''' ḷist unpacking '''
# number = [1, 2, 3]
# first = number[0]
# second = number[2]
# list unpackung
# first, second, third = number

# print(first)

'''packing list '''
number = [1, 2, 3, 4, 5, 6]
# first, second, *other = number
# first, *other, last = number
# print(first)
# print(second)
# print(other)

'''iterate over list'''

# with indexing
letter = [1, 2, 3, 4]
# for x in enumerate(letter):
#     print(x)

# for x in enumerate(letter):
#     print(x[0], x[1])

# when we do x,i = list
#  its provide tuple to counter it we

# adding items in a list

letter.append(5)
# print(letter)

# adding element in a specific position
letter.insert(1, 6)
# print(letter)

# removing the element
letter.pop()

# removing the specific position
letter.pop(1)

# removing element starting with b and first ll be removed out
# letter.remove(6)

# removing element with del method it ll delete the range of element
del letter[0:2]

# to remove all element of the object or variable
letter.clear()

'''finding object in a list '''

letters = ['a', 'b', 'c']

# counting the occurence of the element in a list  if not exist means 0
letters.count('d')

# finding index of the element if not exist throw error
letters.index('a')

# to handle error when element not exists
if "d" in letters:
    letters.index('d')

'''sorting a list '''

number = [3, 4, 5, 2, 3, 4, 1, 9]

# sorting in a ascending order
number.sort()

# sorting in a reverser order
number.sort(reverse=True)

# build in function
sorted(number)
sorted(number, reverse=True)

# sorting a complex list
items = [
    ("product1", 120),
    ("product2", 110),
    ("product3", 410)
]
# need to define a function first


def sort_item(items):
    return items[1]


# not calling the function also passing reference of it , with keyword argument
items.sort(key=sort_item)

# by lambda function to clean our code
items.sort(key=lambda items: items[1])

'''lambda function or anonymous function '''


def sum(x, y): return x+y


sum(5, 3)

'''Map function'''

items1 = [
    ("product1", 120),
    ("product2", 110),
    ("product3", 410)
]

price = []
for item in items:
    price.append(item[1])
# print(price)

# alternative with map function , this is an object u have to iterate to get values
x = map(lambda item: item[1], items1)

# in a list
price = list(map(lambda item: item[1], items1))

'''filter function '''
# lets filter our items1 list only price greater or equal to 120

items1 = [
    ("product1", 120),
    ("product2", 110),
    ("product3", 410)
]

filtered = list(filter(lambda item: item[1] >= 120, items1))


"""list comprehensions"""

# lets say you need the price of the items1 (result = expressions)
# [expressions for item in items1]

# alternate of mapping
# price = list(map(lambda item: item[1], items1))
price = [item[1] for item in items1]

# filtered = list(filter(lambda item: item[1] >= 120, items1))
filtered = [item for item in items1 if item[1] >= 120]

"""zip function"""

list1 = [1, 2, 3]
list2 = [10, 20]

# need a result something like [(1,10),(2,20),(3,30)]

x = zip(list1, list2)
list(x)

y = zip('abc', list1, list2)
list(y)

# x ll be neglected
z = zip('abvx', list1, list2)
list(z)

'''stacks'''
# LIFO last in first out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
# print(browsing_session)  our stacks

last = browsing_session.pop()
# print(last) last page remove from our browsing session

# browsing_session[-1] ll give you last element of our stacks this expression comes after if statement
x = ("redirect", browsing_session[-1])

# if our stack empty we ll disable our back button
if not browsing_session:
    browsing_session[-1]

"""Queue"""

# first in first our


queue = deque([])

queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()

if not queue:
    print('empty')

"""tuple"""


# read only data type
# point type is tuple

point = tuple([1, 2, 3])
point = ()
point = 1,

point = (1, 2) + (3, 4)
point = (1, 2) * 3

x, y = (1, 2)
# also can indexing and slicing

'''swapping variable'''

x = 10
y = 20

# lets swap

z = y
y = x
x = z

#  alternative also how on right side we have a tuple
x, y = y, x

"""arrays"""


number = array("i", [1, 2, 3])
# number[0] = 1.2  error typecode is i google it we cant assing float

"""set"""

# collection with no duplicate

number = [1, 2, 3, 5, 3, 2, 3, 5, 6, 84, 2, 34, 5, 63, 2, 3]
first = set(number)

second = {1, 2, 2, 3, 4, 5, 2, 1}
#  we can add remove pop etc
# not in sequence and also its doesnot support indexing but we can check existence of the element with if statement

# where set shine
x = (first | second)  # union of first and second set
x = (first & second)  # intesection in both
x = (first-second)  # difference of first and second set
x = (first ^ second)  # either first or second but not both

"""dictionary"""

# unmutable key in dic
# values should not be same
# key can be deleted by del
# can add new key and also update value

points = dict(x=1, y=2)

# checking/finding key
if "a" in points:
    print(points["a"])

#  or
# if 2nd arguement doesnot pass its throw none value but in this case it ll checkit if not then a ll be assign to 0
x = points.get("a", 0)

"""for loop in dic"""

#  key result is key of the dic, points[key] gives value
for key in points:
    pass  # print(key)
for key in points:
    pass  # print(key,points[key])
for key, values in points.items():
    pass  # print(key,values)

"""dic comprehension"""

values = []
for x in range(5):
    values.append(x*2)

# alternative
values = [x*2 for x in range(5)]
values = {x: x*2 for x in range(5)}  # comphrehension in a dic

"""generator"""

# its give a generator object if our values is more than 50 its still take 120 byte memory
values = (x*2 for x in range(50))
# this expression ll take a lot our memory to see that lets import something
values = [x*2 for x in range(50)]

# its stupid to use list comprehension when working in a large data set
values = (x*2 for x in range(50))
# print("Gen Size is", getsizeof(values)) this is only 112
# print(len(values)) this ll shows you generator object has no length

values = [x*2 for x in range(50)]
# print("Gen Size is", getsizeof(values)) its shows 520

"""unpacking operator"""

number = [1, 3, 4]
# print(*number)

# lets say we have iterable value lets use unpacking operator
values = list(range(5))
values = [*range(5)]
# print(values)


# excercise

vari = "this is a common interview question"

dic = {}
for letter in vari:
    if letter in dic:
        dic[letter] += 1
    else:
        dic[letter] = 1

# for better readble
# pprint(dic, width=1)

# sorted in a desending ordre
x = sorted(dic.items(), key=lambda dict1: dict1[1], reverse=True)

'''exception and handling error '''

# also last line print in both cases if age is a string or an int
# else block execute when exception not execute

'''try:
    age = int(input('enter the age: '))
except ValueError:
    print('you didnt enter the numeric value')
else:
    print('no exception has been trown')
print('execution continues')'''


# try:
#     age = int(input('enter the age: '))
# except ValueError as ex:
#     pass
# print('you didnt enter the numeric value')
# print(ex) # error description
# print(type(ex)) # its shows class value error

'''handling different exception'''

'''try:
    age = int(input("Age: "))
    xfactor = 10/age
# multiple error in except
except (ValueError, EOFError, SyntaxError):
    print("you didnt enter the valid age ")
except ZeroDivisionError:
    print("age cannot be zero")
else:
    print('no exception thrown')
'''

'''cleaning up'''

# opening a file and closing file

try:
    file = open('app.py')
    # age = int(input('age:'))
    # xfactor = 10/age
    # file.close()  cant put here bcoz what if exception throws in above 2 vari
except (ValueError, ZeroDivisionError):
    x = 'not valid age'
    # file.close() cant put here to what if no execution throws
else:
    # file.close() can put here and except block but repeatation is bad practise
    x = 'no execption'
finally:
    file.close()

'''with statement'''
# we dont need file.close when with working "with" statement its automatically call exit method wheather its throw exception or not
try:
    # working with 2 files simultaneously with open('app.py') as file, open("another.txt") as target:
    with open('app.py') as file:
        x = 'file opened'  # here you can write in a file read it
    # age = int(input('age:'))
except ValueError:
    x = 'enter valid age'
else:
    x = 'no exception '

'''raising exceptipn'''

# creating our own message valuerror


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)

'''cost of raising exception'''

code = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be zero or less")
    return 10/age

try:
    calculate_xfactor(-1)
except ValueError as error:
    # print(error)
    pass
"""
# time taken by x = 12 sec approx when printing error
# time taken by x = .012 sec when using pass instead of printing error
x = ("time taken :", timeit(code, number=10000))

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10/age

xfactor = calculate_xfactor(-1)
if xfactor == None:
    pass
"""
# time taken by y is .0041
y = ("time taken :", timeit(code1, number=10000))


'''classes'''

# object oriented programming (inheritance , encapsulation)
# in python every object is created using a class which is a blueprint for creating object of that type

# class: blueprint for creating new objects
# objects : instance of a class
# class = humans as example
# objects = azhar , ajju etc


class Point:
    # magic method called constructor __init__
    # The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
    # All classes have a function called __init__(), which is always executed when the class is being initiated.

    # class level attribute
    # this attribute ll shared accross all instance of a class , if we change it it ll be visible to all
    default_color = "red"  # this is class lvl attribute

# x and y are instance attribute , that belong to point object
    def __init__(self, x, y):
        self.x = x  # instance attribute
        self.y = y

# because of self we able to access variable
    def draw(self):
        return (f'Point ({self.x}),({self.y})')


# print(type(points))  class __main__ Point main is our module

# "isinstance" we wanna know if this object is an instance of a given class # either true or flase
"""print(isinstance(points, Point))"""

'''constructor'''
points = Point(1, 2)

# print(points.x) because of self we able to access this attribute
# points.draw()

'''class vs instance attribute'''

points.draw()

another = Point(3, 4)
another.draw()

# for example if its a human class so class attribute should be like eye = 2 which is applied to every one
# print(points.default_color)
# print(Point.default_color)

Point.default_color = "yellow"

'''class vs instance method '''


class Points:

    # both function we define is instance method
    def __init__(self, x, y):
        self.x = x
        self.y = y

# decorator its a way to extend a behavior of a method or a function
    @classmethod
    def zero(cls):
        # same as Points(0,0) difference is when we call zero method python interpreter automatically pass reference to the point calss to zero method
        return cls(0, 0)

    def draw(self):
        print(f'Points ({self.x},({self.y}))')


pointzz = Points.zero()

# so we call them instance of the object class or a object pointzz

# pointzz.draw() we get answer 0,0

'''magic method'''

# its start with __ at the begining and at the end and they called it automatically


class Default:
    def __init__(self, x, z):
        self.x = x
        self.z = z

    def __str__(self):
        return f'({self.x}, {self.z})'

    def draw(self):
        print(f'Points {self.z} and {self.x}')

    def __eq__(self, point2):
        return self.x == point2.x and self.z == point2.z

    def __gt__(self, point2):
        return self.x > point2.x and self.z > point2.z


point1 = Default(1, 2)

# withour str magic method if next line execute its shows you something like  <__main__.Point object at 0x000001CE2F18E8E0>
# print(point1)

'''comparing objects'''

point2 = Default(0, 1)

# its gives you false reason by default equality operator compare the address of those 2 objects
"""print(point1 == point2)"""
#  to solve this again we need to access some magic method name __eq__

# lets compare point object greater than
# print(point1 > point2)


'''experimenting with the code'''

# some JSON:
x = '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
# print(y["age"])
# print(y) same as dump method which is shown below


# a Python object (dict):
x = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:

# print(json.dumps(x))

z = json.dumps(x, indent=4, separators=(' .', ' = '), sort_keys=True)


'''performing arirthmetic operation '''


class Azhar:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return(self.x + other.x, self.y + other.y)


'''optional'''
# def __str__(self):
#     return(self.x + other.x, self.y + other.y)


ajju = Azhar(10, 20)
other = Azhar(20, 30)

'''making custom'''


class TagCloud:
    def __init__(self):
        # instead of tags we using __tags to make
        self.__tags = {}

    def add(self, tag):
        # buttom line if
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), "none")

    # where tag = key and count = value
    def __setitem__(self, tag, count):
        self.__tags[tag.lower()] = count

    def __len__(self):
        return len(self.__tags)

    def __iter__(self):
        return iter(self.__tags)
# when varibale followed by __ then this ll be private memeber


cloud = TagCloud()
cloud.add("python")
cloud.add("azhar")
cloud.add("jaba")
cloud.add("self")
cloud.add("python")

# private member need to hide
# print(cloud.tags["azh"]) error
# print(cloud.__tags) our dic goes private (but its still accessible its just a warning not to touch these files or dict)

'''how to a access private dic'''
# print(cloud._TagCloud__tags)
# print(cloud.__dict__)

'''properties'''

# wanna control over attribute in a class


class Products:
    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price

    def set_price(self, value):
        if value < 0:
            raise ValueError("price should not be negative")
        self.__price = value

# we r not calling the function only referencing the fn it ll only read the value of that function
    price = property(get_price, set_price)


# product = Products(-50) lets say we dont want our price to be negative
'''first let make attribute to be private and then create a instance method to handle it like set price fn'''

# above code is ugly and make this code in a pythonic way we call it properties
# properties is an object that sits infront of an attribute and allows us to get or set the value

product = Products(10)  # use negative value here
# print(product.price)

# remote with less button with more operation is better than single button with single operation
# similary more fn in a code with is no good so we go for decorator

# same result as above we have explicity called property fn to create a property object
# we achive same result by property decorator


class Pordctss:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("price should not be negative")
        self.__price = value


pro = Pordctss(10)
# pro.price = 20 # updating value if we del setter instance or fun update ll not longer work
# print(pro.price)


'''inheritance '''


class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print('eat')


# Animal: parent base
# mammal : child sub

class Mammal(Animal):
    def walk(self):
        print('walk')


class Fish(Animal):
    def swim(self):
        print('swim')

# not only we inherit the calss but also iherit the class attribute


# we can excess class attribute to
'''the object class'''

m = Mammal()
(isinstance(m, Animal))
# to show is this object is insatance of given class or not

'''this animal class inherits from another class called objects that is a base class even we didnt pass
so every class that we have in python directly or indirectly derives from the object class'''

# this ll be true
(isinstance(m, object))

'''method over riding'''


class Animal1:
    def __init__(self):
        print('animal constructor')
        self.age = 1

    def eat(self):
        print("eat")


class Mammal1(Animal1):
    def __init__(self):
        print('method constructor')
        self.weight = 2
        super().__init__()  # move this line below def of mammal1 and check result

    def walk(self):
        print('walk')


# e = Mammal1()

'''you see attribute error reason behind is constructor that define in animal class not executed 
the constructor that was define in mammal class replaced the constructor in the base class'''
# this is what we method over riding
# print(m.age)
# print(m.weight)

# so we ll use super function to get access to the super or base class  which is this case is animal class
'''
(e.age)
(e.weight)'''

# so method overiding means replacing or extending a method define a base class without super() mammal iniit ll replace animal constructor

'''multiple inheritance'''


class Janwar:
    def eat(self):
        print('eat')


class Bird(Janwar):
    def fly(self):
        print('fly')


class Chiken(Bird):
    pass

# multiple inheritance


class Employee:
    def greet(self):
        print('welcome employee')


class Person:
    def greet(self):
        print('welcome perosn')


class Manager(Employee, Person):
    pass
# we have a problem order of the inherit class matters
# so in this case this is bad thing when we dont use inheritance properly
# its stupid to use 2 instance with same name

# manager = Manager()
# manager.greet()


'''good example of inheritance'''


class UserInvalidOperation(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            return UserInvalidOperation("stream is already opened")
        self.opened = True
        return self.opened

    def close(self):
        if not self.opened:
            return UserInvalidOperation("stream already closed")
        self.opened = False
        return self.opened

    @abstractmethod
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("reading data from file")


class NetworkStream(Stream):
    def read(self):
        print("reading data from Network")


stream = FileStream()
# print(stream.close())  working
# print(stream.open()) not working because its an abstract base class concept what kind of stream we r dealing here
# print(stream.open())
# print(stream.open())
# print(stream.close())
# print(stream.close())


# this is abstract base classs
'''polymorphism'''


class UIControl(ABC):

    @abstractmethod
    def draw(self):
        pass
# this draw method ll have derivative in all those classes which are inherit from UIControl base class


class TextBox(UIControl):
    def draw(self):
        print("Textbox")


class DropDownList(UIControl):
    def draw(self):
        print("Dropdownlist")

# so here is what we expect UIControl object


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
# so we pass ddl which is drop down list to draw (we can pass uicontrol derivative (which is text box and dropdownlist) to uicontrl object )
tb = TextBox()
# draw([ddl, tb])

# poly morphism means many form here our draw method is taking many form
