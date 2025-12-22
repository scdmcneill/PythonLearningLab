# Write a program that asks the user for a numebr in the range of 1 through 7. The program should display the corresponding
# day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, 7 = Sunday
# The program should display an error message if the user enters a number that is outside the range of 1 through 7.

dayOfWeek = int(input('Enter a number in the range of 1 through 7: '))

if dayOfWeek == 1:
    print('Monday')

if dayOfWeek == 2:
    print('Tuesday')

if dayOfWeek == 3:
    print('Wednesday')

if dayOfWeek == 4:
    print('Thursday')

if dayOfWeek == 5:
    print('Friday')

if dayOfWeek == 6:
    print('Saturday')

if dayOfWeek == 7:
    print('Sunday')

if dayOfWeek != 1 and 2 and 3 and 4 and 5 and 6 and 7:
    print('Error: Number must be between 1 and 7.')
    