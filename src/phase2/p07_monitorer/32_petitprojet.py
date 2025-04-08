import time
import os
import matplotlib.pyplot as plt
import memray
from memray import Tracker
from memray.reporters.summary import SummaryReporter

# https://bloomberg.github.io/memray/

def leaky_function():
    data = []
    for i in range(100_000):
        data.append([i] * 100)
        if i % 10_000 == 0:
            time.sleep(0.01)
    return data

def profile_and_plot():
    # Créer un fichier binaire temporaire pour le tracking memray
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)
    bin_path = os.path.join(output_dir, f"memray_profile_{timestamp}.bin")

    # Profiler avec memray
    with Tracker(bin_path):
        leaky_function()

    # Charger les allocations depuis le fichier
    allocations = []
    timestamps = []

    with memray.FileReader(bin_path) as reader:
        for record in reader.get_allocation_records():
            allocations.append(record.size)
            timestamps.append(record.timestamp)

    # Cumuler les allocations (approximativement, à titre illustratif)
    cumulative = []
    total = 0
    for a in allocations:
        total += a
        cumulative.append(total / 1024 / 1024)  # Convertir en MB

    # Graphe matplotlib
    plt.figure(figsize=(10, 5))
    plt.plot(cumulative, label="Mémoire cumulée (MB)", linewidth=2)
    plt.xlabel("N° d'allocation")
    plt.ylabel("Mémoire (MB)")
    plt.title("Profil mémoire avec Memray")
    plt.grid(True)
    plt.legend()
    png_path = os.path.join(output_dir, f"memray_graph_{timestamp}.png")
    plt.tight_layout()
    plt.savefig(png_path)
    print(f"✅ Graphe sauvegardé sous : {png_path}")
    print(f"🔍 Profil Memray : {bin_path}")


if __name__ == "__main__":
    profile_and_plot()
