a = [2, 0, 4, 0, 0, 1]

for i in range(0, len(a)):

    if a[i] == 0:
        a.append(0)
        a.remove(0)


print(a)