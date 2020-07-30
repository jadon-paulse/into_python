import calendar

#Checks if the year is a leap year or not
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    else:
        return False

#Gets the number of the month
def month_name(month_number):
    calendar = ["January", "February", "March", "April", "May", "June",
                "July", "August", "September", "October", "November", "December"]
    return calendar[month_number - 1]
    # print(calendar.month_name[number])

#Gets the number of days in a month
def days_in_month(month_number, year):
    is_leap_year(year)
    month_name(month_number)
    days = calendar.monthrange(year, month_number)
    return days


def R(n, m):
    return n % m

#Checks for the first day of the year
def first_day_of_year(year):
    a = 1 + 5 * R(year - 1, 4)
    b = 4 * R(year - 1, 100)
    c = 6 * R(year - 1, 400)
    day = R(a + b + c, 7)
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    day = week[day]
    return week.index(day), day

#Checks for the first day of the month
def first_day_of_month(month, year):
    firstDay = calendar.weekday(year, month, 1)
    return firstDay



# user = int(input("Choose from the following options: \n"
#                  "1. Test is_leap_year() \n"
#                  "2. Test month_name() \n"
#                  "3. Test days_in_month() \n"
#                  "4. Test first_day_of_year() \n"
#                  "5. Test first_day_of_month() \n"
#                  "Enter choice number here: "))
#
#
# if user == 1:
#     year = int(input("Enter year(4 digits): "))
#     is_leap_year(year)
#     if is_leap_year(year) == True:
#         print(year, "is a leap year")
#     else:
#         print(year, "is not a leap year")
# elif user == 2:
#     number = int(input("Enter month number: "))
#     month_name(number)
# elif user == 3:
#     year = int(input("Enter year(4 digits): "))
#     month_number = int(input("Enter month number: "))
#     days_in_month(month_number, year)
# elif user == 4:
#     year = int(input("Enter year(4 digits): "))
#     first_day_of_year(year)
# elif user == 5:
#     year = int(input("Enter year(4 digits): "))
#     month_number = int(input("Enter month number: "))
#     first_day_of_month(month_number, year)
# else:
#     print("Invalid choice")


