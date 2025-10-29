def pgcd(a, b):
    print(f"Calcul du PGCD de {a} et {b} :\n")
    etape = 1
    while b != 0:
        q = a // b   # quotient
        r = a % b    # reste
        print(f"Étape {etape} : {a} = {b} × {q} + {r}")
        a, b = b, r
        etape += 1
    print(f"\nLe PGCD est {a}")


x = int(input("Entrez le premier nombre : "))
y = int(input("Entrez le deuxième nombre : "))

pgcd(x, y)