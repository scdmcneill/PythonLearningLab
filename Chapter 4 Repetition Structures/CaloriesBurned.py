# Write a program that uses a loop to display the number of calories burned after 10, 15, 20, 25, and 30 minutes

CALORIES_PER_MIN = 4.2

for minute in (10, 15, 20, 25, 30):
    print('Calories Burned:', minute * CALORIES_PER_MIN, 'calories')