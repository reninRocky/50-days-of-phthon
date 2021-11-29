###                                  """ DAY_11 """

# Day 11 of 50 Days of Python 
# Monday, 22-11-2021
'''
1. Sets-Contd...
2. Dictionary
3. Mini Exercise!!
4. Assignment
'''




#####################################################################3
    #INTRO to SETS: Used to store many items in a single variable
#How do I create a set?

'''fruits = {"Apples", "Mangoes", "Almonds"}
print(fruits)
fruits.clear()
print(fruits)

# Using Union()

names = {"Anjali", "Amith","Ananya", "Renin"}
age ={19, 20, 18, 19}

#setBoth = names.union(age)
#print(setBoth)
#Uisng update()

names.update(age)
print(names)

## Use of intersection_update()

company1 = {"Facebook", "Apple", "Amazon"}
company2 = {"Amazon","Netflix", "Google"}
company1.intersection_update(company2)
print(company1)'''


 # DICTIONARY


##### Extended Example On Dictionary  #####
 
#A dictionary is a more general version of a
#list. Here is a list that contains the
#number of days in the months of the year:
#day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#Here is a dictionary of the days in the months of the year:
#days = {'January':31, 'February':28, 'March':31, 'April':30,
#            'May':31, 'June':30, 'July':31, 'August':31,
#                'September':30, 'October':31, 'November':30, 'December':31}

'''
diwali = {"Ram" : "A Hindu God that has mysterious powers",
          "Sita" : "The Goddess of Himalayas",
          "Bahuballi": "The strongest God"}
word = input("Enter any word related to Diwali like Ram/Sita" )
print("The definition is: ", diwali[word])
'''

######### MINI EXERCISE   ############

# Can you count how frequent certain words appear in a text?

from string import punctuation

#i. read from file, remove caps and punctuation, and split into words

text = open('bahuballi.txt').read()

text = text.lower()
for p in punctuation:
    text = text.replace(p, '')
words = text.split()

#ii. build the dictionary of frequencies

d = {}
for w in words:
    if w in d:
        d[w] = d[w] + 1
    else:
        d[w] = 1
        
#iii. print in alphabetical order
        
items = list(d.items())
items.sort()
for i in items:
    print(i)
    
#iv. print in order from least to most common
    
items = list(d.items())
items = [(i[1], i[0]) for i in items]
items.sort()
for i in items:
    print(i)

####### ASSIGNMENT ###########
    
For this problem, use the dictionary from
the beginning of this chapter whose keys are
month names and whose values are the number
of days in the corresponding months.

(a) Ask the user to enter a month name and use the dictionary to tell them how many days
are in the month.
(b) Print out all of the keys in alphabetical order.
(c) Print out all of the months with 31 days.
(d) Print out the (key-value) pairs sorted by the number of days in each month
(e) Modify the program from part (a) and the dictionary so that the user does not have to
know how to spell the month name exactly. That is, all they have to do is spell the first
three letters of the month name correctly.'''
'''

# Can we design a Scrabble Game

word = input("Enter a word")
points = {'A':1, 'K':8, 'X':8, 'Z':10}
score = sum([points[c] for c in word])
print(score)'''




###                                  """ DAY_12 """

# Day 12 of 50 Days of Python 
# Tuesday, 23-11-2021
'''
1. Reading from files 
2. Writing to Files
3. Examples (Wrt files)
4. Functions
5. Function Arguments
6. Examples (Wrt Functions)
7. Assignment
'''


''' ########## TEXT FILES #########

#Eg. 1: Reading text files

#line =  [line.strip() for line in open('eg1.txt')]
# Try this# line2 = open('eg1.txt').read()

#Eg. 2: Writing to files

f1 = open('writefile.txt', 'w')
print('Okay,  I know nothing about it.', file=f1)
print('And I mean the same thing.', file=f1)
f1.close()
line =  [line.strip() for line in open('writefile.txt')]

#Eg. 3: Let's say you have results of NBA Players viz

#11/23/2021, Robert Morris, 61, Mount St. Mary's, 63

lines = [line.strip() for line in open('scores.txt')]
games = [line.split(',') for line in lines]
print(max([abs(int(g[2])-int(g[4])) for g in games]))
lines = [line.strip() for line in open('scores.txt')]
games = [line.split(',') for line in lines]
biggest_diff = 0

