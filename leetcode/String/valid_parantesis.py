def valid_para(strs):
    stack =[]
    lookup = { ')':'(',']':'[','}':'{'}
    for p in strs:
        if p in lookup.values():
            stack.append(p)
        elif stack and lookup[p] == stack[-1]:
            stack.pop()
        else:
            return False
    return stack == []


# driver code
strs ="()[]{"
result= valid_para(strs)
print(result)