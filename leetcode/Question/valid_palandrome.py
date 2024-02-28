def isPalindrome(s):
    lst =[]

    for i in s:
        lst.append(i)


    rev=lst[::-1]

    if lst == rev:
        return lst
    else:
        return lst

s= "A man, a plan, a canal: Panama"
result =  isPalindrome(s)
print(result)
