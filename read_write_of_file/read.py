# f = open('for_read.txt', 'r')
# rd= f.readline()
# print(rd)
#
# file1 = open('for_read.txt','w+')
# file1.writelines(["He provides me all the things I need \n"," He is the Almighty Lord"])
# file1.close()


# file1 = open('for_read.txt','r+')
# print(file1.read())

# print(file1.read(3))
# print("Output of Readline(9) function is ")
# print(file1.readline(2))
# print(file1.readlines(4))

with open('for_read.txt', 'r+') as file:
    file.write('I am the best')

with open('for_read.txt', 'r+') as file2:
    print(file2.readline())

with open('for_read.txt', 'a') as file3:
    line = "the new line added\n"
    file3.write(line)

with open('for_read.txt','r+') as file3:
    content=file3.read()
    print(content)
