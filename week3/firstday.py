
#User inputs first and second year
year1 = int(input("Enter first year: "))
year2 = int(input("Enter second year: "))

#Finds R
def R(n, m):
    return n % m
#first_month calculates the day
def first_month(year):
    a = 1 + 5 * R(year - 1, 4)
    b = 4 * R(year - 1, 100)
    c = 6 * R(year - 1, 400)
    day = R(a + b + c, 7)
    return day

week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

#For loop uses the 2 years as a range and prints out each year and the day
for year in range(year1, year2):
    year += 1
    day = week[(first_month(year))]
    print("The first of January ", year, "falls on" , day)