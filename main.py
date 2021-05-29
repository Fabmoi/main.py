

def afficher_informations_personne(nom, age, taille):
    print()
    print("Vous vous appelez " + nom + ", vous avez " + str(age) + " ans et vous mesurez " + str(taille) + " cm.")
    print(f"Vous vous appelez {nom}, vous avez {age} ans et vous mesurez {taille} cm;")
    print("Vous vous appelez %s, vous avez %s ans et vous mesurez %s cm." % (nom, age, taille))
    print("L'an prochain, vous aurez " + str(age + 1) + " ans.")
    print(f"L'an prochain, vous aurez {age + 1} ans.")
    print("L'an prochain, vous aurez %s ans." % (age + 1))
    print("Dans 2 ans, vous aurez " + str(age + 2) + " ans.")
    print(f"Dans 2 ans, vous aurez {age + 2} ans.")
    print("Dans 2 ans, vous aurez %s ans." % (age + 2))
    print("L'an passé, vous aviez " + str(age - 1) + " ans.")
    print(f"L'an passé, vous aviez {age - 1} ans.")
    print("L'an passé, vous aviez %s ans." % (age - 1))


    if age == 1 or age == 2:
        print("Vous êtes un bébé très avancé intellectuellement pour savoir utiliser un PC")
    elif age <= 10:
        print("Vous êtes un enfant")
    elif age >= 60:
        print("Vous êtes un sénior")
    elif age == 17:
        print("Vous êtes presque majeur")
    elif age >= 12 and age < 18:
        print("Vous êtes adolescent")
    elif age == 18:
        print("Vous êtes tout juste majeur : Félicitations")
    elif age >= 18:
        print("Vous êtes majeur")
    else:
        print("Vous êtes mineur")


    if not taille == 0:
        print("Votre taille est de : " + str(taille) + " cm ")



def demander_nom():
    reponse_nom = ""
    while reponse_nom == "":
        reponse_nom = input("Quel est votre nom ? ")
    return reponse_nom


def demander_age(nom_personne):
    age_int = 0
    while age_int == 0:
        age_str = input(nom_personne + " Quel est votre âge ? ")
        try:
            age_int = int(age_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour l'âge")
    return age_int


def demander_taille(nom_personne):
    taille_int = 0
    while taille_int == 0:
        taille_str = input("Quelle est votre taille en cm ? ")
        try:
            taille_int = int(taille_str)
        except:
            print("ERREUR: Vous devez rentrer un nombre pour la taille")
    return taille_int


# nom1 = demander_nom()
# nom2 = demander_nom()

# age1 = demander_age(nom1)
# age2 = demander_age(nom2)

# taille1 = demander_taille(nom1)
# taille2 = demander_taille(nom2)

# afficher_informations_personne(nom1, age1)
# afficher_informations_personne(nom2, age2)

NB_PERSONNES = 1

for i in range(0, NB_PERSONNES):
    nom = "personne" + str(i+1)
    age = demander_age(nom)
    taille = demander_taille(nom)
    afficher_informations_personne(nom, age, taille)

print("""
    ICI
    UN PRINT
    SUR PLUSIEURS
    LIGNES
""")

