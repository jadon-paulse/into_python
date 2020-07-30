#Application for checking the validity of time entered by the user

hours = int(input("Enter the hours: "))
minutes = int(input("Enter the minutes: "))
seconds = int(input("Enter the seconds: "))

#Checks if time entered by user is valid
if 0 <= hours <= 23 and 0 <= minutes <= 59 and 0 <= seconds <= 59:
    print("Your time is valid")
# elif 0 <= minutes and seconds <= 59:
#     print("Your time is valid")
else:
    print("Your time is invalid")