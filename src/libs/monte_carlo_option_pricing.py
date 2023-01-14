from typing import Tuple

import numpy as np


def monte_carlo_option_pricing(S: float, K: float, r: float, sigma: float, T: float, n_sim: int) -> Tuple[float,float]:
    """
    Monte Carlo option pricing engine for European call and put options.
    S: spot price
    K: strike price
    r: risk-free interest rate
    sigma: volatility of the underlying asset
    T: time to maturity (in years)
    n_sim: number of simulations
    """
    dt: float = T / n_sim

    S_path: np.ndarray = np.zeros((n_sim + 1,))
    S_path[0] = S

    for i in range(1, n_sim + 1):
        e = np.random.normal(size=1)
        S_path[i] = S_path[i - 1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * e * np.sqrt(dt))

    call_option_price: float = np.mean(np.maximum(S_path[-1] - K, 0)) * np.exp(-r * T)
    put_option_price: float = np.mean(np.maximum(K - S_path[-1], 0)) * np.exp(-r * T)

    return call_option_price, put_option_price
