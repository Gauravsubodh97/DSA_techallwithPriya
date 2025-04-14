# WITH IS A REPLACEMENT OF CLOSE() OPERATION
with open('sample2.txt','w') as f:
    f.write('I have a total control on devil With God Grace')
#with is automatically closing here the file

with open('sample2.txt','r') as f:
    print(f.readline(6))

with open('sample2.txt','r') as f:
    print(f.read())

#phenomina because of buffer memory
with open('sample2.txt','r') as f:
    print(f.read(10))
    print(f.read(10))
    print(f.read(11))

#reading big file in chunk
big_txt = ['Netow was a scientiest\n' for i in range(10)]
with open('big_file','w') as o:
    o.writelines(big_txt)

f = open('big_file','r')
print(f.read())
f.close()

# with open('big_file','r') as f:
#
#     chunk_size =10
#
#     while len(f.read(chunk_size)) >0:
#         print(f.read(chunk_size),end ='*')

