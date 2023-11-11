# solution using flatten function
def flatten(L):
    for item in L:
        try:
            yield from flatten(item)
        except TypeError:
            yield item


# solutino using flatten function
def sum_seqflat(sequence):
    return sum(list(flatten(sequence)))


def sum_seq(sequence):
    fin = 0
    for item in sequence:
        if isinstance(item, (list, tuple)):
            fin += sum_seq(item)
        else:
            fin += item
    return fin


seq = [[([[[[95]]]])], [4], (1, 2), [[[2], (3, 50)], 3, 4], (5, 6, 7), [15, 23, 12], (-34, 2)]

print(sum_seqflat(seq))
print(sum_seq(seq))
