import numpy as np
from matplotlib import pyplot as plt

from lab4.lab.param import mu, lambda_1, lambda_2

rho = (lambda_1 + lambda_2) / mu
rho_1 = lambda_1 / mu
rho_2 = lambda_2 / mu

Wq_1 = (lambda_2 / (mu * (mu - lambda_1 - lambda_2)))
Wq_2 = ((lambda_1 + lambda_2) / (mu * (mu - lambda_1 - lambda_2)))

W_1 = Wq_1 + (1 / mu)
W_2 = Wq_2 + (1 / mu)

L = (lambda_1 + lambda_2) * (W_1 + W_2) / 2

P_wait = rho_2 / (1 - rho_1)

def print_res():
    print(f"Коэффициент загрузки системы: {rho:.2f}")

    print(f"Среднее время ожидания в очереди (высокий приоритет): {Wq_1:.2f} ч")
    print(f"Среднее время ожидания в очереди (низкий приоритет): {Wq_2:.2f} ч")
    print(f"Среднее время пребывания в системе (высокий приоритет): {W_1:.2f} ч")
    print(f"Среднее время пребывания в системе (низкий приоритет): {W_2:.2f} ч")
    print(f"Вероятность того, что заявка будет ждать в очереди: {P_wait:.2f}")

    print(f"Среднее число заявок в системе: {L:.2f}")


def show_plot():
    lambda_values = np.linspace(1, 9, 50)
    Wq_1_values = lambda_2 / (mu * (mu - lambda_values))
    Wq_2_values = (lambda_values + lambda_2) / (mu * (mu - lambda_values))

    plt.figure(figsize=(8, 5))
    plt.plot(lambda_values, Wq_1_values, label="Высокий приоритет", color='red')
    plt.plot(lambda_values, Wq_2_values, label="Низкий приоритет", color='green')
    plt.xlabel("Интенсивность входящего потока (λ)")
    plt.ylabel("Среднее время ожидания в очереди (ч)")
    plt.title("Зависимость времени ожидания от λ")
    plt.legend()
    plt.grid()
    plt.show()
