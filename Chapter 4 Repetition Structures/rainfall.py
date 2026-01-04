# Write a program that uses nested loops to collect data and calculate the average rainfall over a period of years. 
# The program should first ask for the number of years. The outer loop will iterate once for each year. 
# The inner loop will iterate twelve times, once for each month. Each iteration of the inner loop will ask the user 
# for the inches of rainfall for that month. After all iterations, the program should display the number of months, 
# the total inches of rainfall, and the average rainfall per month for the entire period.

numOfYears = int(input('Enter the number of years:'))

months = 12
monthCount = 0
totalRainfall = 0
averageRainfall = 0

for year in range(1, numOfYears + 1, 1):
    for month in range(1, months + 1, 1):
        print('Month:', month, 'Year:', year)
        rainfall = float(input('Enter the inches of rainfall:'))
        totalRainfall = totalRainfall + rainfall
        monthCount = monthCount + 1

averageRainfall = totalRainfall / monthCount

print('Total Rainfall:', totalRainfall)
print('Average Rainfall per month:', averageRainfall)