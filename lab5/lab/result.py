import numpy as np
import simpy
from matplotlib import pyplot as plt

from lab5.lab.Bank import Bank
from lab5.lab.param import sim_time

env = simpy.Environment()
smo = Bank(env)
env.process(smo.generate_requests())
env.process(smo.manage_agents())
env.process(smo.monitor())
env.run(until=sim_time)

average_wait_time = np.mean(smo.total_wait_time)
average_queue_length = np.mean(smo.queue_lengths)
average_agents = np.mean(smo.agent_counts)
loss_probability = smo.lost_requests / (len(smo.total_wait_time) + smo.lost_requests)

def print_res():
    print(f'Среднее время ожидания: {average_wait_time:.2f}')
    print(f'Средняя длина очереди: {average_queue_length:.2f}')
    print(f'Среднее число агентов: {int(average_agents)}')
    print(f'Вероятность потери заявки: {loss_probability:.2%}')


def show_plot():
    plt.figure(figsize=(12, 6))
    plt.subplot(2, 1, 1)
    plt.plot(smo.agent_counts, label='Число агентов', color='red')
    plt.xlabel('Время')
    plt.ylabel('Число агентов')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(smo.queue_lengths, label='Длина очереди', color='green')
    plt.xlabel('Время')
    plt.ylabel('Длина очереди')
    plt.legend()

    plt.show()
