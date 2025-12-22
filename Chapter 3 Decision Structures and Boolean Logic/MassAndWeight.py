# Write a program that asks the user to enter an object's mass, then calculates its weight. If the object weighs more than
# 500 newtons, display a message indicating that it is too heavy. If the obejct weighs less than 100 newtons, display a message
# indicating that it is too light

objectMass = float(input('Enter the mass of the object: '))

weight = objectMass * 9.8

if weight < 100:
    print('Error: the object is too light.')
    print('Object\'s weight: ', weight)
elif weight > 500:
    print('Error: the object is too heavy.')
    print('Object\'s weight: ', weight)
else:
    print('Weight: ', format(weight, '.2f'))