for g in games:
    diff = abs(int(g[2])-int(g[4]))
    if diff>biggest_diff:
        biggest_diff = diff
        game_info = g
print(game_info)
print(diff)'''

##### WORDPLAY ########

#Eg4: Print all 3 letters

'''
wordlist = [line.strip() for line in open('wordlist2.txt')]
for word in wordlist:
    if len(word)==3:
        print(word)'''

#try print([word for word in wordlist if len(word)==6])
'''
wordlist = [line.strip() for line in open('wordlist2.txt')]
#Eg 5: Starts with ac vs AC or da vs DA
for word in wordlist:
    if word[:2]=='ac' or word[:2]=='da':
        print(word)
wordlist = [line.strip() for line in open('wordlist2.txt')]
#Eg 5: Starts with ac and ends with tor #actuator
for word in wordlist:
    if word[:2]=='ac' or word[:3]=='tor':
        print(word)'''


#Eg 6: Determine what %age starts with a vowel

def calci():
    wordlist = [line.strip() for line in open('wordlist2.txt')]
    count = 0
    for word in wordlist:
        if word[0] in 'aeiou':
            count=count+1

    print(100*count/len(wordlist))
calci()

###                                  """ DAY_13 """

# Day 13 of 50 Days of Python 
# Wednesday, 24-11-2021

'''
1. Functions
        Creating & Calling
2. Function Arguments vs Parameters
        Arbitrary Arguments
3. The Pass Statement
4. Recursion
5. Lambda Function
6. Examples (Wrt Lambda Functions)
7. Assignment
'''
#1. Creating a Function

#2. Calling a Function

'''
#3. Arguments

def say_Hello():
    print("Hello, Mysuru")
say_Hello()

def my_func(fname):
    print(fname + ",is my Friend")
my_func("Dhanush")
my_func("Mahesh")
my_func("Varsha")

#4. Parameters vs Arguments

def my_func2(fname, lname):
    print(fname + " " + lname)
my_func2("Akash", "Mahesh")

#5. Arbitrary Arguments, *args

def my_dish(*food):
  print("My favourite dish is " + food[1])
my_dish("Masala poori", "Biryani", "Idli")

#6. Keyword Arguments (using key = value pair)

def my_dish(f3,f2,f1):
  print("My favourite dish is " + f2)
my_dish(f1="Masala poori", f2="Biryani", f3="Idli")

#7. Arbitrary Keyword Arguments, **kwargs

def my_dish(**food):
  print("My favourite dish is " + food["f1"])
my_dish(f1="Masala poori", f2="Biryani", f3="Idli")

#8. Default Parameter Value

def my_country(country = "Nigeria"):
    print("I am from " +country)
my_country("Jamaica")
my_country("India")
my_country()
my_country("South Africa")

#9. Passing sequences as an argument

def my_function(fruits):
    for x in fruits:
        print(x)
fruits = ["Apples", "Bananas", "Mangoes"]
my_function(fruits)

#10. Can we return values
#11. Use of Pass Statement

def myPassStmt():
    pass
########  LAMBDA FUNCTIONS ##########

#12. Use of Lambda Expessions

ex = lambda a : a + 10
print(ex(15))

#13. Using two arguments

x = lambda a, b : a * b
print(x(4, 5))'''

#14. Using lambda to double a number

def myfunc(n):
    return lambda a : a * n
my_double = myfunc(2)
print(my_double(11))'''

