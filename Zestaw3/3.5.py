dots = "...."
vertical = "|"

n = input("ruller length: ")
output = ""

length = int(n)

#creating output string
for i in range (0, length):
    output += vertical + dots
output += vertical + "\n"


for k in range(0, length):
    output += str(k) + (" " * (5 - len(str(k+1))))

output += str(n)



print(output)



