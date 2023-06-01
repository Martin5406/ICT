import random
import json

# Načtení dat z JSON souboru
with open("otázky.JSON", encoding="utf-8") as f:
    data = json.load(f)

# Funkce která vybírá náhodnou otázku, která nebyla použita
def nacteni_otazek(vybrane_otazky):
    dostupne_otazky = []

# Nachází otázky, které nebyly použity
    for i in range(len(data["otazky"])):
        if i not in vybrane_otazky:
            dostupne_otazky.append(i)

# Vybere náhodnou otázku
    otazka_index = random.choice(dostupne_otazky)

    return data["otazky"][otazka_index], otazka_index

# Funkce samotné hry
def hra():
    print("Vítejte ve hře Chcete být milionářem!")
    jmeno = input("Jaké je tvé jméno?:")
    print("\nVítej", jmeno + "!")

# Vysvětlí pravidla hry
    count = 0
    while count < 1:
        print("\nVysvětlím ti pravidla hry:"
              "\n"
            "\nCelkem je 10 otázek."
            "\nNa každou otázku musíš odpovědět z možností a, b, c nebo d."
            "\nPokud odpovíš správně, postupuješ na další otázku."
            "\nZa každou správně zodpovězenou otázku se ti do výhry přičte 10 000 $."
            "\nPokud však odpovíš špatně, dál nepostupuješ a získáš výhru za správně zodpovězené otázky.")
        
        print("\nPokud ti jsou pravidla jasná, stiskni 1:"
            "\nPokud je chceš vysvětlit znovu, stiskni 0:")
        
        x = int(input("Vyberte možnost 1 nebo 0:"))
        
        if x == 1:
            count += 1
        elif x == 0:
            continue


# Počitání otázek a výhry
    otazky = 0
    vyhra = 0

# Pole ktéré uchovává indexy otázek, které byly položney
    vybrane_otazky = []

# První otázka
    while otazky < 1:
        print("\nVýborně!")
        print("Začněme tedy otázkou č.", otazky + 1, "za", vyhra+10000, "$")

# Volá funkci nacteni_otazek
        otazka, otazka_index = nacteni_otazek(vybrane_otazky)

# Výpis otázky a odpovědí
        print(otazka["otazka"])
        for moznost, odpoved in otazka["moznosti"].items():
            print(moznost + ") " + odpoved)

# Výběr uživatele mezi možnostmi a,b,c,d
        user_odpoved = input("Zadejte písmeno správné odpovědi:")

# Zodpovězení otázky správně
        if user_odpoved.lower() == otazka["odpoved"].lower():
            vyhra += 10000
            otazky += 1
            vybrane_otazky.append(otazka_index)

# Zodpovězení otázky špatně
        else:
            print("\nŠpatně!")
            print("Správná odpověď je:", otazka["odpoved"])
            print("Bohužel dnes se nezadařilo. Vaše výhra činí:", vyhra, "$")
            break

# Otázky 2-9
    if otazky > 0:
        while vyhra < 90000:
            print("\nSprávně!")
            print("Pokračujme otázkou č.", otazky + 1, "za", vyhra+10000,"$!")

            otazka, otazka_index = nacteni_otazek(vybrane_otazky)

            print(otazka["otazka"])
            for moznost, odpoved in otazka["moznosti"].items():
                print(moznost + ") " + odpoved)

            user_odpoved = input("Zadejte písmeno správné odpovědi:")

            if user_odpoved.lower() == otazka["odpoved"].lower():
                vyhra += 10000
                otazky += 1
                vybrane_otazky.append(otazka_index)

            else:
                print("\nŠpatně!")
                print("Správná odpověď je:", otazka["odpoved"])
                print("Gratulujeme! Vaše výhra činí:", vyhra, "$!")
                break

# Poslední otázka
    if vyhra >= 90000 and otazky == 9:
        print("\nSprávně!")
        print("A poslední otázka za nejvyšší možnou výhru! Otázkou č.", otazky + 1, "za", vyhra+10000,"$!")

        otazka, otazka_index = nacteni_otazek(vybrane_otazky)

        print(otazka["otazka"])
        for moznost, odpoved in otazka["moznosti"].items():
            print(moznost + ") " + odpoved)

        user_odpoved = input("Zadejte písmeno správné odpovědi:")

        if user_odpoved.lower() == otazka["odpoved"].lower():
            vyhra += 10000
            otazky += 1
            vybrane_otazky.append(otazka_index)
        else:
            print("\nŠpatně!")
            print("Správná odpověď je:", otazka["odpoved"])
            print("Gratulujeme! Vaše výhra činí:", vyhra, "$!")

# Zodpovězení všech otázek správně
    if vyhra == 100000:
        print("Gratuluji! Vyhrál jste nejvyšší možnou výhru 100 000 $!")
hra()