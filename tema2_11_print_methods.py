"""Using print methods presented:
Print: I have 1000 dollars so I can buy 3 football for 450.00 dollars.
totalMoney = 1000
quantity = 3
price = 450"""

TOTAL_MONEY = 1000
QUANTITY = 3
PRICE = 450
print("I have", TOTAL_MONEY,  "dollars so I can buy", QUANTITY, "football for", PRICE,  "dollars.")
print('I have ' + str(TOTAL_MONEY) + ' dollars so I can buy ' + str(QUANTITY)
      + ' football for ' + str(PRICE) + ' dollars.')
print(f'I have {TOTAL_MONEY} dollars so I can buy {QUANTITY} football for {PRICE} dollars.')
print('I have {} dollars so I can buy {} football for {} dollars.'.format('1000', '3', '450'))
print('I have {} dollars so I can buy {} football for {} dollars.'
      .format(TOTAL_MONEY, QUANTITY, PRICE))
print('I have {0} dollars so I can buy {1} football for {2} dollars.'
      .format(TOTAL_MONEY, QUANTITY, PRICE))
print('I have {totalMoney} dollars so I can buy {quantity} football for {price} dollars'
      .format(totalMoney=1000, quantity=3, price=450)+".")
