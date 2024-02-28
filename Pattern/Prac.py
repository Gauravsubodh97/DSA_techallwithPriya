n = 5
for i in range(0,n):
    for j in range(i,n):
        print(" ", end="")
    for j in range(0,i):
        print("*",end ="")
    print()

print()
print('second pattern')
print()
for i in range(0,n):
    for j in range(i,n):
        print("*",end=" ")
    print()

print()
print("Third pattern")
print()
for i in range(0,n):
    for j in range(i+1):
        print('*',end =" ")
    print()

print()
print('forth pattern ')
print()
for i in range(0,n):
    for j in range(i+1):
        print(" ",end="")
    for k in range(n-i-1):
        print("*",end ="")
    print()

print()
print('fifth pattern')
print()

for i in range(0,n):
    for j in range(i,n):
        print(" ",end="")

    for k in range(i+1):
        print("*",end=" ")
    print()

print()
print("Sixth pattern 'dimond'")
print()
s=8

for i in range(0,s):
    for j in range(i,s):
        print(" ",end="")

    for k in range(i):
        print("*",end=" ")
    print()

    for l in range(s//2,s):
        for m in range(l+1):
            print(" ",end ="")
        for n in range(s-l-1):
            print("*",end =" ")