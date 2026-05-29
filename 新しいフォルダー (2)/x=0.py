def green(price):
    return float(price)*1.1
def blue(price):
    return float(price)*1.08
while True:
    price=(input("値段は"))
    if price=="終了":
        break
    while True:
        tax=input(("8%?or10%?"))
        if tax=="10"or tax=="10%":
            print(green(price))
            break
        elif tax=="8"or tax=="8%":
            print(blue(price))
            break
        else:
            print("やり直し！")