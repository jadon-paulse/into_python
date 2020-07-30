#Calculating value of pi
import math

#user input for the radius
radius = float(input("Enter radius: "))

a = 2*(2/math.sqrt(2))
b = math.sqrt(2)
pi = a

#While loop is used too approximate pi
while 2 / math.sqrt(2 + b) > 1:
    pi = pi * 2 / math.sqrt(2 + b)
    b = math.sqrt(2 + b)

#Calculating the area of the circle
area = (pi * radius ** 2)
print("Approximation of pi: ", round(pi, 3))
print("Area is", round(area, 3))

