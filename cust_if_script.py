#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = 'Your grade will be determined off of your most recent test score'

# wrap connection in a float() to accept decimals as numbers
test_grade = float(input("What was your most recent test grade? (1 - 100) "))

# if input value was higher or equal to 90
if test_grade >= 90 and test_grade < 100:
    message = message + ', and you got an A.'
elif test_grade >= 80 and test_grade < 90:
    message = message + ' ,and you got a B'
elif test_grade >= 70 and test_grade < 80:
    message = message + ' ,and you got a C'
else:
    message = message + ', you did not pass the test'
print(message)

