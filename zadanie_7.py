a=float(input("Podaj wartość a:"))
b=float(input("Podaj wartość b:"))

if a!=0:
    if b==0:
        x=0.0
        print("Równanie tożsamościowe")
    else:
        x=(-b)/a
        print(f"Rozwiązaniem równania jest liczba: {x} .")
else:
    print("Równanie sprzeczne")