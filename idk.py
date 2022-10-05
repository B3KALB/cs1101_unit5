import math

input_x = int(input('What is x: '))
a = 4
def my_sqrt(a, x):
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
        return x

print(my_sqrt(a, input_x))

def test_sqrt():
    count = 0
    x = 1
    
    while (count < 25):
        count = count + 1
        a = count
        # print(f"a: {a}")
        y = (x + a/x) / 2.0
        # print(f"y: {y}")
        if count == 26:
           break
        x = y 
        # print(f"x: {x}")
        
        py_math = math.sqrt(a)
        # print(f"py_math: {py_math}")
        
        diff =  x - py_math
        # print(f"diff: {diff}")
          
        print(f"a = {a} | my_sqrt(a) = {x} | math.sqrt(a) = {py_math} | diff = {diff}")
 
            
test_sqrt()

import math
# Part 1

# Encapsulate the following Python code from Section 7.5 in a function named my_sqrt
#  that takes a as a parameter, chooses a starting value for x, and returns an estimate of the square root of a. 

# Part 1
print('part 1 ')
print(" ")

x = 3
a = 4
def my_sqrt(a, x):
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
        
        return abs(x)

print(my_sqrt(a, x))

print("________________________")
print(" ")

# part 2
print('part 2 ')
print(" ")
def my_sqrt_abs(a, x):
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
        
    return abs(x)
def test_sqrt():
    
    count = 1
   
    while count <= 25:
        
        print('a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {} '.format(count, my_sqrt_abs(count,1), math.sqrt(count), abs(my_sqrt_abs(count,1)-math.sqrt(count))))
        
        count = count + 1
 
test_sqrt()

# 6th try
import math
# Part 1

# Encapsulate the following Python code from Section 7.5 in a function named my_sqrt
#  that takes a as a parameter, chooses a starting value for x, and returns an estimate of the square root of a. 

# Part 1
print('part 1 ')
print(" ")

def my_sqrt(a, x):
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
        
        return abs(x)

print(my_sqrt(4, 3))

print("________________________")
print(" ")

# part 2
print('part 2 ')
print(" ")
def my_sqrt_abs(a, x):
    while True:
        y = (x + a/x) / 2.0
        if y == x:
            break
        x = y
        
    return abs(x)
def test_sqrt(num):
    
    count = 1
   
    while count < (num + 1):
        
        print('a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {} '.format(count, my_sqrt_abs(count,1), math.sqrt(count), abs(my_sqrt_abs(count,1)-math.sqrt(count))))
        
        count = count + 1
 
test_sqrt(25)