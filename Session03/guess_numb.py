from random import randint
numb = randint(0,100)
print(numb)

playing = True 
count = 0
while playing: 

    guess = int(input("Guess my number (0-100): "))
    if guess < numb :
        print("A little too small :(")
    elif guess > numb:
        print("A little too big :(")
    else:
        print("Bingo")
        break 

    count +=1
    if count ==7:
        print("You lose")
        




