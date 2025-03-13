import math


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
