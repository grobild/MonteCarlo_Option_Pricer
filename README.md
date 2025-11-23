# Monte Carlo Option Pricer

![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![NumPy](https://img.shields.io/badge/NumPy-Vectorized-green) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Overview
A high-performance **Monte Carlo simulation engine** for pricing European Call options under **Geometric Brownian Motion (GBM)**. This project demonstrates stochastic modeling, vectorized numerical implementation in `NumPy`, and validation against the closed-form **Black-Scholes** solution.

### Key Features
* **Vectorized Simulation:** Leverages `NumPy` broadcasting for parallel path generation, minimizing runtime.
* **Analytical Benchmarking:** Validates numerical error convergence against Black-Scholes.
* **Statistical Analysis:** Verifies the Log-Normal distribution of terminal asset prices.

---

## 📐 Mathematical Model

### 1. Asset Dynamics (GBM)
The asset price $S_t$ evolves under the risk-neutral measure $\mathbb{Q}$ according to the Stochastic Differential Equation:

$$
\mathrm{d}S_t = r S_t \mathrm{d}t + \sigma S_t \mathrm{d}W_t^{\mathbb{Q}}
$$

Where:
* $r$: Risk-free rate
* $\sigma$: Volatility
* $W_t$: Wiener process

### 2. Numerical Solution
Since European options are path-independent, we simulate the terminal price $S_T$ directly using the exact solution to the SDE:

$$
S_T = S_0 \exp\left( \left(r - \frac{1}{2}\sigma^2\right)T + \sigma \sqrt{T} Z \right)
$$

Where $Z \sim \mathcal{N}(0, 1)$ is a standard normal random variable.

### 3. Monte Carlo Estimator
The option price is the discounted expectation of the payoff:

$$
V_0 \approx e^{-rT} \frac{1}{N} \sum_{i=1}^{N} \max(S_{T}^{(i)} - K, 0)
$$

---

## 📊 Validation
The implementation confirms the **Law of Large Numbers**, where the Monte Carlo estimator converges to the analytical Black-Scholes price at a rate of $\mathcal{O}(1/\sqrt{N})$.

![Convergence Plot](path/to/your/plot.png)
*(Replace this text with your actual image path)*

---

## 🚀 Roadmap
1. **C++ Implementation:** Rewrite the core engine in C++ for high-performance benchmarking ($N > 10^7$).
2. **Exotic Derivatives:** Extend pricing to **Asian Options** (path-dependent arithmetic mean).
3. **Greeks Calculation:** Implement Delta and Gamma sensitivity using pathwise differentiation.

---

## ⚙️ Usage

```bash
# 1. Clone the repository
git clone [https://github.com/grobild/montecarlo_option_pricer.git](https://github.com/grobild/montecarlo_option_pricer.git)

# 2. Install dependencies
pip install numpy scipy matplotlib

# 3. Run the pricer
python main.py
