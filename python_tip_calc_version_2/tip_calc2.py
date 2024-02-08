# tip_calc2,py

bill_amount = float(input('Total bill amount?:'))
print('Bill amount:', bill_amount)

level_of_service = input('Level of service?: (bad = 10%, fair = 15%, good = 20%)')

tip_amount = level_of_service

bad = float(bill_amount * .10) 

fair = float(bill_amount * .15)

good = float(bill_amount * .20)

print('Level of service:', level_of_service)

split_check = int(input('Split bill how many ways?'))

print('Split bill how may ways:', split_check)


if tip_amount == 'bad':
    print('Tip amount: $', float(bad))
elif tip_amount == 'fair':
    print('Tip amount: $', float(fair))
elif tip_amount == 'good':
    print('Tip amount: $', float(good))
else:
    print('ERROR!')

if tip_amount == 'bad':
    print('Total amount: $', bill_amount + bad)
elif tip_amount == 'fair':
    print('Total amount: $', bill_amount + fair)
elif tip_amount == 'good':
    print('Total amount: $', bill_amount + good)


if split_check  > 1:
    print('Amount per person: $', (bill_amount + bad) / split_check)

 