day_of_week = int(input('Day of weeek(0-6)?'))

print(day_of_week)

if day_of_week == int(0):
    print('Sunday') 
elif day_of_week == int(1):
    print('Monday')
elif day_of_week == int(2):
    print('Tuesday')
elif day_of_week == int(3):
    print('Wednesday')
elif day_of_week == int(4):
    print('Thursday')
elif day_of_week == int(5):
    print('Friday')
elif day_of_week == int(6):
    print('Saturday')
else:
    print('please enter a mumber 0-6')