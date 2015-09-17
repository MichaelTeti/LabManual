########################################################
#------------------------------------------------------#
#
# Machine Perception and Cognitive Robotics Laboratory
#
#     Center for Complex Systems and Brain Sciences
#               Florida Atlantic University
#
#------------------------------------------------------#
########################################################
#------------------------------------------------------#
#LabManual
#------------------------------------------------------#
#An Informal Introduction to Python
#The Python Software Foundation
#https://docs.python.org/2/tutorial/introduction.html
#100 numpy exercises
#https://github.com/rougier/numpy-100

#------------------------------------------------------#

print "Hello World!"

# this is the first comment
spam = 1  # and this is the second comment
  # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#------------------------------------------------------#

print 2 + 2
print 50 - 5*6
print (50 - 5.0*6) / 4
print 8 / 5.0
print 17 / 3  # int / int -> int
print 17 / 3.0  # int / float -> float
print 17 // 3.0  # explicit floor division discards the fractional part
print 17 % 3  # the % operator returns the remainder of the division
print 5 * 3 + 2  # result * divisor + remainder
print 5 ** 2  # 5 squared
print 2 ** 7  # 2 to the power of 7

#------------------------------------------------------#

#The equal sign (=) is used to assign a value to a variable. Afterwards, no result is displayed before the next interactive prompt:
width = 20
height = 5 * 9
print width * height


i = 256*256
print 'The value of i is', i


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 100:
	print b
	a, b = b, a+b


#------------------------------------------------------#


#. Import the numpy package under the name np     

import numpy as np


#. Create a null vector of size 10

Z = np.zeros(10)
print(Z)


#. Create a null vector of size 10 but the fifth value which is 1

Z = np.zeros(10)
Z[4] = 1
print(Z)



#. Create a vector with values ranging from 10 to 49

Z = np.arange(10,50)
print(Z)



#. Create a 3x3 matrix with values ranging from 0 to 8

Z = np.arange(9).reshape(3,3)
print(Z)



#. Find indices of non-zero elements from [1,2,0,0,4,0]

nz = np.nonzero([1,2,0,0,4,0])
print(nz)



#. Create a 3x3 identity matrix

Z = np.eye(3)
print(Z)


#. Create a 5x5 matrix with values 1,2,3,4 just below the diagonal

Z = np.diag(1+np.arange(4),k=-1)
print(Z)



#. Create a 3x3x3 array with random values

Z = np.random.random((3,3,3))
print(Z)



#. Create a 8x8 matrix and fill it with a checkerboard pattern

Z = np.zeros((8,8),dtype=int)
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)



#. Create a 10x10 array with random values and find the minimum and maximum values

Z = np.random.random((10,10))
Zmin, Zmax = Z.min(), Z.max()
print(Zmin, Zmax)



#. Create a checkerboard 8x8 matrix using the tile function

Z = np.tile( np.array([[0,1],[1,0]]), (4,4))
print(Z)



#. Normalize a 5x5 random matrix (between 0 and 1)

Z = np.random.random((5,5))
Zmax, Zmin = Z.max(), Z.min()
Z = (Z - Zmin)/(Zmax - Zmin)
print(Z)



#. Multiply a 5x3 matrix by a 3x2 matrix (real matrix product)

Z = np.dot(np.ones((5,3)), np.ones((3,2)))
print(Z)



#. Create a 5x5 matrix with row values ranging from 0 to 4

Z = np.zeros((5,5))
Z += np.arange(5)
print(Z)



#. Create a vector of size 10 with values ranging from 0 to 1, both excluded

Z = np.linspace(0,1,12,endpoint=True)[1:-1]
print(Z)



#. Create a random vector of size 10 and sort it

Z = np.random.random(10)
Z.sort()
print(Z)


#. Consider two random array A anb B, check if they are equal.

A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.allclose(A,B)
print(equal)



#. Create a random vector of size 30 and find the mean value

Z = np.random.random(30)
m = Z.mean()
print(m)     


print 'done'


#------------------------------------------------------------------#

#. A function is a statement(s) that performs an operation. It can be named anything.
#. All functions have the same format. They all begin with the word def, followed by the name of the function and any parameters the function will need when it is executed. 

def remainder(a):	#This function will need to know and use the variable a, so a goes in parentheses. Don't forget the colon after the parentheses.
	if a%5==0:	#The first line after a function must be indented, typically by four spaces. This function is testing "if" something is true, then returning a result based on if it's true or not.
		print("No remainder")

remainder(20)	#There is one more step. For your function to be executed, you have to call it. Just write the name of the function and the parameter in parentheses without indentation. 
		#Notice how you can run specify what number you want to run through the function, the letter "a" takes on the number 20. 




