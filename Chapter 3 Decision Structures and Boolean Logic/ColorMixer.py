# Design a program that prompts the user to enter the names of two primary colors to mix. If the user enters anything other
# than "red", "blue", or "yellow", the program should display an error message. Otherwise, th eprogram should display the name
# of the secondary color that results.

firstColor = input('Enter the first primary color to mix:')

if firstColor != 'red' and firstColor != 'blue' and firstColor != 'yellow':
    print('Error: please enter only primary colors.')
    firstColor = input('Enter the first primary color to mix:')

secondColor = input('Enter the second primary color to mix:')

if secondColor != 'red' and secondColor != 'blue' and secondColor != 'yellow':
    print('Error: please enter only primary colors.')
    secondColor = input('Enter the second primary color to mix:')

def colorMixer(color1, color2):
    if color1 == 'blue' or color2 == 'blue':
        if color1 == 'yellow' or color2 == 'yellow':
            return 'green'

    if color1 == 'blue' or color2 == 'blue':
        if color1 == 'red' or color2 == 'red':
            return 'purple'

    if color1 == 'blue' or color2 == 'blue':
        if color1 == 'blue' or color2 == 'blue':
            return 'blue'

    if color1 == 'red' or color2 == 'red':
        if color1 == 'blue' or color2 == 'blue':
            return 'purple'
    
    if color1 == 'red' or color2 == 'red':
        if color1 == 'yellow' or color2 == 'yellow':
            return 'orange'

    if color1 == 'red' or color2 == 'red':
        if color1 == 'red' or color2 == 'red':
            return 'red'

    if color1 == 'yellow' or color2 == 'yellow':
        if color1 == 'red' or color2 == 'red':
            return 'orange'

    if color1 == 'yellow' or color2 == 'yellow':
        if color1 == 'blue' or color2 == 'blue':
            return 'green'

    if color1 == 'yellow' or color2 == 'yellow':
        if color1 == 'yellow' or color2 == 'yellow':
            return 'yellow'

print(firstColor, 'and', secondColor, 'make:', colorMixer(firstColor, secondColor))