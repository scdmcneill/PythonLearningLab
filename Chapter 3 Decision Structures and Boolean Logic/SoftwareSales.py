# Write a program that asks the user to enter the number of packages purchased. The program should then
# display the amount of the discount (if any) and the total amount of the purchase after the discount.

packagesPurchased = int(input('Enter the number of packages purchased:'))

if packagesPurchased >= 10 and packagesPurchased <= 19:
    discount = 10
elif packagesPurchased >= 20 and packagesPurchased <= 49:
    discount = 20
elif packagesPurchased >= 50 and packagesPurchased <= 99:
    discount = 30
elif packagesPurchased >= 100:
    discount = 40

if discount > 0:
    print('Discount Applied:', discount, '%')
