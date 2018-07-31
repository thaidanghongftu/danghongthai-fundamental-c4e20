numb = int(input("Enter a number: "))

counting = True
count = 0


while counting:
    numb = numb // 10
    count += 1
    if numb == 0:
        counting = False

print(count)
