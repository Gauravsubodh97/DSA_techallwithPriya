def dicount(*total):
    total = [20, 30, 44, 98, 34, 12]
    total_amount =0

    for amount in total:
        total_amount = total_amount + amount
    return total_amount


# # driver code
total =[20,30,44,98,34,12]
result = dicount(total)
print(result)