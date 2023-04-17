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
        file_content = file_content.replace('é', 'e').replace('è', 'e').replace('ê', 'e').replace('à', 'a').replace('â', 'a').replace('î', 'i').replace('ô', 'o').replace('û', 'u').replace('\n\n', '\n').replace('\n ', '\n')

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
