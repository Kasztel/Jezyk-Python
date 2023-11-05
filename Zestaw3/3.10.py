def roman2int(text):
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0

    for i in range(len(text)):
        if i > 0 and roman[text[i]] > roman[text[i - 1]]:
            num += roman[text[i]] - 2 * roman[text[i - 1]]
        else:
            num += roman[text[i]]
    return num


print(roman2int("XIX"))
print(roman2int("MMMCCC"))
print(roman2int("CMXLIX"))

'''
można stworzyć pusty słownik i wpisywac poszczególne wartości

roman = {}
roman["I"] = 1
roman["V"] = 5
roman["X"] = 10
roman["L"] = 50
roman["C"] = 100
roman["D"] = 500
roman["M"] = 1000


lub użyć konstruktora

roman = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
'''
