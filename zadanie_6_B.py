droga=float(input("Podaj przebytą drogę w km: "))
spalanie=float(input("Podaj średnie spalanie (litr/100 km): "))
paliwo=6.5

zuzyte_paliwo=round((droga/100)*spalanie,2)
cena_trasy=round((paliwo*zuzyte_paliwo),2)
print(f"Szacowane zużycie plaiwa to: {zuzyte_paliwo} l.")
print(f"\nSzacowane koszty podróży: {cena_trasy} zł.")