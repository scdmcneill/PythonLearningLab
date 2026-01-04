# If a moderately active person cuts their calorie intake by 500 calories a day, they can typically lose about 4 pounds a month. 
# Write a program that lets the user enter their starting weight, then creates and displays a table showing what their expected 
# weight will be at the end of each month for the next 6 months if they stay on this diet.

startingWeight = float(input('Enter your starting weight:'))
weightLoss = 4
monthsOnDiet = 6
totalWeightLost = 0

for month in range(1, monthsOnDiet + 1, 1):
    weight = startingWeight - (4 * month)
    
    print('Month', month)
    print('Weight:', weight)

totalWeightLost = 4 * monthsOnDiet
print('Total Weight Lost:', totalWeightLost, 'pounds.')