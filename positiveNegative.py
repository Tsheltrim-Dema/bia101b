
## Objective:
# Create a program that takes in user input
# and determines if the number is positive or negative
# print: "Your number is positive" or "Your number is negative"

# If else
# print()
# input()

# ! 3 mins

# break down the problem
# 1. Take user input 
# cheak the type of the input
# If the type is string, how do you conveert it to an int?
# 2, Check the number is positive or negative or zero
#  need to use if else statment 
# ! a == b (is equqal to)
# ! a != b(is not equal to)
#   a > b (is grater than b)
# a<b (is less than b)
   # ! a >= b (is a greater than or equal to b)
    # ! a <= b (is a less than or equal to b)
    #* - you will be comparing numbers and not string
# ?3. Print the result

# 1. Get user input
userInput = input('Please type any number: ')
userInputType = type(userInput)
print('The type of user input is:', userInputType)

userInputNumber = float(userInput)
print('The type of userInputNumber is:', type(userInputNumber))

# 2,3 - if else statement and print
if userInputNumber > 0:
    print('The number is positive')

elif userInputNumber < 0:
    print('The number is negative')

elif userInputNumber == 0:
    print('The number is zero')


