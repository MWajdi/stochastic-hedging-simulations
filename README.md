
# Stochastic Hedging Simulations

This repository contains a Python-based project exploring the profit and loss of Black-Scholes hedging strategies under a stochastic volatility framework. The simulations analyze how stochastic volatility impacts hedging efficiency for European call options and how different strike prices affect hedging outcomes.

## Project Structure

```
stochastic_hedging_simulations/
│
├── main_notebook.ipynb   # Main Jupyter notebook containing our study
├── utils.py              # Utility functions for mathematical and statistical calculations
├── simulation.py         # Functions to simulate sigma_t and S_t trajectories
├── analysis.py           # Functions for analyzing results and visualizing distributions
└── README.md             # Project overview
```


## How to Use

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/MWajdi/stochastic-hedging-simulations.git
   cd stochastic-hedging-simulations
   ```

2. **Install Required Libraries**:
   Ensure you have Python 3.x installed, then install the required packages:
   ```bash
   pip install numpy matplotlib
   ```

3. **Run the Notebook**:
   Open the `main_notebook.ipynb` file in Jupyter Notebook or JupyterLab to run simulations and view results.

## Insights

- **Mean and Variance Analysis**: The mean of $\text{PL}_T(\Sigma)$ exhibits a U-shaped behavior, while variance highlights growing risk for moderately in-the-money options.
- **Empirical Distributions**: Histograms indicate significant asymmetry and tail risks for deep in-the-money options, showing inefficiencies in hedging under stochastic volatility.

