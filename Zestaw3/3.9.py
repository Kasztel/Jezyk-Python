seq = [[], [4], (1, 2), [3, 4], (5, 6, 7), [15, 23, 12], {-34, 2}]

fin = []

for i in seq:
    fin.append(sum(i))

print(fin)
