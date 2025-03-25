import simpy
import random

from lab5.lab.param import initial_agents, lambda_requests, mu_service, agent_connect_rate, max_agents, \
    agent_disconnect_rate


class Bank:
    def __init__(self, env):
        self.env = env
        self.queue = simpy.PriorityResource(env, capacity=initial_agents)  # Используем PriorityResource
        self.active_agents = initial_agents
        self.total_wait_time = []
        self.queue_lengths = []
        self.agent_counts = []
        self.lost_requests = 0

    def process_request(self):
        arrival_time = self.env.now
        with self.queue.request(priority=1) as req:  # Добавляем приоритет (для FIFO)
            result = yield req | self.env.timeout(1 / lambda_requests)
            if req in result:
                yield self.env.timeout(1 / mu_service)
                self.total_wait_time.append(self.env.now - arrival_time)
            else:
                self.lost_requests += 1  # Если заявка не дождалась обработки, теряем её

    def generate_requests(self):
        while True:
            yield self.env.timeout(random.expovariate(lambda_requests))
            self.env.process(self.process_request())

    def manage_agents(self):
        while True:
            yield self.env.timeout(1)
            if random.random() < agent_connect_rate and self.active_agents < max_agents:
                self.active_agents += 1
                self.servers = simpy.Resource(self.env, capacity=self.active_agents)
            if random.random() < agent_disconnect_rate and self.active_agents > 1:
                self.active_agents -= 1
                self.servers = simpy.Resource(self.env, capacity=self.active_agents)
            self.agent_counts.append(self.active_agents)

    def monitor(self):
        while True:
            yield self.env.timeout(10)
            self.queue_lengths.append(len(self.queue.queue))