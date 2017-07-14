a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c = []
i = 0
while i <= len(b):
    if a.count(i) in a:
        if a.count(i) in b:
            c.append(i)
    i += 1
print(c)