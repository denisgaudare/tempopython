# Autres fonctions intéressantes qu'on peut utiliser :
import ctypes
from ctypes import wintypes
import time

import _locale
ENCODING = _locale.getencoding()

# Charger la DLL
winmm = ctypes.WinDLL('winmm')
### 🔉 1. `waveOutGetNumDevs` – connaître le nombre de sorties audio disponibles
winmm.waveOutGetNumDevs.argtypes = []
winmm.waveOutGetNumDevs.restype = wintypes.UINT

nb_devices = winmm.waveOutGetNumDevs()
print(f"Nombre de sorties audio disponibles : {nb_devices}")

### 🎛️ 2. `midiOutGetNumDevs` – connaître le nombre de sorties MIDI disponibles
winmm.midiOutGetNumDevs.argtypes = []
winmm.midiOutGetNumDevs.restype = wintypes.UINT

nb_midi = winmm.midiOutGetNumDevs()
print(f"Nombre de sorties MIDI disponibles : {nb_midi}")

### 🕒 3. `timeBeginPeriod` et `timeEndPeriod` – changer la résolution du timer système

# timeBeginPeriod(UINT uPeriod)
winmm.timeBeginPeriod.argtypes = [wintypes.UINT]
winmm.timeBeginPeriod.restype = wintypes.UINT

# timeEndPeriod(UINT uPeriod)
winmm.timeEndPeriod.argtypes = [wintypes.UINT]
winmm.timeEndPeriod.restype = wintypes.UINT

# Demander une résolution de 1ms
result = winmm.timeBeginPeriod(1)
print(f"Résolution du timer système (begin) : {result}")

# ... tu fais tes opérations ici (comme un sleep ou un timer précis)
time.sleep(0.01)  # Exemple

# Rétablir la résolution normale
result = winmm.timeEndPeriod(1)
print(f"Résolution du timer système (end) : {result}")

### 🧪 4. `mciGetErrorStringA` – pour décoder les erreurs de MCI
# mciSendStringA : parfois un code d’erreur.
# Voici comment le lire :

winmm.mciGetErrorStringA.argtypes = [wintypes.DWORD, wintypes.LPSTR, wintypes.UINT]
winmm.mciGetErrorStringA.restype = wintypes.BOOL

def get_mci_error(err_code):
    buffer = ctypes.create_string_buffer(256)
    success = winmm.mciGetErrorStringA(err_code, buffer, 256)
    return buffer.value.decode(encoding=ENCODING) if success else b"Erreur inconnue"

# Exemple : code d'erreur bidon
err_msg = get_mci_error(274)  # Par exemple
print(f"Erreur MCI 274 : {err_msg}")
