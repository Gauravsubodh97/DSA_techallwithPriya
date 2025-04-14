arr =[1,2,3,4,5,6,7]

#
#
# my_list = ["apple", "banana", "cherry", "date", "elderberry", "fig",
#           "grape", "honeydew", "kiwi", "lime", "mango", "nectarine"]
#
# # Traverse backward up to a maximum of 4 elements
# max_elements = 4
# for fruit in my_list[-max_elements:]:
#   print(fruit)


# arr =[202,165,89,76,12]
# number_to_insert =15
#
# for i in range(len(arr)):
#     if arr[i] <= number_to_insert:
#         arr.insert(i,number_to_insert)
#         break
#     else:
#         arr.append(number_to_insert)
# print(arr)

n = int(input('The input timing : '))

my_lst =[]

for i in range(1,n+1):
    user_input = int(input(f"inputs {i}st item: "))

    my_lst.append(user_input)
print(my_lst)


