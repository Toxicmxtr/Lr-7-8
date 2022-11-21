from itertools import count


s = input()
cnt = 0 
for i in s:
    if i.isdigit():
        cnt += 1
print(cnt)