import csv

from projectaircraft import config


class DistanceMatrix:
    def __init__(self, path):
        self.distances = None
        self.path = path

    def _load_all(self):
        self.distances = {}
        with open(self.path, newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                key = (row["from"], row["to"])
                self.distances[key] = float(row["distance_km"])

    def get_distance(self, origin, destination):

        # lazy loading
        if self.distances is None:
           self._load_all()

        key = (origin, destination)
        reverse_key = (destination, origin)
        return self.distances.get(key) or self.distances.get(reverse_key) or None


if __name__=="__main__":
    dm = DistanceMatrix(config.DATA)