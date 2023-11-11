# we could've use array slicing, but it's not in-place solution
def odwracanieIT(L, left, right):
    if left < 0 or left > right or right > len(L)-1:
        raise ValueError("Illegal value")

    size = left + right
    for i in range(left, (size + 1) // 2):
        j = size - i
        L[i], L[j] = L[j], L[i]


def odwracanieREC(L, left, right):
    if left >= right:
        return L
    if left < 0 or left > right or right > len(L) - 1:
        raise ValueError("Invalid input")

    L[left], L[right] = L[right], L[left]

    return odwracanieREC(L, left + 1, right - 1)


myList1 = list(range(10))
myList2 = list(range(11))

print(myList1)
print(myList2)
print()

odwracanieIT(myList1, 2, 9)
#odwracanieREC(myList1, 0, 9)
#odwracanieIT(myList2, 2, 10)
odwracanieREC(myList2, 2, 10)

print(myList1)
print(myList2)
