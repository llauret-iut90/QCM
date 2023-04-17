import os
import colorama
import random
from colorama import Fore, Style

# initialisation de la bibliothèque colorama
colorama.init()
# effacer le terminal
os.system('cls' if os.name == 'nt' else 'clear')

# initialisation des variables
num_questions = 1
lines = []

print('''
                        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
                        █░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
                        █░░║║║╠─║─║─║║║║║╠─░░█
                        █░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█
                        ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
''')
print(Style.BRIGHT + Fore.RED + "                        Bienvenue dans le QCM !" + Style.RESET_ALL)

while True:
    cours = input("Choissisez le cours :" + Fore.GREEN + "1 [GestionProjet]"+ Style.RESET_ALL + Fore.RED + "2 [QualiteDev]" + Style.RESET_ALL + Fore.BLUE + "3 [ProgObj]" + Style.RESET_ALL + " : ")
    if cours in ['1', '2','3']:
        break
    else:
        print(Fore.RED + '''Veuillez entrer un cours valide : 
    1 pour GestionProjet 
    2 pour QualiteDev
    3 pour ProgObj. ''' + Style.RESET_ALL)

if cours == "1":
    # ouverture du fichier
    with open("Questions/GestionProjet.txt", "r") as file:
        # lecture des lignes
        lines = file.readlines()
        # calcul du nombre de questions dans le fichier
        num_questions = len(lines) // 6
elif cours == "2":
    # ouverture du fichier
    with open("Questions/QualiteDev.txt", "r") as file:
        # lecture des lignes
        lines = file.readlines()
        # calcul du nombre de questions dans le fichier
        num_questions = len(lines) // 6
elif cours == "3":
    # ouverture du fichier
    with open("Questions/ProgObj.txt", "r") as file:
        # lecture des lignes
        lines = file.readlines()
        # calcul du nombre de questions dans le fichier
        num_questions = len(lines) // 6
else:
    print(Fore.RED + '''Veuillez entrer un cours valide : 
    1 pour GestionProjet 
    2 pour QualiteDev 
    3 pour ProgObj. ''' + Style.RESET_ALL)

# initialisation du score
score = 0
question_restante = 0
# choix du mode de sélection des questions
while True:
    mode = input("Voulez-vous sélectionner les questions de manière aléatoire ? (o/n) : ")
    if mode.lower() == "o":
        # choix aléatoire des indices des blocs de questions
        n = int(input(f"Combien de questions voulez-vous ? (max {num_questions}) "))
        # vérification que le nombre de questions demandé ne dépasse pas le nombre de questions disponibles
        if n > num_questions:
            print(Fore.RED + f"Le nombre de questions demandé dépasse le nombre de questions disponibles ({num_questions})." + Style.RESET_ALL)
            continue
        block_indices = random.sample(range(0, num_questions), n)
        questions_indices = [i*6 for i in block_indices]
        break
    elif mode.lower() == "n":
        # sélection des n premiers blocs de questions du fichier
        n = int(input(f"Combien de questions voulez-vous ? (max {num_questions}) "))
        # vérification que le nombre de questions demandé ne dépasse pas le nombre de questions disponibles
        if n > num_questions:
            print(Fore.RED + f"Le nombre de questions demandé dépasse le nombre de questions disponibles ({num_questions})." + Style.RESET_ALL)
            continue
        block_indices = range(0, n)
        questions_indices = [i*6 for i in block_indices]
        break
    else:
        print(Fore.RED + "Veuillez entrer une réponse valide : o pour oui, n pour non." + Style.RESET_ALL)

