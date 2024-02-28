
#READ

f=open('sample.txt','r')
s=f.read()
print(s)
f.close()

f=open('sample1.txt','r')
s=f.readline()
print(s)
f.close()

f=open('sample1.txt','r')
print(f.readline())
print(f.readline())
f.close()

# readline() -'print one line at a time

f=open('sample1.txt','r')
print(f.readline(),end='')
print(f.readline(),end='')
f.close()

# reading entire file with custome code using readline()

f =open('sample1.txt','r')

while True:
    data = f.readline()
    if data =='':
        break
    else:
        print(data,end='')
f.close()
