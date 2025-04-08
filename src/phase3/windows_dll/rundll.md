** Fonctions courantes de `winmm.dll`** pour aller un peu plus loin, toujours en gardant ça simple. Voici ce qu’on peut faire :

### 🧰 Fonctions qu’on va utiliser :
1. `PlaySoundA` — lire un son `.wav`
2. `mciSendStringA` — pour **contrôler les médias plus avancés** (lecture, pause, stop de fichiers audio/vidéo)
3. `timeGetTime` — pour **récupérer le temps écoulé** depuis le démarrage de Windows

---
### ✅ Script complet avec plusieurs fonctions de `winmm.dll`

```python
import ctypes
from ctypes import wintypes
import time

# Charger la DLL
winmm = ctypes.WinDLL('winmm')

# === PlaySoundA ===
winmm.PlaySoundA.argtypes = [wintypes.LPCSTR, wintypes.HMODULE, wintypes.DWORD]
winmm.PlaySoundA.restype = wintypes.BOOL

# === mciSendStringA ===
winmm.mciSendStringA.argtypes = [wintypes.LPCSTR, wintypes.LPSTR, wintypes.UINT, wintypes.HANDLE]
winmm.mciSendStringA.restype = wintypes.DWORD

# === timeGetTime ===
winmm.timeGetTime.argtypes = []
winmm.timeGetTime.restype = wintypes.DWORD

# === Jouer un fichier WAV simple ===
SND_FILENAME = 0x00020000
SND_ASYNC = 0x0001
print("Lecture simple de WAV avec PlaySound...")
winmm.PlaySoundA(b"test.wav", None, SND_FILENAME | SND_ASYNC)
time.sleep(2)

# === Utiliser mciSendStringA pour jouer un MP3 ===
# Ça permet plus de contrôle (pause, resume, stop)
print("Lecture MP3 avec mciSendString...")
winmm.mciSendStringA(b"open \"test.mp3\" type mpegvideo alias mymusic", None, 0, None)
winmm.mciSendStringA(b"play mymusic", None, 0, None)
time.sleep(5)
winmm.mciSendStringA(b"pause mymusic", None, 0, None)
print("Musique en pause.")
time.sleep(2)
winmm.mciSendStringA(b"resume mymusic", None, 0, None)
print("Musique relancée.")
time.sleep(3)
winmm.mciSendStringA(b"stop mymusic", None, 0, None)
winmm.mciSendStringA(b"close mymusic", None, 0, None)
print("Lecture terminée.")

# === Temps écoulé depuis le démarrage de Windows ===
ms = winmm.timeGetTime()
print(f"Temps depuis le démarrage de Windows : {ms} ms")
```

---

### 🔊 Fichiers requis :
- `test.wav` (pour `PlaySoundA`)
- `test.mp3` (pour `mciSendStringA`) – oui, on peut lire des `.mp3` avec MCI !

---

### 🧠 Bonus : ce que tu peux ajouter ensuite

- Interface graphique (Tkinter) pour faire **Play / Pause / Stop**
- Lecture de **vidéo** avec `mciSendStringA` (via `type avivideo`)
- Chronomètre précis avec `timeGetTime`
- Utilisation de buffers pour **midi, waveIn/waveOut**, etc.

---