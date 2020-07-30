
month = input("Enter the month: ")
day = input("Enter the starting day: ")

# day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# month_list = ["January", "February", "March", "April", "May", "June", "July", "August",
#               "September", "October", "November", "December" ]


# Get the number of days in the months
if month in ["April", "June", "September", "November"]:
    x = 30
elif month in ["February"]:
    x = 28
else:
    x = 31

# Get the number of "blank spaces" we need to skip for the first week, and when to break
blank_space = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
space = blank_space.index(day)

print("-----------------")
print(month)
print("Mo Tu We Th Fr Sa Su")
# Print empty "cells" when the first day starts after Monday
for i in range(space):
    print("  ", end=' ')
# Print days of the month
for i in range(x):
    print("%2d" % (i + 1), end=' ')
    # If we just printed the last day of the week, print a newline
    if (i + space) % 7 == 6: print()