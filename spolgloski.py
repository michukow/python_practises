samogloski = "aeiouyąęó"
spogloski = "wrtpsdfghjklzbnmćśńżźłqxv"
cyfry = "0123456789"
spacja = " "

def litery(tekst):
    l_samogloski = 0
    l_spolgloski = 0
    l_cyfry = 0
    l_spacja = 0
    inne = 0

    for litera in tekst:
        znak = litera.lower()
        if znak in samogloski:
            l_samogloski += 1
        elif znak in spogloski:
            l_spolgloski += 1
        elif znak in cyfry:
            l_cyfry += 1
        elif litera in spacja:
            l_spacja += 1
        else:
            inne += 1

    print(f"Liczba samogłosek: {l_samogloski}")
    print(f"Liczba spółgłosek: {l_spolgloski}")
    print(f"Liczba cyfr: {l_cyfry}")
    print(f"Liczba spacji: {l_spacja}")
    print(f"Liczba innych znaków: {inne}")

litery("Ala ma kota, a kot ma Alę!")
