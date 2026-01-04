# Write a program that asks the user to enter the amount that he or she has budgeted for a month. A loop should then
# prompt the user to enter each of his or her expenses for the month and keep a running total. When the loop finishes,
# the program should display the amount that the user is over or under budget.

userBudget = float(input('Enter your budget for the month: $'))

nextEntry = 'y'

totalExpenses = 0

while nextEntry == 'y':
    expense = float(input('Enter expense amount: $'))
    totalExpenses += expense
    nextEntry = input('Do you have another expense? y/n')

remainingBudget = userBudget - totalExpenses

print('Total amount spent: $', totalExpenses)
if remainingBudget < 0:
    print('You are over budget by: $', remainingBudget)
else:
    print('You are under budget by: $', remainingBudget)
