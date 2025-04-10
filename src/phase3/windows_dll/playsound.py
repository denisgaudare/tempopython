import sys
import ctypes
from ctypes import wintypes
from PySide6.QtWidgets import QApplication, QPushButton, QFileDialog, QWidget, QVBoxLayout, QLabel

# Charger winmm.dll pour la lecture de son
winmm = ctypes.WinDLL("winmm")
PlaySound = winmm.PlaySoundW
PlaySound.argtypes = [wintypes.LPCWSTR, wintypes.HMODULE, wintypes.DWORD]
PlaySound.restype = wintypes.BOOL

# Flags de PlaySound
SND_FILENAME = 0x00020000
SND_ASYNC = 0x0001

def play_wav_file(path):
    PlaySound(path, None, SND_FILENAME | SND_ASYNC)

# Interface PySide6
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Lecteur WAV via DLL Windows")

layout = QVBoxLayout()
label = QLabel("Choisissez un fichier .wav à jouer")
btn = QPushButton("Sélectionner un fichier WAV")

def choose_file():
    file, _ = QFileDialog.getOpenFileName(None, "Choisir un fichier WAV", "", "Fichiers WAV (*.wav)")
    if file:
        label.setText(f"Lecture de : {file}")
        play_wav_file(file)

btn.clicked.connect(choose_file)
layout.addWidget(label)
layout.addWidget(btn)

window.setLayout(layout)
window.show()
sys.exit(app.exec())
