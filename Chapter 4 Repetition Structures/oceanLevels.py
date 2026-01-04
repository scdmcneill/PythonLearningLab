# Assuming the ocean’s level is currently rising at about 1.6 millimeters per year, create an application that displays 
# the number of millimeters that the ocean will have risen each year for the next 25 years.

risingRate = 1.6
years = 25
oceanLevel = 0

for year in range(1, years + 1, 1):
    oceanLevel = risingRate * year
    print('Ocean Level: +', format(oceanLevel, '.1f'), 'milimeters')