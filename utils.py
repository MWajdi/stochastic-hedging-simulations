import numpy as np

def d_plus(S, K, T, sigma, r, t):
    """Calculate d+ for Black-Scholes gamma."""
    return (np.log(S / K) + (r + 0.5 * sigma**2) * (T - t)) / (sigma * np.sqrt(T - t))

def gamma_bs(S, K, T, sigma, r, t):
    """Calculate the Black-Scholes gamma."""
    d1 = d_plus(S, K, T, sigma, r, t)
    return np.exp(-d1**2 / 2) / (S * sigma * np.sqrt(2 * np.pi * (T - t)))
