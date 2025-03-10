import numpy as np
import simpy


class BankWindowSimulation:
    def __init__(self, env, arrival_rate, service_rate_param, simulation_time_param):
        self.env = env
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate_param
        self.simulation_time = simulation_time_param
        self.server = simpy.Resource(env, capacity=1)

        self.total_arrivals = 0
        self.served = 0
        self.lost = 0
        self.busy_time = 0

    def arrival_process(self):
        while True:
            interarrival = np.random.exponential(1 / self.arrival_rate)
            yield self.env.timeout(interarrival)

            self.total_arrivals += 1

            if self.server.count < self.server.capacity:
                self.env.process(self.service_process())
            else:
                self.lost += 1

    def service_process(self):
        with self.server.request() as request:
            yield request

            start_time = self.env.now

            service_time = np.random.exponential(1 / self.service_rate)
            yield self.env.timeout(service_time)

            self.served += 1
            busy_duration = self.env.now - start_time
            self.busy_time += busy_duration