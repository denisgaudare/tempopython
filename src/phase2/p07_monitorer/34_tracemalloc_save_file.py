import tracemalloc
import time
import matplotlib.pyplot as plt
import os
from datetime import datetime

def allocate_chunks(chunk_count=50, chunk_size=10000):
    data = []
    memory_evolution = []

    tracemalloc.start()

    for i in range(chunk_count):
        mul = 200000 if i==20 else 100
        data.extend([[i] * mul] * chunk_size)
        snapshot = tracemalloc.take_snapshot()
        total_alloc = sum(stat.size for stat in snapshot.statistics("lineno")) / 1024 / 1024  # en MB
        memory_evolution.append(total_alloc)
        print(f"📈 Étape {i + 1}/{chunk_count} - Mémoire cumulée : {total_alloc:.2f} MB")
        time.sleep(0.05)

    tracemalloc.stop()
    return memory_evolution

def plot_memory(memory_evolution):
    os.makedirs("outputs", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = f"outputs/tracemalloc_plot_{timestamp}.png"

    plt.figure(figsize=(10, 5))
    plt.plot(memory_evolution, marker="o", linestyle="-", color="teal")
    plt.title("Évolution cumulée de la mémoire (tracemalloc)")
    plt.xlabel("Étapes d’allocation")
    plt.ylabel("Mémoire allouée (MB)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path)

    print(f"✅ Graphique sauvegardé sous : {output_path}")

if __name__ == "__main__":
    memory_data = allocate_chunks()
    plot_memory(memory_data)
