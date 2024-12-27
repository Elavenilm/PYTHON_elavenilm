# Built-in Functions:

# abs():                                               #Output: 53
x = -53
print("absolute value of integer is : ",abs(x))


# all():                                               #Output: False
print(all([True,False,True,False]))


# any():                                               #Output: True
x = [False,False,True,False,False]
print(any(x))


# ascii():                                             #Output: '\xa5'
print(ascii("¥"))


# bin():                                               #Output: 0b100011
x = bin(35)
print(x)


# bool():
x = bool(0)                                            #Output: False
print(x)
y = bool(1)                                            #Output: True
print(y)
z = bool()                                             #Output: False       
print(z)


# len():                                               #Output: 18
x = "python programming"
length = len(x)
print(length)


# max():                                               #Output: 9
A = 3
B = 6
C = 9
max_value = max(A,B,C)
print(max_value)


# min():                                               #Output: 3
A = 3
B = 6
C = 9
min_value = min(A,B,C)
print(min_value)


# pow():                                               #Output: 36
print(pow(6,2))


# print():  
print("hello,world!!!")                                #Output: hello,world!!!
x = ("python")                                         #Output: python
print(x)


# round():                                             #Output: 36
number = 35.53
round_num = round(number)
print(round_num)


# bytearray():                                         #Output: bytearray(b'hello')
x = bytearray("hello","utf-8")
print(x)


# recursive():                                         #Output: Factorial of 10 is 3628800
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
number = 10
print("Factorial of", number, "is", factorial(number))


# lambda():                                            #Output: Sum of 15 and 5: 20
add = lambda x, y: x + y
print("Sum of 15 and 5:", add(15, 5))


# Conversion and Formatting with Concatenation

# String Concatenation                                 #Output: Hello, World!
string6 = "Hello"
string7 = "World!"
concatenated_string = string6 + ", " + string7
print("Concatenated String:", concatenated_string)  

# str.capitalize()                                     #Output: Hello, world!
string1 = "hello, world!"
print("capitalize():", string1.capitalize())  

# str.lower()                                          #Output: hello, world!
string2 = "HELLO, WORLD!"
print("lower():", string2.lower())  

# str.upper()                                          #Output: HELLO, WORLD!
string3 = "hello, world!"
print("upper():", string3.upper())  

# str.title()                                          #Output: Hello, World!
string4 = "hello, world!"
print("title():", string4.title())  

# str.swapcase()                                       #Output: hELLO, wORLD!
string5 = "Hello, World!"
print("swapcase():", string5.swapcase())  

# str.format()                                         #Output: My name is Alice and I am 30 years old.
name = "Alice"
age = 30
print("My name is {} and I am {} years old.".format(name, age))  


# math():
import math                                                     #Output:                          
print("Square root of 16:", math.sqrt(16))                      # Square root of 16: 4.0
print("2 raised to the power of 3:", math.pow(2, 3))            # 2 raised to the power of 3: 8.0
print("Exponential value of 2:", math.exp(2))                   # Exponential value of 2: 7.38905609893065
print("Natural logarithm of 10:", math.log(10))                 # Natural logarithm of 10: 2.302585092994046
print("Ceiling of 3.14:", math.ceil(3.14))                      # Ceiling of 3.14: 4
print("Floor of 3.14:", math.floor(3.14))                       # Floor of 3.14: 3
print("Truncated value of 3.14:", math.trunc(3.14))             # Truncated value of 3.14: 3
print("Factorial of 5:", math.factorial(5))                     # Factorial of 5: 120 


# arbitary():                                                   #Output: total :  275
def arun(*args):                                                #        average :  55.0        
    total = sum(args)
    print("total : ",total)
    average = total/len(args)
    return average
print("average : ",arun(35,45,55,65,75))


# random():
import random
random_number = random.randint(1,10)                            #Output: random number :  9
print("random number : ",random_number)
random_float = random.random()                                  #        random float :  0.7953037515387081
print("random float : ",random_float)