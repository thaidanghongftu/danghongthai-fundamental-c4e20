# Lưu các món ăn trong nhà hàng 
# Để khai báo một list trong python ta dùng dấu đóng mở ngoặc vuông [ ] 
menu = [
    "Cơm",
    "Cá",
    "Thịt Bò",
    "Pizza"
    ]
print(menu)

# để không hiện kết quả chứa các dấu thừa ta dùng dấu sao trước biến menu 

print(*menu)

# Dùng lệnh sep="  " để tạo separator phân cách nội dung 
print(*menu, sep=",")

# Dùng append để thêm phần tử 
menu.append("Ghẹ")
print(*menu,sep=",")

# Dùng len() để đếm số phần tử 
print(len(menu))

print(menu[-2])

# in ra từng phần tử 

for i in range (len(menu)):
    print(menu[i])

for index, item in enumerate(menu):
    print(index + 1,item, sep=". ")

for item in menu:
    print(item)


for index, item in enumerate(menu):
    print("{}. {}".format(index+1,item)) 

    # Update phần tử vào chuỗi 
    menu[4] = "Sữa Chua"