import os
import sys

import numpy as np
from matplotlib import pyplot as plt

from lab1.obj.util.util import run_simulation


class Visualisation:
    service_rate = 6
    simulation_time = 1000

    lambda_values = np.linspace(1, 10, 10)
    exp_blocking = []
    theoretical_blocking = []

    def print_results(self):
        self.__refresh()

        for lam in self.lambda_values:
            total_arr, served, lost, busy_time = run_simulation(lam, self.service_rate, self.simulation_time)

            blocking_prob = lost / total_arr if total_arr > 0 else 0
            self.exp_blocking.append(blocking_prob)

            rho = lam / self.service_rate
            th_blocking = rho / (1 + rho)
            self.theoretical_blocking.append(th_blocking)

            utilization = busy_time / self.simulation_time

            print(f"λ = {lam:.2f}: Всего: {total_arr}, Обслужено: {served}, Отказано: {lost}, "
                  f"P(отказа) = {blocking_prob:.3f}, Загрузка = {utilization:.3f}")

    def __refresh(self):
        self.service_rate = 6
        self.simulation_time = 1000

        self.lambda_values = np.linspace(1, 10, 10)
        self.exp_blocking = []
        self.theoretical_blocking = []

    def show_plot(self):
        if len(self.exp_blocking) == 0 or len(self.theoretical_blocking) == 0:
            sys.stdout = open(os.devnull, 'w')
            self.print_results()
            sys.stdout = sys.__stdout__

        plt.figure(figsize=(8, 6))
        plt.plot(self.lambda_values, self.exp_blocking, 'o-', label='Экспериментальная P(отказа)')
        plt.plot(self.lambda_values, self.theoretical_blocking, 's--', label='Теоретическая P(отказа) (Эрланг)')
        plt.xlabel('Интенсивность поступления λ (заявок/час)')
        plt.ylabel('Вероятность отказа')
        plt.title('Зависимость вероятности отказа от интенсивности входящего потока')
        plt.legend()
        plt.grid(True)
        plt.show()