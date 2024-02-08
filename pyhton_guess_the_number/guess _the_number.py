secret_num = int(5)

print('I am thinking of a number between 1 and 10.')

while True:
    user_guess = int(input('Whats the number? '))
    
    if user_guess == secret_num:
        print('Yes! You Win!')
        break
    else:
        print('try again loser.')


