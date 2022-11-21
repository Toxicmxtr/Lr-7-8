a = input()
cnt = 0
for i in range(len(a)):
    if a[i] == 'a' or a[i] == 'b' or a[i] == 'c':
        cnt += 1
if cnt == len(a):
    print('Да')
else:
    print('Нет')
