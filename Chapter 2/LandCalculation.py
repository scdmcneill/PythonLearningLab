ACRE = 43560

totalSquareFeet = float(input('Enter the total square feet in the tract of land: '))

landAcreage = totalSquareFeet / ACRE

print('Tract Size: ', format(landAcreage, '.2f'), 'acres')