liczba_1=float(input("Podaj pierwszą liczbę: "))
liczba_2=float(input("Podaj drugą liczbę: "))

suma=liczba_1+liczba_2
roznica=liczba_1-liczba_2
iloczyn=liczba_1*liczba_2
potega=liczba_1**liczba_2

print(f"\nWyniki działań dla liczb {liczba_1} oraz {liczba_2}:")
print(f"Dodawanie: {suma}")
print(f"Odejmowanie: {roznica}")
print(f"Mnożenie: {iloczyn}")
print(f"Potęgowanie: {potega}")

if liczba_2 != 0:
    iloraz=liczba_1/liczba_2
    print(f"Dzielenie: {iloraz}")
else:
    print("Dzielenie: Nie można dzielić przez 0")