from random import randint
mood = randint(0,100)
print(mood)
if mood <= 30 :
    print("I am sad")

elif mood >= 60 :
    print("Let's rock the world")

else:
    print("I am OK")

