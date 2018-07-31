#Viết chữ C trước cho dễ nhé
fontsize_unit = 1
chieudai = 3
chieucao = 5

fontsize = int(input("Please input the fontsize you want to draw the C: "))
n = fontsize - fontsize_unit
chieudai = chieudai + n*1
chieucao = chieucao + n*2
print("Chiều dài = ", chieudai)
print("Chiều cao = ", chieucao)


print("*"*chieudai," ","*"*chieudai," ","*"*(chieudai-1),"  ","*"*chieudai)
# for i in range (chieucao-2):
#     print("*"," "*(chieudai-1)," ","*"," "*(chieudai-2),"*"," ","*"," "*(chieudai-2),"*"," ","*"," "*(chieudai-1))
print("*"*chieudai," ","*"*chieudai," ","*"*(chieudai-1),"  ","*"*chieudai)


# fontsize = fontsize + 1
# chieudai = chieudai + 1
# chieucao = chieucao + 2 

print("*","*")
print("**")

# print()
 