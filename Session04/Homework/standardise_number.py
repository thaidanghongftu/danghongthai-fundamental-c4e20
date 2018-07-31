balance_number = input("Enter your balance: ") # Nhập dạng text vào 
split_string = list(balance_number)
print(split_string)

split_string.insert(-3,",")
print(split_string)


print("Độ dài từ khoá: " , len(balance_number))
