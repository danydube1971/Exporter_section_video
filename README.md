# Exporter_section_video
Permet d'exporter une section d'une vidéo au format MP4

Le script demande d'abord à l'utilisateur de saisir le nom du fichier vidéo qu'il souhaite exporter. 
Ensuite, il demande à l'utilisateur d'entrer le temps de début et de fin de la section qu'il souhaite 
exporter en utilisant le format "hh:mm:ss.ms".

Le script utilise ensuite la bibliothèque FFMpeg pour exporter la section spécifiée de la vidéo en MP4. 
La commande FFMpeg est appelée avec les arguments suivants :

1. -i : Spécifie le fichier d'entrée, c'est-à-dire la vidéo que l'utilisateur a saisie.
2. -ss : Spécifie le temps de début de la section à exporter, qui est fourni par l'utilisateur.
3. -to : Spécifie le temps de fin de la section à exporter, également fourni par l'utilisateur.
4. -c : Spécifie le codec à utiliser pour l'exportation de la vidéo. Ici, nous utilisons l'option "copy" pour copier le flux vidéo et audio sans ré-encodage, 
ce qui est plus rapide et conserve la qualité d'origine de la vidéo.
5. output_file : Spécifie le nom du fichier de sortie pour la vidéo exportée. Dans ce cas, nous utilisons le nom du fichier d'entrée en remplaçant 
l'extension par "_export.mp4".

Enfin, le script affiche un message de confirmation une fois que l'exportation est terminée.

Testé dans Linux Mint 21

---------------

**Comment exécuter ce script ?**

1. Placer le script dans le même dossier du fichier vidéo à traiter.
2. Ouvrir un terminal
3. Taper la commande: *python3 "Exporter_section_vidéo.py"*


