import math
# Program for calculating the area of a triangle
a = int(input("Enter the length of the first side: "))
b = int(input("Enter the length of the seconod side: "))
c = int(input("Enter the length of the third side: "))
#Program uses Heron's formula to calculate user inputs
s = (a + b + c) / 2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
#Prints out the result
print("The area of the traingle with sides of length", a, 'and', b,'and', c, 'is', area)
