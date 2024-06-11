import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import QTime, QThread, pyqtSignal

class DurationExtractor(QThread):
    duration_extracted = pyqtSignal(str)
    
    def __init__(self, file_path):
        super().__init__()
        self.file_path = file_path

    def run(self):
        duration = self.extract_duration(self.file_path)
        self.duration_extracted.emit(duration)

    def extract_duration(self, file_path):
        try:
            result = subprocess.run(
                ['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', file_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True
            )
            duration_seconds = float(result.stdout.strip())
            duration = QTime(0, 0, 0).addSecs(int(duration_seconds))
            return duration.toString("HH:mm:ss")
        except Exception as e:
            print(f'Erreur lors de l\'extraction de la durée : {e}')
            return '00:00:00'

class VideoExporter(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.video_duration = QTime(0, 0, 0)  # Initialisation de la durée de la vidéo
        
    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel('Sélectionnez un fichier vidéo :', self)
        layout.addWidget(self.label)

        self.file_path_input = QLineEdit(self)
        self.file_path_input.setReadOnly(True)
        layout.addWidget(self.file_path_input)

        self.select_file_button = QPushButton('Choisir un fichier vidéo', self)
        self.select_file_button.clicked.connect(self.select_file)
        layout.addWidget(self.select_file_button)

        self.duration_label = QLabel('Durée de la vidéo : ', self)
        layout.addWidget(self.duration_label)

        self.start_time_label = QLabel('Début de la vidéo: HH:MM:SS', self)
        layout.addWidget(self.start_time_label)

        self.start_time_input = QLineEdit(self)
        layout.addWidget(self.start_time_input)

        self.end_time_label = QLabel('Fin de la vidéo: HH:MM:SS', self)
        layout.addWidget(self.end_time_label)

        self.end_time_input = QLineEdit(self)
        layout.addWidget(self.end_time_input)

        self.export_button = QPushButton('Exporter la section vidéo', self)
        self.export_button.clicked.connect(self.export_video)
        layout.addWidget(self.export_button)
        
        self.setLayout(layout)
        
        self.setWindowTitle('Exportateur de Section Vidéo')
        self.setGeometry(300, 300, 400, 350)
        
    def select_file(self):
        file_dialog = QFileDialog(self)
        file_path, _ = file_dialog.getOpenFileName(
            self, 
            'Ouvrir fichier vidéo', 
            '', 
            'Vidéo (*.mkv *.mp4 *.avi *.webm)'
        )
        if file_path:
            self.file_path_input.setText(file_path)
            self.duration_label.setText('Extraction de la durée en cours...')
            
            self.duration_extractor = DurationExtractor(file_path)
            self.duration_extractor.duration_extracted.connect(self.update_duration_label)
            self.duration_extractor.start()

    def update_duration_label(self, duration):
        self.duration_label.setText(f'Durée de la vidéo : {duration}')
        self.video_duration = QTime.fromString(duration, "HH:mm:ss")
    
    def export_video(self):
        file_path = self.file_path_input.text()
        start_time = self.start_time_input.text()
        end_time = self.end_time_input.text()

        if file_path and start_time and end_time:
            start_time_obj = QTime.fromString(start_time, "HH:mm:ss")
            end_time_obj = QTime.fromString(end_time, "HH:mm:ss")

            if not start_time_obj.isValid() or not end_time_obj.isValid():
                self.show_error_message("Les temps de début ou de fin sont invalides. Veuillez entrer des valeurs au format HH:MM:SS.")
                return

            if start_time_obj >= end_time_obj:
                self.show_error_message("Le temps entré dans 'Fin de la vidéo' doit être plus grand que 'Début de la vidéo'.")
                return

            if end_time_obj > self.video_duration:
                self.show_error_message("Le temps entré dans 'Fin de la vidéo' ne doit pas dépasser la 'Durée de la vidéo'.")
                return

            section_duration = QTime(0, 0, 0).addSecs(start_time_obj.secsTo(end_time_obj)).toString("HH:mm:ss")
            file_extension = os.path.splitext(file_path)[1]
            file_name = os.path.basename(file_path)
            base_name = os.path.splitext(file_name)[0]
            output_file_name = f'{base_name}_section_video_durée_{section_duration}{file_extension}'
            output_file_path = os.path.join(os.path.dirname(file_path), output_file_name)
            
            command = [
                'ffmpeg',
                '-i', file_path,
                '-ss', start_time,
                '-to', end_time,
                '-c', 'copy',  # Copie les codecs sans réencodage
                output_file_path
            ]
            
            try:
                subprocess.run(command, check=True)
                self.show_success_message(f'Vidéo exportée avec succès ! Fichier exporté : {output_file_path}')
            except subprocess.CalledProcessError as e:
                self.show_error_message(f'Erreur lors de l\'exportation de la vidéo : {e}')
        else:
            self.show_error_message("Veuillez sélectionner un fichier et remplir les champs de temps.")
    
    def show_error_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Critical)
        msg_box.setWindowTitle("Erreur")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

    def show_success_message(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Information)
        msg_box.setWindowTitle("Succès")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoExporter()
    ex.show()
    sys.exit(app.exec_())

