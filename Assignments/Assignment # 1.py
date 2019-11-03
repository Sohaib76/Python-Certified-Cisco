'''1. Write a Python program to print the following string in a specific format
(see the output).

Twinkle, twinkle, little star,
How I wonder what you are!
Up above the world so high,
Like a diamond in the sky.

Twinkle, twinkle, little star,
How I wonder what you are'''
print('''Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high,
 \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!''')


print("----------------------------------------------------------")

'''2. Write a Python program to get the Python version you are using'''
import sys
print("Python version")
print (sys.version)


print("----------------------------------------------------------")

'''3. Write a Python program to display the current date and time.'''
import datetime
now = datetime.datetime.now()
print ("Current date and time is : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))

print("----------------------------------------------------------")


'''4. Write a Python program which accepts the radius of a circle from the user
and compute the area.'''
from math import pi
r = float(input ("Input the radius of the circle : "))
print ("The area of the circle is: " + str(pi * r**2))


print("----------------------------------------------------------")



'''5. Write a Python program which accepts the user's first and last name and
print them in reverse order with a space between them.'''
fname = input("Input your First Name : ")
lname = input("Input your Last Name : ")
print (lname + " " + fname)



print("----------------------------------------------------------")
'''6. Write a python program which takes two inputs from user and print them
addition'''
num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))