import numpy as np

def simulate_sigma(n, dt, lambda_, c, gamma, sigma0):
    """
    Simulate a single trajectory of the Ornstein-Uhlenbeck process sigma_t.
    Returns:
        sigma (numpy.ndarray): Simulated trajectory of sigma_t.
    """
    sigma = np.zeros(n + 1)
    sigma[0] = sigma0

    for i in range(1, n + 1):
        dW2 = np.sqrt(dt) * np.random.randn()
        sigma[i] = sigma[i - 1] + lambda_ * (c - sigma[i - 1]) * dt + gamma * dW2

    return sigma

def simulate_S(sigma, n, dt, lambda_, c, gamma, S0, sigma0):
    """
    Simulate a single trajectory of the asset price S_t using sigma_t.
    Args:
        sigma (numpy.ndarray): Simulated trajectory of sigma_t.
    Returns:
        S (numpy.ndarray): Simulated trajectory of S_t.
    """
    S = np.zeros(n + 1)
    S[0] = S0

    for i in range(1, n + 1):
        dW1 = np.sqrt(dt) * np.random.randn()
        S[i] = S[i - 1] * np.exp(-0.5 * sigma[i - 1]**2 * dt + sigma[i - 1] * dW1)

    return S
