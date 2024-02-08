ask_temp = int(input('Tempature in C?')) 

if ask_temp >= 0:
    print(float((ask_temp * 9/5) + 32)) 
elif ask_temp < 0:
    print(float((ask_temp * 9/5) + 32)) 
else:
    print('Please enter tempature')