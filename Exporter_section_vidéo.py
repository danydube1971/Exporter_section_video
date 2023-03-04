""" Vous devez installer ffmpeg (apt install ffmpeg) en premier lieu

Le script demande d'abord à l'utilisateur de saisir le nom du fichier vidéo qu'il souhaite exporter. Ensuite, il demande à 
l'utilisateur d'entrer le temps de début et de fin de la section qu'il souhaite exporter en utilisant le format "hh:mm:ss.ms".

Le script utilise ensuite la bibliothèque FFMpeg pour exporter la section spécifiée de la vidéo en MP4. La commande FFMpeg est 
appelée avec les arguments suivants :

-i : Spécifie le fichier d'entrée, c'est-à-dire la vidéo que l'utilisateur a saisie.
-ss : Spécifie le temps de début de la section à exporter, qui est fourni par l'utilisateur.
-to : Spécifie le temps de fin de la section à exporter, également fourni par l'utilisateur.
-c : Spécifie le codec à utiliser pour l'exportation de la vidéo. Ici, nous utilisons l'option "copy" pour copier le flux vidéo et audio 
sans ré-encodage, ce qui est plus rapide et conserve la qualité d'origine de la vidéo.
output_file : Spécifie le nom du fichier de sortie pour la vidéo exportée. Dans ce cas, nous utilisons le nom du fichier d'entrée en 
remplaçant l'extension par "_export.mp4".

Enfin, le script affiche un message de confirmation une fois que l'exportation est terminée."""

import subprocess

# Demander à l'utilisateur le nom du fichier vidéo
input_file = input("Entrez le nom du fichier vidéo : ")

# Demander à l'utilisateur les temps de début et de fin de la section
start_time = input("Entrez le temps de début de la section (hh:mm:ss.ms) : ")
end_time = input("Entrez le temps de fin de la section (hh:mm:ss.ms) : ")

# Utiliser FFMpeg pour exporter la section en MP4
output_file = input_file.split(".")[0] + "_export.mp4"  # Nom du fichier de sortie
command = ["ffmpeg", "-i", input_file, "-ss", start_time, "-to", end_time, "-c", "copy", output_file]
subprocess.run(command)

print("La section de la vidéo a été exportée en MP4 avec succès !")

