import math
import random

import simpy


def calculate_metrics(lambd, mu, n):
    rho = lambd / (n * mu)
    if rho >= 1:
        return None

    sum_p0 = sum(((lambd / mu) ** k) / math.factorial(k) for k in range(n))
    p0_term = ((lambd / mu) ** n) / (math.factorial(n) * (1 - rho))
    p0 = 1 / (sum_p0 + p0_term)

    p_que = p0_term * p0
    lq = (p_que * rho) / (1 - rho)
    wq = lq / lambd
    w = wq + 1 / mu
    l = lambd * w

    return {
        'p0': p0,
        'p_que': p_que,
        'lq': lq,
        'wq': wq,
        'w': w,
        'l': l,
        'rho': rho
    }


def simulate_queue(lambd, mu, n, sim_time=10000):
    env = simpy.Environment()
    server = simpy.Resource(env, capacity=n)

    wait_times = []
    system_times = []
    queue_lengths = []
    busy_servers = 0
    total_customers = 0

    def customer(env, server):
        nonlocal busy_servers, total_customers
        arrival_time = env.now
        with server.request() as req:
            queue_len = max(len(server.queue) - (n - busy_servers), 0)
            queue_lengths.append(queue_len)

            yield req
            wait_time = env.now - arrival_time
            wait_times.append(wait_time)

            busy_servers += 1
            service_time = random.expovariate(mu)
            yield env.timeout(service_time)
            busy_servers -= 1

            total_customers += 1
            system_times.append(env.now - arrival_time)

    def arrival_process(env, lambd, server):
        while True:
            yield env.timeout(random.expovariate(lambd))
            env.process(customer(env, server))

    env.process(arrival_process(env, lambd, server))
    env.run(until=sim_time)

    p0 = 1 - (sum(queue_lengths) / len(queue_lengths)) / n
    p_que = sum(1 for t in wait_times if t > 0) / total_customers if total_customers else 0
    lq = sum(queue_lengths) / len(queue_lengths) if queue_lengths else 0
    wq = sum(wait_times) / len(wait_times) if wait_times else 0
    w = sum(system_times) / len(system_times) if system_times else 0
    l = lambd * w
    rho = 1 - p0

    return {
        'p0': p0,
        'p_que': p_que,
        'lq': lq,
        'wq': wq,
        'w': w,
        'l': l,
        'rho': rho
    }
