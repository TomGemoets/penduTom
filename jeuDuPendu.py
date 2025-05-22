import random
import unicodedata

##DEFINITION DES FONCTIONS

#demande au joueur quel fichier il souhaite utiliser
def choix_du_fichier():
    choixFichier = input('Voulez-vous utilser votre fichier personnel (p) ou le fichier par défaut (d)?:')

    if(choixFichier.lower() == 'p'):
        fichierPerso = input('Rentrez le nom du fichier que vous souhaitez utiliser, attention au .txt :')
        return creer_listeMots(fichierPerso)

    elif(choixFichier.lower() == 'd'):
        return creer_listeMots("mots_pendu.txt")

def creer_listeMots(nomDuFichier): #Ouvre le fichier en lecture et créer une liste àpd de ces éléments
    with open(nomDuFichier, "r", encoding="utf-8") as f: # Lis toutes les lignes et supprime les caractères de fin de ligne
        mots = [ligne.strip() for ligne in f]
        return mots

def choix_mot_aleatoire(listeMots):
    return random.choice(listeMots)

#compter nombre de lettre dans le mot
def compter_nb_lettres(motAleatoir):
    return len(motAleatoir)

#creer une list qui aura la longueur du mot et contiendra intialement des tirets à la place des lettres
def creer_list_joueur(nbDeLettres):
    liste = ['_'] * nbDeLettres #initialisation des tirets
    return liste


#demander à l'utilisateur de rentrer une lettre à évaluer
def demander_rentrer_une_lettre():
    lettre = input('Quelle lettre voulez-vous essayer ? : ')

def retirer_accents(mot):
    return ''.join(c for c in unicodedata.normalize('NFD', mot)
                   if unicodedata.category(c) != 'Mn')

#comparer lettre entré à celles du mot, si la lettre entrée par le joueur correspond alors le tiret va etre remplacer par la lettre
#cette fonction renvoi le tableau mis à jour
def compare_lettres(motAleatoire, listeJoueur, lJoueur):
    #lettreJoueur = input('Quelle lettre voulez-vous essayer ? : ')
    for i, l in enumerate(motAleatoire):
        if(lJoueur == l):
            #print('Bien joué !')
            listeJoueur[i] = lJoueur
                    #else:
            #print(f'Dommage, plus que {nbDeVie-1} chances')

    return listeJoueur




##JEU
continuer = 'o'

while continuer == 'o' :
    # intitialisation du jeu
    nbVie = 6
    mot_aleatoire = choix_mot_aleatoire(choix_du_fichier())  # Choix aléatoire d'un mot de la liste
    mot_aleatoire = retirer_accents(mot_aleatoire)
    #print(mot_aleatoire)

    list_Du_Joueur = creer_list_joueur(compter_nb_lettres(mot_aleatoire))

    print(list_Du_Joueur) #indique le nombre de lettre du mot à trouver

    while nbVie > 1 and list_Du_Joueur != mot_aleatoire:
        lettreJoueur = input('Quelle lettre voulez-vous essayer ? : ')
        lettreJoueur = retirer_accents(lettreJoueur)
        list_Du_Joueur = compare_lettres(mot_aleatoire,list_Du_Joueur,lettreJoueur) #compare la lettre rentrée par le joueur aux lettres du mot recherhé
        print(list_Du_Joueur) #affiche état de l'avancement du joueur
        if (''.join(list_Du_Joueur) == mot_aleatoire): #si le joueur trouve toutes les lettre c'est gagné
            print("C'est gagné")
            break
        nbVie -= 1
        print(f'il vous reste {nbVie}.')

    if (nbVie == 1): #s'il reste qu'un essai, le joueur propose un mot
        proposition = input('Quel mot proposez-vous ?: ')
        proposition = retirer_accents(proposition)
        if(proposition == mot_aleatoire): #si porposition est correcte c'est gagné
            print("C'est gagné")
        else:
            print("C'est perdu")

    continuer = input('Voulez-vous continuer ? (o = oui / n = non):') #demande au joueur s'il veut rejouer ou non



