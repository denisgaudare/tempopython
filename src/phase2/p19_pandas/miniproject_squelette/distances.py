from geographiclib.geodesic import Geodesic


def karney_distance(lat1, lon1, lat2, lon2):
    # Utilise l'ellipsoïde WGS84
    geod = Geodesic.WGS84

    # Résout le problème géodésique inverse (distance entre deux points)
    result = geod.Inverse(lat1, lon1, lat2, lon2)

    # Retourne la distance en mètres
    return result['s12']
