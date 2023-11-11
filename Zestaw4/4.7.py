#solution using yield statement
def flattenyield(L):
   for item in L:
       try:
           yield from flattenyield(item)
       except TypeError:
           yield item

def flatten(L):
    fin = []

    for x in L:
        if isinstance(x, (list, tuple)):
            fin.extend(flatten(x))
        else:
            fin.append(x)

    return fin




seq = [[[[[[1]]]]], [4], (1, 2), [[[2], (3)], 3, 4], (5, 6, 7), [15, 23, 12], (-34, 2)]

#for solution with yield statement
print(list(flattenyield(seq)))


print(flatten(seq))
