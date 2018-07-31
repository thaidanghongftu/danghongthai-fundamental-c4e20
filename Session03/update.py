print("Hi there, your favorite things so far below: ")
print("*"*20)
favs = ["death note","netflix","teaching"]
for index, fav in enumerate(favs):
    print("{}. {}".format(index+1,fav)) 
print("*"*20)
pos = int(input("Position you wanna update: "))
update_fav = input("New favorite you wanna update: ")

favs[pos-1] = update_fav

print("*"*20)
for index, fav in enumerate(favs):
    print("{}. {}".format(index+1,fav)) 
print("*"*20)