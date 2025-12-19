# A vineyard owner is planting several new rows of grapevines, and needs to know how many grapevines to plant
# in each row. She has determined that after measuring the length of a future row, she can use the following
# formula to calculate the number of vines that will fit in the row, along with the trellis end-post assemblies
# that will need to be constructed at each end of the row
# V = (R - 2E) / S
#   - V = number of grapevines that fit in row
#   - R = length of row in feet
#   - E = amount of space, in feet, used by an end-post assembly
#   - S = space between vines, in feet
# Write a program that makes the calculation for the vineowner. The program should ask the user to input the 
# following:
#   - length of row, in feet
#   - amount of space used by an end-post assembly, in feet
#   - amount of space between the vines in feet

rowLength = float(input('Enter the length of the grapevine row in feet: '))
assemblySpace = float(input('Enter the space needed for the end-post assembly in feet: '))
spaceBetweenVines = float(input('Enter the space between vines in feet: '))

vineCapacity = ((rowLength - (2 * assemblySpace)) / spaceBetweenVines)

print('The vine capacity for each row is', vineCapacity, 'vines.')