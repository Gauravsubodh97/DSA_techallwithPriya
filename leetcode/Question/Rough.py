def longstSubStr(str):
    st =0
    m =0
    d ={}
    for i ,v in enumerate(str):
        if v in d and st <=d[v]:
            st = d[v] +1
        else:
            m = max(m,i-st +1)
        d[v] =i
    return m
#driver code
str = 'au'
result = longstSubStr(str)
print(result)