from random import choice 
# Trên đã dùng module choice nên không được đặt tên biến trùng tên là choice 

words = ["champion","dungeon","vodka"]

word = choice(words)
# chars viết tắt của biến characters để chứa list các chữ cái 
chars = list(word)
updated_chars = []

loop = True 
while loop: 
    rand_chars = choice(chars)
    updated_chars.append(rand_chars)
    chars.remove(rand_chars)
    if len(chars) == 0:
        loop = False

print(*updated_chars)

ans = input("Your guess: ")
if ans == word:
    print("Huraaaa")
else: 
    print(":<")

