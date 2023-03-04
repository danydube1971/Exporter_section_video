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

