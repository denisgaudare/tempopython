### 📅 **Modules et fonctions les plus utiles pour la gestion des dates et heures en Python**  

#### 1️⃣ **Module `datetime`** (Le plus utilisé pour manipuler les dates et heures)
```python
from datetime import datetime, date, time, timedelta
```
- `datetime.now()` → Récupérer la date et l'heure actuelles
- `datetime.today()` → Similaire à `now()`, sans timezone
- `datetime.strptime(date_string, format)` → Convertir une chaîne en `datetime`
- `datetime.strftime(format)` → Convertir un `datetime` en chaîne formatée
- `datetime.utcfromtimestamp(timestamp)` → Convertir un timestamp en UTC  
- `timedelta(days=1, hours=3)` → Manipuler des durées  

Exemple :
```python
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formatage personnalisé
```

---

#### 2️⃣ **Module `time`** (Pour travailler avec des timestamps et des pauses)
```python
import time
```
- `time.time()` → Récupérer le timestamp actuel (secondes écoulées depuis 1970)
- `time.sleep(seconds)` → Mettre le programme en pause
- `time.strftime(format, time.localtime())` → Convertir un timestamp en date lisible
- `time.gmtime()` → Récupérer l'heure UTC

Exemple :
```python
print(time.time())  # Timestamp actuel
time.sleep(2)  # Pause de 2 secondes
```

---

#### 3️⃣ **Module `calendar`** (Pour manipuler des calendriers)
```python
import calendar
```
- `calendar.month(year, month)` → Afficher un mois sous forme de texte
- `calendar.isleap(year)` → Vérifier si une année est bissextile
- `calendar.weekday(year, month, day)` → Récupérer le jour de la semaine (0=lundi, 6=dimanche)

Exemple :
```python
print(calendar.month(2025, 3))  # Affiche le calendrier de mars 2025
```

---

#### 4️⃣ **Module `zoneinfo`** (Gestion des fuseaux horaires - depuis Python 3.9)
```python
from datetime import datetime
from zoneinfo import ZoneInfo
```
- `ZoneInfo("Europe/Paris")` → Récupérer un fuseau horaire
- `datetime.now(ZoneInfo("UTC"))` → Récupérer l'heure actuelle en UTC

Exemple :
```python
paris_time = datetime.now(ZoneInfo("Europe/Paris"))
print(paris_time)
```

---

#### 5️⃣ **Module `dateutil`** (Extension puissante - nécessite `pip install python-dateutil`)
```python
from dateutil import parser, relativedelta
```
- `parser.parse(date_string)` → Convertir automatiquement une date en `datetime`
- `relativedelta(months=+1, days=-5)` → Manipuler les dates plus facilement qu’avec `timedelta`

Exemple :
```python
from dateutil.parser import parse
dt = parse("12 March 2025")
print(dt)
```

---

💡 **Conclusion :**
- **`datetime`** → Pour manipuler les dates et heures
- **`time`** → Pour travailler avec des timestamps et temporisations
- **`calendar`** → Pour gérer des calendriers et vérifier les jours
- **`zoneinfo`** → Pour gérer les fuseaux horaires (Python 3.9+)
- **`dateutil`** → Pour des manipulations avancées de dates (externe)