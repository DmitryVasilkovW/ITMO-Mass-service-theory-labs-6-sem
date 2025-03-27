import numpy as np
from matplotlib import pyplot as plt

from lab3.lab.mm1k import mm1k_metrics, simulate_mm1k
from lab3.lab.param import lambd

m_values = np.arange(1, 16)
metrics_list = [simulate_mm1k(m, lambd) for m in m_values]

loss_probs = [res["p_loss"] for res in metrics_list]
waiting_times = [res["W_queue"] for res in metrics_list]

opt_m = None
for res in metrics_list:
    if res["p_loss"] <= 0.05:
        opt_m = res["m"]
        break

def print_res():
    print("m\tp_loss\t\tL_queue\t\tW_queue\t\tW_system\tServer Utilization")
    for res in metrics_list:
        print(
            f"{res['m']}\t{res['p_loss']:.4f}\t\t{res['L_queue']:.4f}\t\t{res['W_queue']:.4f}\t\t{res['W_system']:.4f}\t\t{res['server_util']:.4f}")

    if opt_m is not None:
        print(f"\nОптимальная длина очереди (m), при которой p_loss <= 5%: m = {opt_m}")
    else:
        print("\nНе найдено значение m, при котором p_loss <= 5%.")


def show_plot():
    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(m_values, loss_probs, marker='o')
    plt.xlabel("Длина очереди m")
    plt.ylabel("Вероятность потерь (p_loss)")
    plt.title("Зависимость p_loss от m")
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(m_values, waiting_times, marker='o', color='orange')
    plt.xlabel("Длина очереди m")
    plt.ylabel("Среднее время ожидания (ч)")
    plt.title("Зависимость W_queue от m")
    plt.grid(True)

    plt.tight_layout()
    plt.show()


show_plot()