# A customer in a store is purchasing five items. Write a program that asks for the price of each item, then displays
# the subtotal of the sale, the amount of sales tax, and the total. Assume the sales tax is 7 percent.

SALES_TAX = 0.07

item1Price = float(input('Enter the price of the first item: '))
item2Price = float(input('Enter the price of the second item: '))
item3Price = float(input('Enter the price of the third item: '))
item4Price = float(input('Enter the price of the fourth item: '))
item5Price = float(input('Enter the price of the fifth item: '))

subtotal = item1Price + item2Price + item3Price + item4Price + item5Price

tax = subtotal * SALES_TAX

total = subtotal * (1 + SALES_TAX)

print('Subtotal: $', format(subtotal, '.2f'), sep = '')
print('Tax: $', format(tax, '.2f'), sep = '')
print('Total: $', format(total, '.2f'), sep = '')