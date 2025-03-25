import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Исходные данные
lambda_1 = 3  # Высокоприоритетные заявки (заявок/час)
lambda_2 = 5  # Низкоприоритетные заявки (заявок/час)
mu = 10  # Интенсивность обслуживания (заявок/час)

# Коэффициент загрузки системы
rho = (lambda_1 + lambda_2) / mu

# Среднее время ожидания в очереди (формулы для абсолютного приоритета)
Wq_1 = (lambda_2 / (mu * (mu - lambda_1 - lambda_2)))  # Для высокоприоритетных заявок
Wq_2 = ((lambda_1 + lambda_2) / (mu * (mu - lambda_1 - lambda_2)))  # Для низкоприоритетных заявок

# Среднее время пребывания в системе (включает обслуживание)
W_1 = Wq_1 + (1 / mu)
W_2 = Wq_2 + (1 / mu)

# Среднее число заявок в системе
L = (lambda_1 + lambda_2) * (W_1 + W_2) / 2

# Вывод результатов
print(f"Коэффициент загрузки системы: {rho:.2f}")
print(f"Среднее время ожидания в очереди (высокий приоритет): {Wq_1:.2f} ч")
print(f"Среднее время ожидания в очереди (низкий приоритет): {Wq_2:.2f} ч")
print(f"Среднее время пребывания в системе (высокий приоритет): {W_1:.2f} ч")
print(f"Среднее время пребывания в системе (низкий приоритет): {W_2:.2f} ч")
print(f"Среднее число заявок в системе: {L:.2f}")

# Построение графиков зависимости времени ожидания от интенсивности входящего потока
lambda_values = np.linspace(1, 9, 50)
Wq_1_values = lambda_2 / (mu * (mu - lambda_values))
Wq_2_values = (lambda_values + lambda_2) / (mu * (mu - lambda_values))

plt.figure(figsize=(8, 5))
plt.plot(lambda_values, Wq_1_values, label="Высокий приоритет", color='blue')
plt.plot(lambda_values, Wq_2_values, label="Низкий приоритет", color='red')
plt.xlabel("Интенсивность входящего потока (λ)")
plt.ylabel("Среднее время ожидания в очереди (ч)")
plt.title("Зависимость времени ожидания от λ")
plt.legend()
plt.grid()
plt.show()
