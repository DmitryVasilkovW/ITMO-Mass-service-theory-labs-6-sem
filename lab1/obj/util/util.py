import simpy

from lab1.obj.bank_window_simulation import BankWindowSimulation


def run_simulation(arrival_rate, service_rate_param, simulation_time_param):
    env = simpy.Environment()
    simulation = BankWindowSimulation(env, arrival_rate, service_rate_param, simulation_time_param)

    env.process(simulation.arrival_process())
    env.run(until=simulation_time_param)

    return simulation.total_arrivals, simulation.served, simulation.lost, simulation.busy_time
