
def longestCommonPrefix(strs):
    ans = ''
    strs = sorted(strs)

    first = strs[0]
    last = strs[-1]

    for i in range(min(len(first), len(last))):
        if (first[i] != last[i]):
            return ans
        else:
            ans += first[i]
    return ans


#driver code
strs = ["flower","flow","flight"]
result =longestCommonPrefix(strs)
print(result)

