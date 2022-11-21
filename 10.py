s = input()
if (s[0]=='a' and s[1]=='b' and s[2]=='c'):
    print(s.replace ('abc','www'))
else:
    s += "zzz"
    print(s)