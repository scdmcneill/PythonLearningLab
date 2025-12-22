# Write a program that calculates the number of packages of hot dogs and the number of packages of hot dog
# buns needed for the cookout and the number of hot dogs each person will be given. The program should display the 
# following details:
#   - The min number of packages of hot dogs required
#   - The min number of packages of hot dog buns required
#   - The number of hot dogs leftover
#   - The number of hot dog buns leftover

HOTDOG_PACKAGE_COUNT = 10
BUN_PACKAGE_COUNT = 8

dogCount = int(input('How many hotdogs will be given per guest?:'))
attendeeCount = int(input('How many guests will attend the cookout?:'))

totalDogs = attendeeCount * dogCount

dogPackagesNeeded = totalDogs // HOTDOG_PACKAGE_COUNT
if totalDogs % HOTDOG_PACKAGE_COUNT > 0:
    dogPackagesNeeded += 1

bunPackagesNeeded = totalDogs // BUN_PACKAGE_COUNT
if totalDogs % BUN_PACKAGE_COUNT > 0:
    bunPackagesNeeded += 1

dogsLeftover = dogPackagesNeeded * HOTDOG_PACKAGE_COUNT - totalDogs
bunsLeftover = bunPackagesNeeded * BUN_PACKAGE_COUNT - totalDogs
    
print('\nMinimum number of packages of hot dogs required:', int(dogPackagesNeeded))
print('Minimum number of packages of buns requried:', int(bunPackagesNeeded))
print('Number of Hotdogs Leftover:', dogsLeftover)
print('Number of Buns Leftover:', bunsLeftover)