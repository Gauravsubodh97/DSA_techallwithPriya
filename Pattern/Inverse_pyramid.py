size = 5
for i in range(0, size):
    for j in range(0,i):
        print(" ", end="")
    for j in range(0,size-i-1):
        print('*', end=" ")
    print()

print()

print('second method')
print()
n =5
for i in range(0,n):
    for j in range(0,i):
        print(" ",end="")
    for j in range(i,n):
        print("*",end ="")
    for j in range(i,n):
        print("*",end ="")
    print()