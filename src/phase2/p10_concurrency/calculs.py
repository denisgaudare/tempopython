import math
import random

from geographiclib.geodesic import Geodesic

# Simule un gros fichier comme une liste de chaînes
def gros_fichier():
    fichier_simule = [str(i) for i in range(100_000)]


# Simule un traitement lourd (par ex. parsing + calcul)
def calcul_x_long(ligne):
    x = int(ligne)
    return math.sqrt(x**2 + math.sin(x)**2 + math.sqrt(math.cos(x)**3))

def karney_distance(lat1, lon1, lat2, lon2, compteur=0):
    # Utilise l'ellipsoïde WGS84
    geod = Geodesic.WGS84

    # Résout le problème géodésique inverse (distance entre deux points)
    result = geod.Inverse(lat1, lon1, lat2, lon2)

    # Retourne la distance en mètres
    return result['s12']

def calcul_N_distances(limit=1):
    # Exemple : Paris (48.853, 2.349) -> New York (40.7128, -74.0060)
    for cpt in range(1,limit):
        lat1 = random.uniform(-90, 90)
        lon1 = random.uniform(-180, 180)
        lat2 = random.uniform(-90, 90)
        lon2 = random.uniform(-180, 180)
        j, distance_m = karney_distance(lat1,lon1,lat2,lon2, cpt)
        print(f"Distance (Karney): {j:06d} -> {distance_m:.3f} m")
    distance_m = karney_distance(48.853, 2.349, 40.7128, -74.0060)
    print("Paris-NY",distance_m)

if __name__ == "__main__":
    calcul_N_distances(100)