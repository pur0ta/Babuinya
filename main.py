def sum_lists(a, b):
    if len(a) > len(b):
        c = a[:]
        r = b[:]
    else:
        c = b[:]
        r = a[:]
    for i in range(len(r)):
        c[i] = c[i] + r[i]
    return c

def sub_lists(a, b):
    if len(a) > len(b):
        c = a[:]
        r = b[:]
    else:
        c = b[:]
        r = a[:]
    for i in range(len(r)):
        c[i] = c[i] - r[i]
    return c
	

# a = [0, 12, 42, -1000]
# b = [-7, 3, 1337, 7]
# print(sum_lists(a, b))
# print(sub_lists(a, b))