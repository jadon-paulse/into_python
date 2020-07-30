import re
#Enter the starting number
n = int(input("Enter the start number: "))

# print("%-2d%2d" % (current_num, current_num), end = " ")

#For loop gets the next 7 numbers starting from n
for current_num in range(n, n + 7):
    if -6 < n < 93:
        #Prints numbers next to each other
        print(current_num, end = " ")
    else:
        print("Invalid number!")
        break