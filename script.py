import math
# Part 1
 
# Encapsulate the following Python code from Section 7.5 in a function named my_sqrt
#  that takes a as a parameter, chooses a starting value for x,
# and returns an estimate of the square root of a.
 
print('part 1 ') #decorative
print(" ") #decorative
 
def my_sqrt(a, x): # This encapsulates our loop and lets us add the arguments
   while True: # Our while loop that runs until not True
       y = (x + a/x) / 2.0 # Our given formula for finding square root
       if y == x: # an if statement saying when y and x are equal, break
           break # causes the loop to stop and do the next instruction
       x = y # when y is found, re assign it as variable x
      
       return abs(x) # return our absolute value of x which represents our square root
 
print(my_sqrt(4, 3)) #when calling our function and passing our two values in a print
# statement will return a value, the print statement displays that value
 
print("________________________") #decorative
print(" ") #decorative
 
# Part 2
 
# Write a function named test_sqrt that prints a table like the following using a while loop, where "diff" is the absolute value of the difference between my_sqrt(a) and math.sqrt(a).
 
# a = 1 | my_sqrt(a) = 1 | math.sqrt(a) = 1.0 | diff = 0.0
# a = 2 | my_sqrt(a) = 1.41421356237 | math.sqrt(a) = 1.41421356237 | diff = 2.22044604925e-16
# a = 3 | my_sqrt(a) = 1.73205080757 | math.sqrt(a) = 1.73205080757 | diff = 0.0
# a = 4 | my_sqrt(a) = 2.0 | math.sqrt(a) = 2.0 | diff = 0.0
# a = 5 | my_sqrt(a) = 2.2360679775 | math.sqrt(a) = 2.2360679775 | diff = 0.0
# a = 6 | my_sqrt(a) = 2.44948974278 | math.sqrt(a) = 2.44948974278 | diff = 0.0
# a = 7 | my_sqrt(a) = 2.64575131106 | math.sqrt(a) = 2.64575131106 | diff = 0.0
# a = 8 | my_sqrt(a) = 2.82842712475 | math.sqrt(a) = 2.82842712475 | diff = 4.4408920985e-16
# a = 9 | my_sqrt(a) = 3.0 | math.sqrt(a) = 3.0 | diff = 0.0
 
# Modify your program so that it outputs lines for values from 1 to 25 instead of just 1 to 9.
 
# You should submit a script file and a plain text output file (.txt) that contains the test output. Multiple file uploads are permitted.
 
print('part 2 ') #decorative
print(" ") #decorative
def my_sqrt_abs(a, x): # Same loop as before but the return is in a different scope
   while True: # Our while loop that runs until not True
       y = (x + a/x) / 2.0 # Our given formula for finding square root
       if y == x: # An if statement saying when y and x are equal, break
           break # Causes the loop to stop and do the next instruction
       x = y # When y is found, re assign it as variable x
      
   return abs(x)  # return our absolute value of x which represents our square root
 
def test_sqrt(num): #
  
   count = 1 #
 
   while count < (num + 1): #
     
       print('a = {} | my_sqrt(a) = {} | math.sqrt(a) = {} | diff = {} '.format(count, my_sqrt_abs(count,1), math.sqrt(count), abs(my_sqrt_abs(count,1)-math.sqrt(count))))
   # print statement that houses a string with places for our values between the ''
   # from .format beyond we inject our aligning values with their corresponding index
   # count, the count variable
   # my_sqrt_abs(count,1),function call with our two arguments passed in
   # math.sqrt(count), part of the math we imported at the top with argument passed in
   # abs(my_sqrt_abs(count,1)-math.sqrt(count)), absolute value of the difference in our
   # square root while loop with two arguments and our python math with one argument 
 
       count = count + 1 # this updates out count variable so it isn't an infinite loop
test_sqrt(25) # this calls our function with the number wae want to represent the end of our range
 
# This took me no less than 10 tries.

# references :
# https://www.w3schools.com/python/ref_math_sqrt.asp 
# https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756
# https://www.geeksforgeeks.org/loops-in-python/
# https://www.geeksforgeeks.org/assign-function-to-a-variable-in-python/
# https://www.adamsmith.haus/python/answers/how-to-print-a-number-in-scientific-notation-in-python#:~:text=Use%20str.&text=format()%20on%20a%20number,the%20number%20in%20scientific%20notation.&text=To%20only%20include%20a%20certain,the%20desired%20number%20of%20digits.
# https://docs.python.org/3/tutorial/inputoutput.html
