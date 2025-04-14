from loguru import logger

labour = ['Ramesh', 'Suresh', 'Bunty', 'Sonty','kamlesh','hitesh']

# for i in labour:
#     print(i,end=",")



#range(from , to ,step)

# for i in range(1,11,2):
#     print(i,end=",")

for i in range(len(labour)):
    logger.info(f"the labour {i+1} is {labour[i]}")


#star pattern
for i in range(5):
    print(i*"*")

#print all even number upto 1 to 100

for i in range(101):
    if i % 2 == 0:
        print(i,end=" ")


        