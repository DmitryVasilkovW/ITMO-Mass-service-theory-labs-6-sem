import numpy as np
import matplotlib.pyplot as plt

# Исходные данные
lambd = 8  # интенсивность входящего потока (заявок/час)
mu = 10  # интенсивность обслуживания (заявок/час)
rho = lambd / mu  # коэффициент загрузки системы


# Функция для расчёта характеристик системы M/M/1/K, где K = m+1 (число мест в системе)
def mm1k_metrics(m, lambd, mu):
    K = m + 1  # общее число мест в системе (один канал + m мест в очереди)

    if np.isclose(rho, 1.0):
        # Для rho=1 используется особая формула
        p0 = 1 / (K)
        p = np.array([p0 for _ in range(K + 1)])
    else:
        # Рассчёт p0:
        p0 = (1 - rho) / (1 - rho ** (K + 1))
        # Вероятностное распределение системы (n=0,...,K)
        p = np.array([rho ** n * p0 for n in range(K + 1)])

    # Вероятность, что система заполнена (блокировка заявки)
    p_loss = p[K]

    # Среднее число заявок в системе
    n_vals = np.arange(K + 1)
    L_system = np.sum(n_vals * p)

    # Среднее число заявок в очереди: если система не пуста, то один находится в обслуживании
    L_queue = L_system - (1 - p0)

    # Эффективная интенсивность входа (учитывая блокировки)
    lambd_eff = lambd * (1 - p_loss)

    # Среднее время пребывания заявки в системе (формула Литтла)
    if lambd_eff > 0:
        W_system = L_system / lambd_eff
        W_queue = L_queue / lambd_eff
    else:
        W_system = 0
        W_queue = 0

    # Загрузка сервера (вероятность, что сервер занят)
    # Можно принять, что сервер занят, когда в системе не 0 заявок
    server_util = 1 - p0

    return {
        "m": m,
        "K": K,
        "p0": p0,
        "p_loss": p_loss,
        "L_system": L_system,
        "L_queue": L_queue,
        "W_system": W_system,
        "W_queue": W_queue,
        "server_util": server_util
    }


# Исследуем зависимость характеристик от m (длина очереди)
m_values = np.arange(1, 16)  # рассматриваем m от 1 до 15
metrics_list = [mm1k_metrics(m, lambd, mu) for m in m_values]

# Извлекаем нужные величины для построения графиков
loss_probs = [res["p_loss"] for res in metrics_list]
waiting_times = [res["W_queue"] for res in metrics_list]

# Поиск оптимального m, при котором p_loss не превышает 5%
opt_m = None
for res in metrics_list:
    if res["p_loss"] <= 0.05:
        opt_m = res["m"]
        break

# Вывод результатов в виде таблицы
print("m\tp_loss\t\tL_queue\t\tW_queue\t\tServer Utilization")
for res in metrics_list:
    print(
        f"{res['m']}\t{res['p_loss']:.4f}\t\t{res['L_queue']:.4f}\t\t{res['W_queue']:.4f}\t\t{res['server_util']:.4f}")

if opt_m is not None:
    print(f"\nОптимальная длина очереди (m), при которой p_loss <= 5%: m = {opt_m}")
else:
    print("\nНе найдено значение m, при котором p_loss <= 5%.")

# Построение графиков
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
