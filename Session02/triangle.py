# for i in range (1,10):
#     for j in range (i):
#         print("* ", end="")
#     print()

# for i in range (4):
    # for j in range (4):
    #     if i + j >= 3 :
    #         print("*", end=" ")
    #     else:
    #         print(" ", end="")
    # print()

n=10

for i in range (n):
    for j in range (n):
        if j + i <= n - 1:
            print("  ", end="")
        else: 
            print("* ", end="")

    print()



for i in range (n): 
    for j in range (n):
        if i + j <= n-1:
            print ("  ", end="")
        else: 
            print ("* ", end="")

    print()

