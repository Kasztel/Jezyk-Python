line = """Lorem ipsum dolor sit amet,
consecteturGvR adipiscing elit,
sed do eiusmod GvR tempor GvRincididunt
ut labore et dolGvRore magna aliqua."""

word = "Warszawa"

L = [13, 22, 134, 25, 37, 3, 484, 14, 833, 23, 412, 1]

bignumber = 300124401002434007020

# do zmiennej length przypisujemy wartość, którą zwróci funkcja len() w parametrem line.split()
# split() dzieli nam string'a (defaultowo separatorem jest dowolny "whitespace"
print("2.10")
# 2.10

length = len(line.split())
print(length)

# do zmiennej letter_array przypisujemy po kolei wszystkie znaki łańcucha word
# do zmiennej letter (string'a) przypisujemy złączoną kolekcje letter_array, gdzie separatorem jest znak "_"
print("\n\n\n2.11")
# 2.11

letter_array = [x for x in word]
letter = "_".join(letter_array)
print(letter)

print("\n\n\n2.12")
# 2.12
# zbudowac napis stworzony z pierwszych znakow wyrazow z wiersza line

splited = line.split()

first_char = []

for element in splited:
    first_char.append(element[:1])

f_first_char = "".join(first_char)

print(f_first_char)

# -,,- z ostatnich
last_char = []

for element in splited:
    last_char.append(element[-1])

f_last_char = "".join(last_char)

print(f_last_char)

print("\n\n\n2.13")
# 2.13
numbers = []

for element in line.split():
    numbers.append(len(element))

print(sum(numbers))

print("\n\n\n2.14")
# 2.14
numbers = []
words = []

for x in splited:
    numbers.append(len(x))
    words.append(x)

print(max(words, key=len))
print(max(numbers))

print("\n\n\n2.15")
# 2.15

L_string = "".join(map(str, L))

print(L_string)

print("\n\n\n2.16")
# 2.16

replaced = line.replace("GvR", "Guido van Rossum")

print(replaced)

print("\n\n\n2.17")
# 2.17

alphabetical = sorted(splited, key=str.lower)
lengthwise = sorted(splited, key=len)

print(alphabetical)
print(lengthwise)

print("\n\n\n2.18")
# 2.18

string_big = str(bignumber)

print(string_big.count('0'))

print("\n\n\n2.19")
# 2.19

L_string_array = []
L_string_final = []

for x in L:
    L_string_array.append(str(x))


for x in L_string_array:
    L_string_final.append(x.zfill(3))

block = " ".join(L_string_final)

#print(L_string_array)
#print(L_string_final)
print(block)
