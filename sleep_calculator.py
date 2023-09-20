print("Welcome to Calculator\n")

#to input something
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
user_hos = int(input("Please enter your hours of sleep...\n"))

print("Thank you for your input\n")
print("The name that you entered is ", user_name)
print("Your age in years is ", 2023 - user_yob)

#To count how many hours sleep
print("The number of hours the user has slept in total is ", ((2023 - user_yob)*user_hos) )

