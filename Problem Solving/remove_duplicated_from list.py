# Remove duplicates from a list while maintaining order.

def remove_dup(arg):
    lst1 = set(arg)
    return lst1


def seq_remove(arg1):
    lst2 = []
    for ele in arg1:
        if ele not in lst2:
            lst2.append(ele)
    return lst2


lst = [5, 6, 66, 7, 54, 3, 'a', 'a', 'apple', 'apple']
print('The de duplicated list is :-', remove_dup(lst))
print('The de duplicated list with maintaning sequence is:- ', seq_remove(lst))
