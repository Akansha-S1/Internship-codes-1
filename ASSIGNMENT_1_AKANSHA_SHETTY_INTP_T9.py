#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#NAME: AKANSHA SHETTY  USN: 22BTRAD002  COURSE: AI/DE  SECTION: A
#DATE: 29/02/2024 : 1PM TO 4PM


# ## 1) Python Program for factorial of a number:

# In[6]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

number = int(input("Enter a number: "))
print("Factorial of", number, "is:", factorial(number))


# ## 3.1) Python Program for simple interest 
# ## 3.2) Python Program for compound interest

# ### 3.1) Python Program for simple interest :
# ### FORMULA FOR SIMPLE INTEREST:  [(Principal x rate x time) / 100 ]

# In[7]:


def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (in years): "))

interest = simple_interest(principal, rate, time)
print("Simple Interest:", interest)


# ### 3.2) Python Program for compound interest
# ### FORMULA FOR COMPOUND INTEREST: 

# In[32]:


def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    ci = amount - principal
    return ci

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (%): "))
time = float(input("Enter the time period (in years): "))

interest = compound_interest(principal, rate, time)
print("Compound Interest:", interest)


# ## 4)  Python Program to check Armstrong Number:

# ### WHAT IS AN ARMSTRONG NUMBER: a number that is equal to the sum of cubes of its digits.

# ### Use case 1: is an armstrong number:

# In[13]:


def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrongSum = sum(int(digit) ** num_digits for digit in num_str)
    return num == armstrongSum

num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# ### Use case 2: is NOT an armstrong number:

# In[15]:


def is_armstrong_number(num):
    num_str = str(num)
    num_digits = len(num_str)
    armstrongSum = sum(int(digit) ** num_digits for digit in num_str)
    return num == armstrongSum

num = int(input("Enter a number: "))
if is_armstrong_number(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")


# ## 5) Python Program for Program to find area of a circle

# ### Formula to find the area of a circle: 2 x radius x pi   

# In[18]:


import math

def area_of_circle(radius):
    return math.pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print("The area of the circle is:", area)


# ## 6) Python program to print all Prime numbers in an Interval

# In[29]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

lower = int(input("Enter the lower bound of the interval: "))
upper = int(input("Enter the upper bound of the interval: "))

print("Prime numbers between", lower, "and", upper, "are:")
for number in range(lower, upper + 1):
    if is_prime(number):
        print(number)


# ## 7) Python program to check whether a number is Prime or not

# ### Use case 1: IS A PRIME NUMBER:

# In[19]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# ### Use case 2: IS NOT A PRIME NUMBER:

# In[27]:


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

number = int(input("Enter a number: "))

if is_prime(number):
    print(number, "is a prime number")
else:
    print(number, "is not a prime number")


# ## 8) Python Program for n-th Fibonacci number

# In[24]:


def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n):
            a, b = b, a + b
        return b

n = int(input("Enter the value of n: "))
print("The", n, "th Fibonacci number is:", fibonacci(n))

