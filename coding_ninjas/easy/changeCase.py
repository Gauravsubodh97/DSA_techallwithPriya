string1 = 'Hello WOrld'
res = ""

for char in string1:
    if 'A' <= char <= 'Z':
        res += chr(ord(char) +32)
    else:
        res+=char
print('To lower case :- ', res)


# Upper case
result = ''
for ch in string1:
    if 'a' <= ch <= 'z':
        result += chr(ord(ch) - 32)
    else:
        result+=ch
print('to upper case :-', result)
