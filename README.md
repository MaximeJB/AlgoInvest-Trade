**🚀 Projet OpenClassrooms n°7 – AlgoInvest\&Trade**

**Description**

Ce repository regroupe l'intégralité des livrables du projet OpenClassrooms n°7 de la formation Développeur d'application Python, réalisé pour AlgoInvest\&Trade. L'objectif principal est de démontrer la mise en place et l'optimisation d'un algorithme de sélection d'actions maximisant le profit sur un horizon de 2 ans.

---

## 🎯 Objectif

Transformer un besoin métier (sélection d'actions sous contraintes budgétaires) en solutions techniques performantes :

* **Brute-force** : exploration exhaustive pour un jeu de données initial.
* **Optimisation** : algorithme avancé assurant un temps de calcul < 1 s même pour de larges volumes.

---

## 🚀 Fonctionnalités clés

1. **Exploration exhaustive** (*Brute Force*) :

   * Lecture de fichiers CSV
   * Énumération de toutes les combinaisons respectant le budget
   * Sélection du panier optimal

2. **Algorithme optimisé** :

   * Application d'une approche dynamique
   * Réduction drastique de la complexité temporelle
   * Gestion de jeux de données à grande échelle pour 20 sets de données (<1 s)

3. **Reporting & Validation** :

   * Comparaison côte-à-côte avec les décisions historiques de Sienna
   * Rapport d'exploration des données

---

## 🛠️ Installation & Usage

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/MaximeJB/algoinvest-trade.git
   cd algo-invest-trade
   ```

2. **Installer les dépendances**

   ```bash
   pip install -r requirements.txt
   ```

3. **Lancer l'algorithme**

   ```bash
   # Version brute
   python bruteforce.py 

   # Version optimisée
   python optimized.py --file data/dataset2.csv
                         file data/dataset1.csv 
   ```

---

## 🔧 Technologies & Librairies

* **Python 3.10+**
* **pandas** pour la manipulation de données
* **matplotlib** (dans le reporting)

---

## 🏆 Résultats et Performances

* Brute-force : *O(2^n)* — pratique jusqu'à \~20 actions
* Optimisé   : *O(n × budget)* ou *O(n log n)* selon la stratégie
* Temps d'exécution : passage de plusieurs secondes à <1 s sur 100+ actions

---

## ✨ Auteur

**JEAN BAPTISTE Maxime** — Développeur Python

*Projet réalisé dans le cadre de la formation OpenClassrooms « Développeur d'application Python »*

---
