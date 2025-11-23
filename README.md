# MonteCarlo_Option_Pricer
Monte Carlo implementation of European option pricer under GBM. Numerical validation and convergence analysis.

1. Quant_Pricing_Engine : Valorisation d'Options par Monte Carlo (Python/NumPy)

🎯 Motivation du Projet

Ce dépôt est le premier pilier de mon portfolio Quant. Il démontre ma maîtrise de la modélisation stochastique et de l'implémentation de méthodes numériques performantes.

Le projet vise à valoriser une option Call Européenne en utilisant la méthode de Monte Carlo (simulation), en utilisant le modèle de Mouvement Brownien Géométrique (GBM) pour le sous-jacent.

Compétences Clés Démontrées

Mathématiques (GMM) : Processus stochastiques, simulation de variables aléatoires (Box-Muller), Théorie de l'évaluation neutre au risque.

Technique : Utilisation de NumPy pour le calcul vectoriel et la rapidité d'exécution, bonne pratique de code Python.

🔬 Modèle Mathématique

L'Équation (GBM)

Sous la mesure neutre au risque, l'évolution du prix de l'actif ($S_t$) suit :

$$\mathrm{d} S_{t} = r S_{t} \mathrm{d} t + \sigma S_{t} \mathrm{d} W_{t}
$$### L'Implémentation Monte Carlo

Pour des options Européennes, la simulation peut se faire directement à maturité ($T$). Le prix est donné par :

$$\text{Prix} = e^{-rT} \mathbb{E}\left[\max(S\_T - K, 0)\right]
$$L'implémentation dans `gbm_pricer.py` utilise la nature vectorielle de `NumPy` pour simuler $N$ prix finaux ($S_T$) en parallèle, ce qui est significativement plus rapide que les boucles itératives.

-----

## 📊 Résultats et Analyse de la Convergence

L'exécution du script compare le prix estimé par Monte Carlo avec la solution analytique exacte (Black-Scholes).

### 1\. Convergence

Ce graphique confirme la validité de l'approche Monte Carlo. Plus le nombre de simulations (N) augmente, plus le prix estimé (ligne verte) converge vers la valeur de référence de Black-Scholes (ligne orange pointillée), conformément à la **Loi des Grands Nombres**.

### 2\. Distribution Log-Normale

L'histogramme des prix de l'actif à maturité ($S_T$) montre la distribution log-normale des prix finaux, ce qui est la signature du modèle GBM. La majeure partie de la probabilité est concentrée à gauche du Strike, mais la longue queue vers la droite justifie la valeur de l'option (le potentiel de gain illimité).

-----

## 🚀 Prochaines Étapes et Améliorations

1.  **Transition C++ :** Réécrire le moteur de calcul de base en C++ pour créer un *benchmark* de performance et le comparer à la version Python/NumPy (objectif de performance pour les grands N).
2.  **Options Exotiques :** Ajouter le pricing d'une option Asiatique (moyenne arithmétique des prix), pour laquelle la formule Black-Scholes n'existe pas, prouvant ainsi la nécessité de la simulation Monte Carlo.
3.  **Calcul des Greeks :** Ajouter le calcul des sensibilités (Delta, Gamma) par différences finies ou par la méthode de la *Pathwise Differentiation*.

## ⚙️ Comment Exécuter le Projet

1.  **Cloner le dépôt :** `git clone https://www.wordreference.com/fren/d%C3%A9p%C3%B4t`
2.  **Installer les dépendances :** Le projet nécessite Python, `numpy`, `scipy` et `matplotlib`.
    ```bash
    pip install numpy scipy matplotlib
    ```
3.  **Lancer la simulation :**
    ```bash
    python gbm_pricer.py
    ```$$
