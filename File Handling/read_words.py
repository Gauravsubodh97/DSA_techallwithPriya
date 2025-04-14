with open("C:/Users/gaurav.subodh/Downloads/example_file.txt",'r+') as f1:
    content = f1.read()
    print(content)

count = 0
for i in range(len(content)):
    count +=1
print("total letter count is :- ",count)


words = content.split()
count = len(words)  
print("Total word count is:", count)