bok1 = float(input("Podaj długość pierwszego boku: "))
bok2 = float(input("Podaj długość drugiego boku: "))

if bok1 >= 0 and bok2 >=0:
    pole_prostokata = bok1 * bok2
    obwod_prostokata = (2 * bok1) + (2 * bok2)
    print("Pole prostokąta wynosi:", pole_prostokata)
    print("Obwód prostokąta wynosi:", obwod_prostokata)
else:
    print("Długości boków prostokąta muszą być liczbami dodatnimi.")
