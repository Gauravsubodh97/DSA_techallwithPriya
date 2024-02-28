

def PalinArray(arr, n):
    for i in arr:
        if str(i) != str(i)[::-1]:
            return False
    return True

#driver code
arr = [111 ,222, 333, 444 ,555]
n =5
result = PalinArray(arr,n)
print(result)