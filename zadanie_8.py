from math import sqrt

a=float(input("Podaj wartość a: "))
b=float(input("Podaj wartość b: "))
c=float(input("Podaj wartość c: "))

if a==0:
    if b != 0:
        if c == 0:
            x = 0.0
            print("Równanie tożsamościowe")
        else:
            x = (-c) / b
            print(f"Rozwiązaniem równania jest liczba: {x} .")
    else:
        print("Równanie sprzeczne")
else:
    delta=b**2-4*a*c
    if delta>0:
        pierwiastek_z_delty = sqrt(delta)
        x1=(-b+pierwiastek_z_delty)/(2*a)
        x2=(-b-pierwiastek_z_delty)/(2*a)
        print(f"Rozwiązania funkcji: {x1}, {x2} .")
    elif delta==0:
        x1=(-b)/(2*a)
        x2=x1
        print(f"Rozwiązanie funkcji: {x1} .")
    else:
        print("Funkcja nie ma rozwiązań dla tych wartości.")