import os

# Chemin du répertoire à traiter
folder_path = "Questions/"
# effacer le terminal
os.system('cls' if os.name == 'nt' else 'clear')

# Boucle sur tous les fichiers du répertoire
for filename in os.listdir(folder_path):
    # Vérifie si le fichier est un fichier texte
    if filename.endswith(".txt"):
        # Ouvre le fichier avec l'encodage UTF-8 et lit son contenu
        with open(os.path.join(folder_path, filename), 'r', encoding='utf-8') as file:
            file_content = file.read()

        # Remplace les caractères spéciaux et supprime les lignes vides
        file_content = file_content.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('É', 'E').replace('À', 'A').replace('à', 'a').replace('â', 'a').replace('î', 'i').replace('ô', 'o').replace('ù','u').replace('û', 'u').replace('\n\n', '\n').replace('\n ', '\n')

        # Récupère les numéros de question et les modifie
        lines = file_content.split('\n')
        num = 1
        for i in range(len(lines)):
            if lines[i].startswith('Question '):
                lines[i] = f'Question {num}: {lines[i].split(":", 1)[1].strip()}'
                num += 1

        # Recompose le texte modifié et le réécrit dans le fichier
        file_content = '\n'.join(lines)
        with open(os.path.join(folder_path, filename), 'w', encoding='utf-8') as file:
            file.write(file_content)

        print(f"Le fichier {filename} a été modifié avec succès.")

# Pour formater le fichier de texte en compactant les lignes pour chatGPT

def group_lines(file_path, target_words_per_line):
    # Ouvrir le fichier en mode lecture
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    # Ouvrir le fichier en mode écriture
    with open(file_path, 'w') as f:
        words = []
        for i, line in enumerate(lines):
            if i >= 11: # Commencer à la ligne 12
                # Ajouter les mots de chaque ligne à une liste
                words += line.split()
                if len(words) >= target_words_per_line:
                    # Si la liste atteint le nombre cible de mots, écrire une nouvelle ligne avec ces mots
                    f.write(" ".join(words[:target_words_per_line]) + "\n")
                    # Supprimer ces mots de la liste pour continuer avec le reste des mots
                    words = words[target_words_per_line:]
            
            # Écrire les lignes avant la ligne 12 sans modification
            else:
                f.write(line)
        
        # Écrire une dernière ligne avec les mots restants (s'il y en a)
        if words:
            f.write(" ".join(words) + "\n")
    
    print("Les lignes ont été regroupées avec succès !")

# Exemple d'utilisation
file_path = "QCMGPT.txt"
target_words_per_line = 200
group_lines(file_path, target_words_per_line)
