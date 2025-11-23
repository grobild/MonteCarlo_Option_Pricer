import matplotlib.pyplot as plt
import numpy as np
from gbm_pricer import EuropeanCallOption
import time

# --- Configuration Parameters ---
S0 = 100.0      # Initial Price
K = 100.0       # Strike Price (At-the-money)
T = 1.0         # Maturity (1 Year)
r = 0.05        # Risk-free Rate (5%)
sigma = 0.2     # Volatility (20%)

def run_analysis():
    print(f"--- Starting Monte Carlo Analysis ---")
    print(f"Parameters: S0={S0}, K={K}, T={T}, r={r}, sigma={sigma}")

    # Initialize the option pricer
    option = EuropeanCallOption(S0, K, T, r, sigma)
    
    # ---------------------------------------------------------
    # 1. Calculate Exact Benchmark
    # ---------------------------------------------------------
    bs_price = option.black_scholes_price()
    print(f"\n[Benchmark] Black-Scholes Analytical Price: {bs_price:.6f}")

    # ---------------------------------------------------------
    # 2. Convergence Analysis
    # ---------------------------------------------------------
    print("\n[Analysis] Running Convergence Check...")
    
    # We simulate with increasing N to show the Law of Large Numbers
    sim_sizes = [100, 1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000, 5_000_000]
    mc_prices = []
    errors = []
    times = []

    for N in sim_sizes:
        start_time = time.time()
        price, _ = option.monte_carlo_price(N, seed=42) # Fixed seed for consistency across N
        end_time = time.time()
        
        mc_prices.append(price)
        error = abs(price - bs_price)
        errors.append(error)
        times.append(end_time - start_time)
        
        print(f"  N={N:9d} | MC Price={price:.6f} | Error={error:.6f} | Time={end_time-start_time:.4f}s")

    # PLOT 1: Convergence Graph
    plt.figure(figsize=(12, 6))
    plt.plot(sim_sizes, mc_prices, marker='o', linestyle='-', color='#2ecc71', label='Monte Carlo Estimate')
    plt.axhline(y=bs_price, color='#e67e22', linestyle='--', linewidth=2, label=f'Black-Scholes ({bs_price:.2f})')
    
    # Aesthetics
    plt.xscale('log') # Log scale to handle wide range of N
    plt.xlabel('Number of Simulations (N) - Log Scale')
    plt.ylabel('Option Price')
    plt.title('Convergence of Monte Carlo Estimator to Black-Scholes Price')
    plt.legend()
    plt.grid(True, which="both", ls="-", alpha=0.2)
    
    # Save plot for README
    plt.savefig('convergence_plot.png')
    print("\nSaved 'convergence_plot.png'")

    # ---------------------------------------------------------
    # 3. Distribution Analysis
    # ---------------------------------------------------------
    print("\n[Analysis] Generating Distribution Histogram...")
    
    # Run a large simulation to get a smooth histogram
    N_dist = 1_000_000
    _, ST = option.monte_carlo_price(N_dist, seed=42)

    # PLOT 2: Log-Normal Distribution
    plt.figure(figsize=(12, 6))
    
    # Plot histogram of terminal prices
    count, bins, ignored = plt.hist(ST, bins=100, density=True, alpha=0.6, color='#3498db', label='Simulated $S_T$')
    
    # Add vertical line for Strike Price
    plt.axvline(x=K, color='#e74c3c', linestyle='--', linewidth=2, label=f'Strike K ({K})')
    
    # Add vertical line for S0 (just for reference)
    plt.axvline(x=S0, color='black', linestyle=':', alpha=0.5, label=f'Initial $S_0$ ({S0})')

    plt.xlabel('Terminal Asset Price ($S_T$)')
    plt.ylabel('Probability Density')
    plt.title(f'Distribution of Terminal Prices (N={N_dist})')
    plt.legend()
    plt.grid(alpha=0.2)
    
    plt.savefig('distribution_plot.png')
    print("Saved 'distribution_plot.png'")
    
    plt.show()

if __name__ == "__main__":
    run_analysis()
