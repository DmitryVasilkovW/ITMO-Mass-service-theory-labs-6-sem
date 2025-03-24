import numpy as np

from lab3.lab.param import rho


def mm1k_metrics(m, lambd):
    K = m + 1

    if np.isclose(rho, 1.0):
        p0 = 1 / K
        p = np.array([p0 for _ in range(K+1)])
    else:
        p0 = (1 - rho) / (1 - rho**(K+1))
        p = np.array([rho**n * p0 for n in range(K+1)])

    p_loss = p[K]

    n_vals = np.arange(K+1)
    L_system = np.sum(n_vals * p)

    L_queue = L_system - (1 - p0)

    lambd_eff = lambd * (1 - p_loss)

    if lambd_eff > 0:
        W_system = L_system / lambd_eff
        W_queue = L_queue / lambd_eff
    else:
        W_system = 0
        W_queue = 0

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
