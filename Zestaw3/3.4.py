while True:
    x = input("Podaj rzeczywistą liczbe: ")
    if x == "stop":
        break
    try:
        num = float(x)
    except:
        print("Not a real number")
    else:
        print(num)
        print(num**3)