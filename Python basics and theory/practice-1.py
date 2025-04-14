lst = [5,18,77,108,930]

to_insert =100

for i in range(len(lst)):
    if to_insert <= i:
        lst.append(to_insert)
print(lst)