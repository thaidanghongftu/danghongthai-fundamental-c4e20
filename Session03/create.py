# Thêm phần tử vào list sở thích cá nhân của mình
favs = ["death note","netflix","teaching"]
print("Hi there, here you favorite thing so far")
print(*favs,sep=", ")

new_favs = input("Name one thing you wanna add")
favs.append(new_favs)

print(*favs,sep=", ")

