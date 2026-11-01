import random

droga=random.randint(1,800)
spalanie=float(input("Podaj średnie spalanie (litr/100 km): "))
paliwo=float(input("Podaj aktualną cenę poliwa za 1 litr: "))

zuzyte_paliwo=round((droga/100)*spalanie,2)
cena_trasy=round((paliwo*zuzyte_paliwo),2)
print("Szacowane zużycie plaiwa to: ",zuzyte_paliwo,"l .")
print("\nSzacowane koszty podróży: ",cena_trasy," zł.")