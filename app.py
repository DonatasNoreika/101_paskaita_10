from modules.biudzetas import Biudzetas
import django

print("Donato programa")

biudzetas = Biudzetas()

while True:
    veiksmas = int(input("1 - įvesti pajamas\n2 - įvesti išlaidas\n3 - peržiūrėti žurnalą\n4 - gauti balansą\n0 - išeiti iš programos\n"))
    if veiksmas == 1:
        suma = float(input("Įveskite pajamų sumą: "))
        siuntejas = input("Įveskite siuntėją: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_pajamas(suma, siuntejas, info)
    if veiksmas == 2:
        suma = float(input("Įveskite išlaidų sumą: "))
        atsiskaitymo_budas = input("Įveskite atsiskaitymo būdą: ")
        isigyta_preke_paslauga = input("Įveskite įsigytą prekę ar paslaugą: ")
        info = input("Įveskite papildomą informaciją: ")
        biudzetas.prideti_islaidas(suma, atsiskaitymo_budas, isigyta_preke_paslauga, info)
    if veiksmas == 3:
        biudzetas.perziureti_zurnala()
    if veiksmas == 4:
        biudzetas.gauti_balansa()
    if veiksmas == 0:
        print("Viso gero")
        break