# boucle sur chaque bloc de questions sélectionné
for i in block_indices:
    # affichage de la question en gras et en couleur
    print(Style.BRIGHT + Fore.BLUE + lines[i*6].strip() + Style.RESET_ALL)
    # affichage des options de réponse
    for j in range(i*6+1, i*6+5):
        print(lines[j].strip())
    # saisie de la réponse de l'utilisateur
    while True:
        answer = input("Réponse: ")
        if answer.upper() in ['A', 'B', 'C', 'D']:
            break
        else:
            print(Fore.RED + "Veuillez entrer une réponse valide : A, B, C ou D" + Style.RESET_ALL)
    answer_index = ord(answer.upper()) - ord('A')
    # récupération de l'index de la bonne réponse
    correct_answer_index = ord(lines[i*6+5].split(":")[1].strip()) - ord('A')
    # vérification de la réponse
    if answer_index == correct_answer_index:
        question_restante = question_restante + 1
        if n-question_restante == 0:
            print(Fore.GREEN + "Bonne réponse !" + Style.RESET_ALL)
        else:
            print(Fore.GREEN + "Bonne réponse !" + Style.RESET_ALL + Fore.LIGHTYELLOW_EX +' [il vous reste encore ' + str(n-question_restante) + ' questions]' + Style.RESET_ALL)
        score += 1
    else:
        question_restante = question_restante + 1
        if n-question_restante == 0:
            print(Fore.RED + f"Mauvaise réponse... La bonne réponse était : {lines[i*6+correct_answer_index+1].strip()}" + Style.RESET_ALL)
        else:
            print(Fore.RED + f"Mauvaise réponse... La bonne réponse était : {lines[i*6+correct_answer_index+1].strip()}" + Style.RESET_ALL+  Fore.LIGHTYELLOW_EX +' [il vous reste encore ' + str(n-question_restante) + ' questions]' + Style.RESET_ALL)
        


# affichage du score final

if score == n:
    print(Fore.GREEN + f"Félicitations ! OMEDETO ! ❤❤❤❤❤❤❤❤❤" + Style.RESET_ALL)
elif score <= n/5:
    print(Fore.RED + f"T'es vraiment mauvais : {(score/n)*100}%" + Style.RESET_ALL)
    print('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡛⠛⠷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠙⠻⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠀⠀⠀⠀⠀⠀⠈⣹⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀⠀⣠⡴⠞⠉⠈⠻⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣿⡧⠤⠤⠶⠖⠋⠉⠀⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⠞⠉⠀⠉⠙⠻⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⢀⣠⡴⠞⠉⠀⢀⣀⣀⣀⠀⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣿⣆⣴⠟⠉⠉⠉⠛⢶⡖⠛⠉⠁⠀⠀⢠⡾⠋⠉⠈⠉⠻⣦⣰⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⣤⣾⠟⠋⡿⠁⢀⣾⣿⣷⣄⠈⢿⡀⠀⠀⠀⢠⡟⠀⢠⣾⣿⣷⡄⠘⣿⠉⠛⢿⣦⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢠⣿⠏⠀⠀⢸⡇⠀⢸⣿⣿⣿⣿⠀⢸⡇⠀⠀⠀⢸⡇⠀⣿⣿⣿⣿⣧⠀⢹⡇⠀⠀⠙⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⡏⠀⠀⠀⠘⣧⠀⠘⣿⣿⣿⡟⠀⣸⠇⠀⣀⣤⢾⣇⠀⠹⣿⣿⣿⠇⠀⣾⠁⠀⠀⠀⢸⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣷⠀⠀⠀⠀⠹⣧⡀⠈⠉⠁⢀⣴⠿⠞⠋⠉⠀⠀⠻⣦⡀⠈⠉⠁⣠⡾⠃⠀⠀⠀⠀⣾⡏⠀⠀⠀⠀
⠀⠀⢀⣠⣶⠿⠛⠛⠛⠛⠛⠛⠉⠙⠛⠒⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠚⠛⠉⠀⠀⠀⠀⢀⡼⠿⢷⣦⣄⠀⠀
⠀⣠⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣟⠛⠛⠒⠶⠶⠶⠶⠶⠶⠶⠖⠚⠛⢛⡷⠀⠀⠀⣀⡴⠋⠀⠀⠀⠈⠻⣷⡄
⢰⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡶⠛⢁⣠⡴⠞⠋⠀⠀⠀⠀⠀⠀⠀⠘⣿
⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠶⠶⠦⠶⠶⣚⣫⡥⠶⠚⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿
⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠴⠖⠚⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣴⡿⠃
⠀⠈⠛⣷⣦⣤⣤⣤⣤⣤⣤⣶⡶⠾⠿⠟⠿⠿⠿⠶⣶⣶⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣶⠶⠿⠛⠉⠀⠀
    ''')
elif score == 0:
    print(Fore.RED + "Arrête de jouer" + Style.RESET_ALL)
    print('''
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████
██████████▄▄▄▄▄▄▄██████████
███████████████████████████
    ''')
else:
    print(Fore.YELLOW + f"Votre score est de {score} sur {n} : {round(((score/n)*100),2)}%" + Style.RESET_ALL)