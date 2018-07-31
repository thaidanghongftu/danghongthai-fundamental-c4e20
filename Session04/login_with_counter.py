print("Hi there, this is a super user gateway")

loop = True 
count = 0
while loop: 
    username = input("Username: ")
    if username == "c4e":
        password = input("Password: ")
        if password == "codethechange":
            print("Welcome, ", username)
            break #Thay loop = False bằng break để nếu đăng nhập đúng ở lần thứ 3 thử thì sẽ vẫn OK chứ ko bị dừng 
        else:
            print("Password is incorrect")
    else:
        print("User not found")
    if count ==3:
        print("You failed to login 3 times, go away")
        loop = False
    count += 1