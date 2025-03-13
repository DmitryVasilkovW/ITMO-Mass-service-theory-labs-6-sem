import numpy as np
import matplotlib.pyplot as plt
from math import factorial


# Функция для аналитических расчётов характеристик М/M/n системы
def analytical_mm_n(lam, mu, n):
    """
    lam - интенсивность входящего потока заявок (λ)
    mu  - интенсивность обслуживания одного канала (μ)
    n   - число каналов (окошек)
    """
    a = lam / mu  # Общая нагрузка
    rho = lam / (n * mu)  # Коэффициент загрузки системы (при условии ρ < 1)

    # Вычисляем сумму для k=0,...,n-1
    sum_terms = sum([a ** k / factorial(k) for k in range(n)])
    # Формула для P0 (вероятность, что система пуста)
    if rho < 1:
        P0 = 1 / (sum_terms + (a ** n / factorial(n)) * (1 / (1 - rho)))
        # Вероятность ожидания (все серверы заняты)
        Pw = (a ** n / factorial(n)) * (1 / (1 - rho)) * P0
        # Среднее число заявок в очереди
        Lq = Pw * rho / (1 - rho)
        # Среднее время ожидания (Wq = Lq/λ)
        Wq = Lq / lam
        # Среднее время пребывания в системе (W = Wq + 1/μ)
        W = Wq + 1 / mu
    else:
        P0 = Pw = Lq = Wq = W = None  # Система неустойчива при ρ >= 1
    return P0, Pw, Lq, Wq, W


# Функция имитационного моделирования М/M/n системы
def simulate_mm_n(lam, mu, n, simulation_time):
    """
    lam             - интенсивность входящего потока (λ)
    mu              - интенсивность обслуживания (μ) одного канала
    n               - количество каналов
    simulation_time - общее время моделирования (например, 10000 часов)

    Возвращает: среднее время ожидания, среднее время пребывания в системе, среднюю длину очереди.
    """
    time = 0.0
    # Планируем первое поступление
    next_arrival = np.random.exponential(1 / lam)
    # Инициализируем время завершения обслуживания для каждого канала (сначала все свободны)
    servers = [np.inf] * n
    queue = []  # Очередь для ожидающих заявок

    # Для расчёта статистик будем собирать времена ожидания и пребывания в системе
    waiting_times = []
    system_times = []
    # Для расчёта среднего числа заявок в очереди по времени – регистрируем изменения
    time_points = [0.0]
    queue_lengths = [0]

    # Основной цикл имитации
    while time < simulation_time:
        next_departure = min(servers)  # ближайшее завершение обслуживания среди каналов
        # Событие поступления происходит, если время следующего поступления меньше времени следующего завершения
        if next_arrival < next_departure and next_arrival < simulation_time:
            time = next_arrival
            time_points.append(time)
            queue_lengths.append(len(queue))

            # Ищем свободный канал (тот, у которого время завершения ≤ текущему времени)
            free_server = None
            for i in range(n):
                if servers[i] <= time:
                    free_server = i
                    break
            if free_server is not None:
                # Если канал свободен – заявка обслуживается сразу
                service_time = np.random.exponential(1 / mu)
                servers[free_server] = time + service_time
                waiting_times.append(0.0)  # без ожидания
                system_times.append(service_time)
            else:
                # Если все каналы заняты, заявка идёт в очередь
                queue.append(time)
            # Планируем следующее поступление
            next_arrival = time + np.random.exponential(1 / lam)
        else:
            # Событие завершения обслуживания
            time = next_departure
            time_points.append(time)
            queue_lengths.append(len(queue))
            # Определяем, какой канал освободился
            server_index = servers.index(next_departure)
            if queue:
                # Если в очереди есть заявка – начинаем обслуживание первой
                arrival_time = queue.pop(0)
                waiting_time = time - arrival_time
                waiting_times.append(waiting_time)
                service_time = np.random.exponential(1 / mu)
                servers[server_index] = time + service_time
                system_times.append(waiting_time + service_time)
            else:
                # Если очереди пусто – канал остаётся свободным
                servers[server_index] = np.inf

    # Расчёт среднего числа заявок в очереди (time-weighted average)
    total_time = 0.0
    area = 0.0
    for i in range(1, len(time_points)):
        dt = time_points[i] - time_points[i - 1]
        area += queue_lengths[i - 1] * dt
        total_time += dt
    avg_queue_length = area / total_time if total_time > 0 else 0

    avg_waiting_time = np.mean(waiting_times) if waiting_times else 0
    avg_system_time = np.mean(system_times) if system_times else 0

    return avg_waiting_time, avg_system_time, avg_queue_length


# Основные параметры задачи:
lam = 10.0  # интенсивность входящего потока (10 заявок/час)
mu = 3.0  # интенсивность обслуживания (3 заявки/час на один канал)
n = 4  # начальное количество каналов (например, 4 окошка)
simulation_time = 10000.0  # время моделирования (часов)

# АНАЛИТИЧЕСКИЕ РАСЧЁТЫ:
P0, Pw, Lq, Wq, W = analytical_mm_n(lam, mu, n)
print("Аналитические результаты для n =", n)
print("Вероятность простоя (P0):", P0)
print("Вероятность ожидания (Pw):", Pw)
print("Среднее число заявок в очереди (Lq):", Lq)
print("Среднее время ожидания в очереди (Wq):", Wq)
print("Среднее время пребывания заявки в системе (W):", W)

# ИМИТАЦИЯ ДЛЯ n = 4:
avg_wait, avg_sys, avg_queue = simulate_mm_n(lam, mu, n, simulation_time)
print("\nРезультаты моделирования для n =", n)
print("Среднее время ожидания в очереди:", avg_wait)
print("Среднее время пребывания в системе:", avg_sys)
print("Средняя длина очереди:", avg_queue)

# АНАЛИЗ ВЛИЯНИЯ КОЛИЧЕСТВА КАНАЛОВ:
# Рассмотрим изменение характеристик при изменении числа каналов от 1 до 10
ns = range(1, 11)
analytical_waits = []
analytical_queue_lengths = []
simulation_waits = []
simulation_queue_lengths = []

for channels in ns:
    # Аналитические расчёты
    _, _, Lq_temp, Wq_temp, _ = analytical_mm_n(lam, mu, channels)
    if Wq_temp is None:
        analytical_waits.append(np.nan)
        analytical_queue_lengths.append(np.nan)
    else:
        analytical_waits.append(Wq_temp)
        analytical_queue_lengths.append(Lq_temp)
    # Моделирование
    sim_wait, _, sim_queue = simulate_mm_n(lam, mu, channels, simulation_time)
    simulation_waits.append(sim_wait)
    simulation_queue_lengths.append(sim_queue)

# Построение графика зависимости среднего времени ожидания от числа каналов
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(ns, analytical_waits, 'o-', label="Аналитически", marker='o')
plt.plot(ns, simulation_waits, 's-', label="Моделирование", linestyle='dashed',  marker='s')
plt.xlabel("Количество каналов (n)")
plt.ylabel("Среднее время ожидания в очереди (Wq)")
plt.title("Зависимость Wq от количества каналов")
plt.legend()

# Построение графика зависимости длины очереди от числа каналов
plt.subplot(1, 2, 2)
plt.plot(ns, analytical_queue_lengths, 'o-', label="Аналитически")
plt.plot(ns, simulation_queue_lengths, 's-', label="Моделирование")
plt.xlabel("Количество каналов (n)")
plt.ylabel("Среднее число заявок в очереди (Lq)")
plt.title("Зависимость Lq от количества каналов")
plt.legend()

plt.tight_layout()
plt.show()
