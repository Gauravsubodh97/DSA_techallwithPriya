n = int(input())
lst = []
for i in range(n):
    num =int(input())
    lst.append(num)

lst.sort()
arr_To_set = set(lst)
result = arr_To_set[1]
print(result)