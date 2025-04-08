import time
import os
from datetime import datetime
from guppy import hpy
import matplotlib.pyplot as plt

h = hpy()

memory_mb = []
steps = []


def allocate_and_track():
    data = []
    for i in range(0, 100_000, 5000):
        data.extend([[i] * 100] * 5000)

        heap = h.heap()
        size_mb = heap.size / 1024 / 1024
        memory_mb.append(size_mb)
        steps.append(i)

        print(f"🔍 Iteration {i} - Mémoire : {size_mb:.2f} MB")
        time.sleep(0.1)

    return data


def plot_and_save():
    # Tracer la courbe
    plt.figure(figsize=(10, 5))
    plt.plot(steps, memory_mb, marker="o", linestyle="-", color="purple")
    plt.xlabel("Nombre d'objets alloués")
    plt.ylabel("Mémoire utilisée (MB)")
    plt.title("Évolution mémoire (via guppy3)")
    plt.grid(True)
    plt.tight_layout()

    # Sauvegarde du graphique
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    path = f"outputs/guppy_memory_{timestamp}.png"
    plt.savefig(path)
    print(f"✅ Graphe sauvegardé sous : {path}")


if __name__ == "__main__":
    print("📥 Avant allocation :")
    print(h.heap())

    allocate_and_track()

    print("📤 Après allocation :")
    print(h.heap())

    plot_and_save()
