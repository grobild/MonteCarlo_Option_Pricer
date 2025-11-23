import numpy as np
from scipy.stats import norm
from typing import Tuple, Optional

class EuropeanCallOption:
    """
    A class to price European Call Options using:
    1. Analytical Black-Scholes-Merton Formula (Exact)
    2. Monte Carlo Simulation under Geometric Brownian Motion (Numerical)
    """

    def __init__(self, S0: float, K: float, T: float, r: float, sigma: float):
        """
        Initialize the Option parameters.

        :param S0: Initial asset price
        :param K: Strike price
        :param T: Time to maturity (in years)
        :param r: Risk-free interest rate (decimal, e.g., 0.05 for 5%)
        :param sigma: Volatility (decimal, e.g., 0.2 for 20%)
        """
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma

    def black_scholes_price(self) -> float:
        """
        Calculates the exact analytical price using the Black-Scholes closed-form solution.
        """
        d1 = (np.log(self.S0 / self.K) + (self.r + 0.5 * self.sigma ** 2) * self.T) / (self.sigma * np.sqrt(self.T))
        d2 = d1 - self.sigma * np.sqrt(self.T)
        
        # Call Price = S0 * N(d1) - K * e^(-rT) * N(d2)
        price = (self.S0 * norm.cdf(d1)) - (self.K * np.exp(-self.r * self.T) * norm.cdf(d2))
        return price

    def monte_carlo_price(self, num_simulations: int = 1_000_000, seed: Optional[int] = None) -> Tuple[float, np.ndarray]:
        """
        Calculates the price using Monte Carlo simulation.
        
        Uses vectorized NumPy operations for performance.
        
        :param num_simulations: Number of paths (N) to simulate.
        :param seed: Random seed for reproducibility.
        :return: Tuple containing (Estimated Price, Array of Terminal Prices ST)
        """
        if seed is not None:
            np.random.seed(seed)

        # 1. Generate Random Component (Z ~ N(0, 1))
        # We generate all N random variables at once using vectorization
        Z = np.random.standard_normal(num_simulations)
        
        # 2. Calculate Terminal Asset Prices (ST)
        # Formula: ST = S0 * exp((r - 0.5*sigma^2)T + sigma*sqrt(T)*Z)
        drift = (self.r - 0.5 * self.sigma ** 2) * self.T
        diffusion = self.sigma * np.sqrt(self.T) * Z
        
        ST = self.S0 * np.exp(drift + diffusion)
        
        # 3. Calculate Payoff for Call Option
        # Payoff = max(ST - K, 0)
        payoffs = np.maximum(ST - self.K, 0)
        
        # 4. Discount to Present Value
        discount_factor = np.exp(-self.r * self.T)
        price_estimate = discount_factor * np.mean(payoffs)
        
        return price_estimate, ST
