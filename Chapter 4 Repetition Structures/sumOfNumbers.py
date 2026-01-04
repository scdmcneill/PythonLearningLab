# Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative 
# number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum.

number = int(input('Enter a series of positive numbers, a negative number will signal the end of the series:'))
total = 0

while number > 0:
    total = total + number
    number = int(input('Enter a series of positive numbers, a negative number will signal the end of the series:'))

print('Total:', total)