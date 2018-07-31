number = 23
guess = int(input('What is your guess number?'))

while True: 

    if guess == number:
        print('Congrats! Done!')
    while number != guess:
        print('Sorry you are so wrong!')
        if guess < number: 
            print('Your guess is a bit lower than actual number, try again')
        else: 
            print('Your guess is a bit higher, try again la!')
        guess = int(input('What is your guess number again?'))
        if guess == number: 
            print('Congrats! Done!')

    print('''Let's play again!''')    
    guess = int(input('What is your guess number?'))



        