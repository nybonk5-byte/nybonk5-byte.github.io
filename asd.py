def green(x):
    return round(float(x))*1.1
while True:
    x=(input("値段は？"))
    if x=="終了":
         break
    print(green(x))
        
