n = int(input('Введите число от 3 до 20:'))
res = []
for j in range(1, n):
    for k in range(2, n):
        if n % (j+k) == 0 and j < k:
            a = str(j) + str(k)
            res.append(a)
result = ''.join(res)
print(result)
