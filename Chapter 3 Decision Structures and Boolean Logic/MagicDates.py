# Design a program that asks the user to enter a month (in numeric form), a day, and a two-digit year. The program
# should then determine whetehr the month times the day equals the year. If so, it should display a message
# saying the date is magic. Otherwise, it should display a message saying the date is not magic.

userMonth = int(input('Enter a month:'))
userDay = int(input('Enter a day:'))
userYear = int(input('Enter a two-digit year:'))

def magicYear(month, day, year):
    if month * day == year:
        print('You entered a magic date!')
    else:
        print('Sorry, you did not enter a magic date.')

magicYear(userMonth, userDay, userYear)