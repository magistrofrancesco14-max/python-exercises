# Write a program that asks the user for 5 grades, calculates the average and prints 'Promoted' or 'Failed'.

import statistics

grade_first = int(input("Enter your first grade (1-10): "))
grade_second = int(input("Enter your second grade (1-10): "))
grade_third = int(input("Enter your third grade (1-10): "))
grade_fourth = int(input("Enter your fourth grade (1-10): "))
grade_fifth = int(input("Enter your fifth grade (1-10): "))

average = statistics.mean([grade_first, grade_second, grade_third, grade_fourth, grade_fifth])

if average >= 6:
    print("Great, you got Promoted")
else:
    print("Too bad, you Failed")