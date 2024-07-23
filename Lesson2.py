#1. Decisions at the Crossroad
#Task 1: Code Correction
number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

#2. The Greatest Showdown
#Task 1: Identify the Greatest
num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number: "))
num_3 = int(input("Enter a number: "))

def max_num(num1, num2, num3):
    largest = num1
    
    if num2 > largest:
        largest = num2
    if num3 > largest:
        largest = num3
    
    return largest

#task 2
def min_num(num1, num2, num3):
    smallest = num1
    
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    
    return smallest

result = max_num(num_1, num_2, num_3)
print ("The largest number is: " + str(result))

result = min_num(num_1, num_2, num_3)
print ("The smallest number is: " + str(result))

#3. Leap Year Explorer
#Task 1: Leap Year Checker
def leap_year(year):

    if (year % 400 == 0):
        return True
    elif (year % 100 == 0):
        return False
    elif (year % 4 == 0):
        return True
    else:
        return False

year = int(input("Enter a year: "))

if leap_year(year):
    print(str(year) + " is a leap year")
else:
    print(str(year) + " is not a leap year")
