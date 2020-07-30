
n = int(input("Enter a numbers: "))

# if -6 < n < 2:
#     for x in range(n, 43 - (n < -4)):
#         for y in range(x, x + 6):
#             # for z in range(y + 7, y + 7 + 6):
#             print("{:>2}".format(y), end=" ")
#
#         print()
# def print_grid(n):
if -6 < n < 2:
    for x in range(n, n + 41, 7):
        for j in range(x + 6,  x + 13):
            print("{:>2}".format(j), end=" ")
        print()

# for n in range(-5, 2):
#              print_grid(n)
#              print()
# if -6 < n < 2:
#     for x in range(n, 38 - (n < -4), 6):
#         for j in range(x,  x + 6):
#             print("{:>2}".format(j), end=" ")
#         print()

# if n>-6 and n<2:
#     for x in range(n, 35 + n, 6):
#         for j in range(x, x + 7):
#             print("{:>2}".format(j), end=" ")
#             print()
