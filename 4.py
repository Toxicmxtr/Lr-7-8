a = input()
for i in range(len(a)):
    if len(a) > 6:
        print(a[0], a[1], a[2], a[-1], a[-2], a[-3])
    else:
        print((a[0]) * len(a))