'''def my_func(fname):
    print(fname + ",is my Friend")
    
my_func("Samarth")
my_func("Amar")
my_func("Anjali")
my_func("Deeksha")
my_func("Niharika")
def my_func(fname):
    print("Wecome " +fname + ",is my Friend")
    
my_func("Samarth")
my_func("Amar")
my_func("Anjali")
my_func("Deeksha")
my_func("Niharika")
def my_func2(fname, lname):
    print(fname + " " + lname)
my_func2("Akash", "Mahesh")
my_func2("Ananya", "Prakash")
my_func2("Anjali", "Hemanth")
#5. Arbitrary Arguments, *args
def my_dish(*food):
  print("My favourite dish is " + food[1])
my_dish("Masala poori", "Biryani", "Idli")
#6. Keyword Arguments (using key = value pair)
def my_dish(f3,f2,f1):
  print("My favourite dish is " + f3)
my_dish(f1="Masala poori", f2="Biryani", f3="Idli")
#7. Arbitrary Keyword Arguments, **kwargs
def my_dish(**food):
  print("My favourite dish is " + food["f1"])
my_dish(f1="Masala poori", f2="Biryani", f3="Idli")
#8. Default Parameter Value
def my_country(country = "Nigeria"):
    print("I am from " +country)
my_country("Jamaica")
my_country("India")
#my_country()
my_country("South Africa")
my_country()
#9. Passing sequences as an argument
def my_function(fruits):
    for x in fruits:
        print(x)
fruits = ["Apples", "Bananas", "Mangoes"]
my_function(fruits)
#10. Can we return values
def multiply(x):
    return 10 * x
print(multiply(1))
print(multiply(11))
print(multiply(111))
print(multiply(1111))
print(multiply(11111))
print(multiply(111111))
def myfunc():
    pass
#12. Use of Lambda Expessions
ex = lambda a : a + 10
print(ex(15))
#13. Using two arguments
x = lambda a, b : a % b
print(x(5, 4))'''

def myfunc(n):
    return lambda a : a * n
my_double = myfunc(2)
my_tripple = myfunc(3)
my_fourth = myfunc(4)

print(my_double(11))
print(my_tripple(11))
print(my_fourth(11))


###                                  """ DAY_14 """

# Day 14 of 50 Days of Python 
# Thursday, 25-11-2021

'''
1. Recursion
2. Functions - Mini Projects 
3. Exception Handling
4. Assignment
'''
'''
#1. Checking Recursion Limit
def countdown(n):
    print(n)
    if n==0:
        return
    else:
        countdown(n-1)
countdown(5)'''
setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
        """
from timeit import timeit
print(timeit("factorial(4)", setup=setup_string, number=1000))

'''
1. What is Python Recursion
2. 
'''

'''#Eg. 1: Example of a recursive function
def factorial(x):
    """This is a recursive function
    to find the factorial of a number"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))
num = 5
print("The factorial of", num, "is", factorial(num))

#Eg. 2: Testing the maximum depth of Recursion
def recurse():
    recurse()
recurse()

#Eg. 3: Another case of max recursion exceeded
def function():
    x = 10
    function()
    
#Eg. 4: Checking Recursion Limit
from sys import getrecursionlimit
getrecursionlimit()

#Eg. 5: You can change it, too, with setrecursionlimit():

from sys import getrecursionlimit,setrecursionlimit
setrecursionlimit(2000)
getrecursionlimit()

#Eg. 6: Count down program

def countdown(n):
    print(n)
    if n == 0:
        return             # Terminates recursion
    else:
        countdown(n - 1)   # Recursive call
        
print(countdown(5))

#Eg. 7: Some more concise ways

def countdown(n):
    print(n)
    if n > 0:
        countdown(n - 1)
# Or using non-recursive ways for comparison
def countdown(n):
    while n >= 0:
         print(n)
         n -= 1
countdown(5)

#Eg. 8: Calculate Factorial of a number

def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
factorial(10)

#Eg 9: Use print() to make it readable

def factorial(n):
    print(f"factorial() called with n = {n}")
    return_value = 1 if n <= 1 else n * factorial(n -1)
    print(f"-> factorial({n}) returns {return_value}")
    return return_value
print(factorial(4))

#Eg. 10: Recursion using For loop

def factorial(n):
     return_value = 1
     for i in range(2, n + 1):
        return_value *= i
     return return_value
factorial(5)

#Eg. 11: Recursion using reduce & lambda functions
from functools import reduce

def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
factorial(4)
######### Speed / Execution Time Comparison ######
#Eg 12:

from timeit import timeit
print(timeit("print(string)", setup="string='Hello'", number=100))
#Eg 13: Using Recursive Call
setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
    """
from timeit import timeit
print(timeit("factorial(4)", setup=setup_string, number=100))'''

#Eg 13: Using Iterative Implementation

setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
        """
from timeit import timeit
print(timeit("factorial(4)", setup=setup_string, number=1000))

'''
#Eg 14: Hey, factorial is available in math module
from math import factorial
print(factorial(6))'''

