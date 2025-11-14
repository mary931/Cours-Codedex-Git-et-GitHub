import random

Nombre = random.randint(1, 100)
Nombre_essais = 1

Choix = int(input('Devine le nombre entre 1 et 100: '))

while Choix != Nombre:

    Choix = int(input('Devine le nombre entre 1 et 100: '))
    Nombre_essais += 1

    if Choix < Nombre:
        print('Plus grand')
    elif Choix > Nombre:
        print('plus petit')
    
   
print(f"Félicitations tu as réussis ! Tu as deviné le bon nombre au bout de {Nombre_essais} coups !")
