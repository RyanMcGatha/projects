day_of_week2 = int(input('Day of week(0-6)?'))

print(day_of_week2)

if day_of_week2 == 0 or day_of_week2 == 6:
    print('Sleep in') 
elif day_of_week2  >= 1 <=6: 
    print('Go to work')     
else:
    print('please enter a number 0-6')