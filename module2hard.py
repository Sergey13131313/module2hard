number = ''
while True:
    number = input('Введите число от 3 до 20: ')
    if number.isdigit() == False:
        print('Неверно, поробуйте ещё раз!')
        continue
    elif int(number) < 3 or int(number) > 20:
        print('Неверно, поробуйте ещё раз!')
        continue
    else:
        break

result = []
a = int(number) // 2
if int(number) % 2 != 0:
    a += 1
for i in range(1, a):
    for j in range(2, int(number) - 1):
        if (int(number) % (i + j)) == 0:
            result.append(i)
            result.append(j)

print(result)
print(len(result))