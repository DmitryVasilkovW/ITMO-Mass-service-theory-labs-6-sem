import numpy as np
from matplotlib import pyplot as plt

from lab2.lab.util import calculate_metrics, simulate_queue
from lab2.lab.param import lambda_, mu_, n_channels, mu_values, n_fixed

def show_lq_and_wq_plot():
    #metrics = calculate_metrics(lambda_, mu_, n_channels)
    metrics = simulate_queue(lambda_, mu_, n_channels)
    print(f"Характеристики системы при n = {n_channels}:")
    for key, value in metrics.items():
        print(f"{key}: {value:.4f}")

    n_values = range(4, 9)
    results = []
    for n in n_values:
        m = calculate_metrics(lambda_, mu_, n)
        results.append(m if m else None)

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(n_values, [m['wq'] if m else None for m in results], marker='o')
    plt.xlabel('Количество каналов (n)')
    plt.ylabel('Wq (часы)')
    plt.title('Среднее время ожидания')

    plt.subplot(1, 2, 2)
    plt.plot(n_values, [m['lq'] if m else None for m in results], marker='s', color='orange')
    plt.xlabel('Количество каналов (n)')
    plt.ylabel('Lq')
    plt.title('Средняя длина очереди')
    plt.tight_layout()
    plt.show()


def show_mu_plot():
    wq_mu = []
    lq_mu = []

    for mu in mu_values:
        m = simulate_queue(lambda_, mu, n_fixed)
        if m:
            wq_mu.append(m['wq'])
            lq_mu.append(m['lq'])
        else:
            wq_mu.append(np.nan)
            lq_mu.append(np.nan)

    plt.figure(figsize=(12, 6))
    plt.plot(mu_values, wq_mu, marker='o', label='Wq')
    plt.plot(mu_values, lq_mu, marker='s', label='Lq')
    plt.xlabel('Интенсивность обслуживания (μ)')
    plt.ylabel('Значение')
    plt.title('Зависимость от μ')
    plt.legend()
    plt.grid(True)
    plt.show()

show_mu_plot()
show_lq_and_wq_plot()
