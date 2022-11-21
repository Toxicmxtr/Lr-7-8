s = input()
d = len(s)
if d > 10:
    print(s[0:6])
elif d < 13:
    while d <= 12:
        s += '0'
        d += 1
    print(s)