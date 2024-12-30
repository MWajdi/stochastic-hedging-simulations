import numpy as np
import matplotlib.pyplot as plt
from utils import gamma_bs

def compute_PLT(S, sigma, K, r, T, dt, n):
    """Compute the profit and loss for a single trajectory."""
    integral = 0.0

    for i in range(n):
        t = i * dt
        gamma = gamma_bs(S[i], K, T, sigma[0], r, t)
        integral += np.exp(r * (T - t)) * (sigma[0]**2 - sigma[i]**2) * S[i]**2 * gamma * dt

    return 0.5 * integral

def analyze_PLT(S_trajectories, sigma_trajectories,  K_values, m):
    """Analyze PLT for all strike prices and trajectories."""
    mean_PLT = []
    var_PLT = []

    for K in K_values:
        PLT_values = [compute_PLT(S_trajectories[j], sigma_trajectories[j], K) for j in range(m)]
        mean_PLT.append(np.mean(PLT_values))
        var_PLT.append(np.var(PLT_values))

        # Plot histogram for every 10th strike price
        if K % 10 == 0:
            plt.figure()
            plt.hist(PLT_values, bins=30, density=True, alpha=0.6, color='b')
            plt.title(f'Empirical Distribution of PLT(Σ) for K = {K}')
            plt.xlabel('PLT(Σ)')
            plt.ylabel('Density')
            plt.grid(True)
            plt.show()

    return mean_PLT, var_PLT

def plot_mean_and_variance(mean_PLT, var_PLT, K_values):
    """Plot the mean and variance of PLT as a function of K."""
    plt.figure(figsize=(12, 6))
    plt.plot(K_values, mean_PLT, label='Mean of PLT(Σ)')
    plt.xlabel('K')
    plt.ylabel('Mean of PLT(Σ)')
    plt.title('Mean of PLT(Σ) as a function of K')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(12, 6))
    plt.plot(K_values, var_PLT, label='Variance of PLT(Σ)', color='orange')
    plt.xlabel('K')
    plt.ylabel('Variance of PLT(Σ)')
    plt.title('Variance of PLT(Σ) as a function of K')
    plt.grid(True)
    plt.legend()
    plt.show()
