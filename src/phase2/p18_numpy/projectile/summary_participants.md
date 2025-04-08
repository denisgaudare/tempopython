### **Projet : Simulation du Mouvement d'un Projectile en 2D**

#### Objectif :
1. Simuler le mouvement d'un projectile (par exemple, un boulet de canon) dans un champ gravitationnel avec une vitesse initiale et un angle donnés.
2. Calculer les trajectoires et analyser des propriétés comme la portée, la hauteur maximale, le temps de vol, etc.
3. Implémenter des méthodes numériques pour résoudre les équations du mouvement.

#### Formules physiques de base :
Le mouvement du projectile est décrit par les équations suivantes (en négligeant la résistance de l'air) :
- x(t) = v0  * cos(theta) * t
- y(t) = v0  * sin(theta) * t - g/2 * t^2
  
Où :
- v0 : la vitesse initiale,
- theta : l'angle de lancement,
- g : l'accélération due à la gravité 
     (approximativement 9.81m/sec^2),
- t : le temps.

### Étapes du projet :

#### 1. **Trpuver la vitesse initiale et l'angle (Fonction simple)**

Commençons par définir une vitesse initiale v0 
et un angle de lancement theta.

```python
import numpy as np

# Constantes physiques
g = 9.81  # accélération due à la gravité (m/s^2)

# Paramètres du projectile
v0 = 20  # vitesse initiale en m/s
theta = 45  # angle de lancement en degrés

# Conversion de l'angle en radians
theta_rad = # TODO

print(f"Vitesse initiale: {v0} m/s")
print(f"Angle de lancement: {theta}° ({theta_rad} rad)")
```

#### 2. **Calcul de la trajectoire (Fonction simple)**

Simulons le mouvement du projectile dans le temps. Nous calculerons les positions \( x(t) \) et \( y(t) \) en utilisant les équations de mouvement.

```python
def projectile_trajectory(v0, theta, g, t_max, dt):
    # Nombre d'itérations en fonction du temps maximum et du pas de temps
    t = # TODO
    
    # Calcul des positions x et y en fonction du temps
    # TODO
    
    return t, x, y

# Paramètres de simulation
t_max = 2 * v0 * np.sin(theta_rad) / g  # Temps maximum pour que le projectile touche le sol
dt = 0.01  # Pas de temps

# Calcul de la trajectoire
t, x, y = projectile_trajectory(v0, theta_rad, g, t_max, dt)

# Affichage des résultats
import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Trajectoire du projectile")
plt.title("Trajectoire d'un projectile")
plt.xlabel("Distance (m)")
plt.ylabel("Hauteur (m)")
plt.grid(True)
plt.legend()
plt.show()
```

#### 3. **Optimisation avec des pas de temps plus fins (Fonction avancée)**

On peut améliorer la précision de la simulation 
en ajustant le pas de temps et en 
utilisant l'intégration plus précise **Runge-Kutta** 
(au lieu de l'approximation simple par différences finies).

```python
def runge_kutta(v0, theta, g, t_max, dt):
    # Initialisation des variables
    t = # TODO series de valeurs 
    x = # TODO plein de zeros
    y = # TODO plein de zeros
    vx = # TODO v0 * cos(theta)
    vy = # TODO v0 * sin(theta)
    
    for i in range(1, len(t)):
        kx1 = vx * dt
        ky1 = vy * dt
        kx2 = (vx) * dt
        ky2 = (vy - 0.5 * g * dt) * dt
        
        x[i] = x[i - 1] + kx2
        y[i] = y[i - 1] + ky2
        
        vy -= g * dt
    
    return t, x, y

# Simulation avec Runge-Kutta
t, x, y = runge_kutta(v0, theta_rad, g, t_max, dt)

# Affichage de la trajectoire
plt.plot(x, y)
plt.title("Trajectoire avec méthode de Runge-Kutta")
plt.xlabel("Distance (m)")
plt.ylabel("Hauteur (m)")
plt.grid(True)
plt.show()
```
