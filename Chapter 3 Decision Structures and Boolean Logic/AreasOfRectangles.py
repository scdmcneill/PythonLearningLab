# The area of a rectangle is the rectangle's length times its width. Write a program that asks for the length and width
# of two rectangles. The program should tell the user which rectangle has the greater area, or if the areas
# are the same.

lengthRectangle1 = float(input('Enter the length of the first rectangle:'))
widthRectangle1 = float(input('Enter the width of the first rectangle:'))

lengthRectangle2 = float(input('Enter the length of the second rectangle:'))
widthRectangle2 = float(input('Enter the width of the second rectangle:'))

def area(length, width):
    area = length * width
    return area

rectangle1Area = area(lengthRectangle1, widthRectangle2)
rectangle2Area = area(lengthRectangle2, widthRectangle2)

print('Area of 1st Rectangle: ', format(rectangle1Area, '.2f'))
print('Area of 2nd Rectange:', format(rectangle2Area, '.2f'))

if rectangle1Area > rectangle2Area:
    print('Rectangle 1 is larger in area.')
elif rectangle1Area == rectangle2Area:
    print('The rectangles are even in size')
else:
    print('Rectangle 2 is larger in area.')

