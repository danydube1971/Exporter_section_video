# Exporter_section_video

Ce script permet d’exporter une section d’une vidéo défini par l’utilisateur. La section choisi sera enregistré au même endroit que la vidéo source. Le script ne réencode pas la vidéo ce qui accélère grandement le traitement.

![Exporter_section_video](https://github.com/danydube1971/Exporter_section_video/assets/74633244/a33bef52-072f-4ff7-b3ca-452d01b1480a)

*Tester dans Linux Mint 21.3 sous Python 3.11*

## Prérequis

Avant d'utiliser ce script, assurez-vous que les éléments suivants sont installés sur votre système :

  • Python 3.11 ou version ultérieure : Vous pouvez télécharger Python depuis python.org.
  
  • PyQt5 : Bibliothèque pour créer des interfaces graphiques. Installez-le en utilisant la commande pip install PyQt5.
  
  • ffmpeg : Outil de traitement vidéo. Vous pouvez le télécharger et l'installer depuis ffmpeg.org.

## Installation

   1. Téléchargez le script : Téléchargez le fichier Exporter_section_vidéo_Qt5.py sur votre ordinateur.
   2. Installez les dépendances :
        ◦ Ouvrez une fenêtre de terminal ou de commande.
        ◦ Exécutez les commandes suivantes pour installer les bibliothèques nécessaires :
       `pip install PyQt5`
      
       `sudo apt-get install ffmpeg`
      
   3. Placez le script dans un répertoire approprié : Placez Exporter_section_vidéo_Qt5.py dans un répertoire où vous souhaitez l'exécuter.

## Lancer l'application

   1. Ouvrez une fenêtre de terminal ou de commande.
   2. Naviguez jusqu'au répertoire contenant le script :
       cd /chemin/vers/le/répertoire
   3. Exécutez le script :
       `python Exporter_section_vidéo_Qt5.py`
   4. L'application s'ouvre : Une fenêtre intitulée "Exportateur de Section Vidéo" s'affiche.
    
## Sélectionner un fichier vidéo
    
  1. Cliquez sur le bouton "Choisir un fichier vidéo" : Une boîte de dialogue de sélection de fichiers apparaît.
  2. Choisissez le fichier vidéo à traiter : Sélectionnez un fichier avec une extension .mkv, .mp4, .avi, ou .webm.
  3. Durée de la vidéo affichée : L'application extrait la durée de la vidéo et l'affiche sous l'étiquette "Durée de la vidéo :".

## Définir la section vidéo à exporter

   1. Entrez le temps de début :
        ◦ Dans le champ "Début de la vidéo: HH:MM
          ", entrez le temps de début de la section que vous souhaitez extraire.
   2. Entrez le temps de fin :
        ◦ Dans le champ "Fin de la vidéo: HH:MM
          ", entrez le temps de fin de la section que vous souhaitez extraire.
        ◦ Assurez-vous que le temps de fin est supérieur au temps de début et ne dépasse pas la durée totale de la vidéo.

## Exporter la section vidéo

   1. Cliquez sur le bouton "Exporter la section vidéo" : L'application commence à traiter la vidéo.
   2. Message de succès ou d'erreur :
        ◦ Si l'exportation est réussie, un message de succès s'affiche avec le chemin du fichier exporté.
        ◦ En cas d'erreur, un message détaillé s'affiche pour vous aider à identifier le problème.


