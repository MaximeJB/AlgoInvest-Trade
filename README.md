# AlgoInvest-Trade

## 📊 Description du Projet
AlgoInvest-Trade est une application Python d'optimisation de portefeuille d'investissement développée dans le cadre du projet #7 d'OpenClassrooms. Le projet implémente et compare deux approches algorithmiques pour résoudre le problème du sac à dos (knapsack problem) appliqué à la sélection d'actions financières.

## 🎯 Objectif
Maximiser le retour sur investissement d'un portefeuille avec une contrainte budgétaire de 500€, en sélectionnant la combinaison optimale d'actions parmi un ensemble donné.

## 🔧 Fonctionnalités
- **Algorithme Bruteforce** : Exploration exhaustive de toutes les combinaisons possibles
- **Programmation Dynamique** : Solution optimisée pour traiter des datasets volumineux
- **Analyse comparative** : Comparaison des performances entre les deux approches
- **Traitement de données réelles** : Support de multiples datasets CSV

## 📁 Structure du Projet
```
AlgoInvest-Trade/
│
├── bruteforce.py           # Algorithme force brute
├── AlgoDynamique.py        # Algorithme de programmation dynamique
├── listes_actions.csv      # Dataset d'actions de test
├── listes_actionss.csv     # Dataset d'actions alternatif
├── dataset1_Python+P7.csv  # Dataset 1 - Données Sienna
└── dataset2_Python+P7.csv  # Dataset 2 - Données Sienna
```

## 🚀 Installation
```bash
# Cloner le repository
git clone https://github.com/MaximeJB/AlgoInvest-Trade.git
cd AlgoInvest-Trade
```

## 💻 Utilisation

### Algorithme Bruteforce
```bash
python bruteforce.py
```
⚠️ **Note** : Recommandé uniquement pour de petits datasets (<20 actions) en raison de la complexité O(2^n)

### Algorithme de Programmation Dynamique
```bash
python AlgoDynamique.py
```
✅ **Recommandé** : Solution optimisée avec complexité O(n*W) pour traiter des datasets volumineux

## 📈 Comparaison des Algorithmes

| Algorithme | Complexité Temporelle | Complexité Spatiale | Dataset Max Recommandé |
|------------|----------------------|---------------------|------------------------|
| Bruteforce | O(2^n) | O(n) | ~20 actions |
| Dynamique | O(n*W) | O(n*W) | Milliers d'actions |

## 📊 Datasets
- **listes_actions.csv** : Dataset de test initial (20 actions)
- **dataset1_Python+P7.csv** : Dataset Sienna #1
- **dataset2_Python+P7.csv** : Dataset Sienna #2 

## 🎓 Contexte Pédagogique
Ce projet fait partie de la formation Développeur d'Application Python d'OpenClassrooms (Projet #7). Il met en pratique :
- L'analyse algorithmique et la complexité
- L'optimisation de performance
- La résolution de problèmes NP-complets
- Le traitement de données financières

## 🛠️ Technologies Utilisées
- Python 3.x
- CSV (manipulation de données)
- Algorithmes d'optimisation

## 📝 Auteur
**Maxime JB** - [GitHub](https://github.com/MaximeJB)

## 📄 Licence
Ce projet est réalisé dans le cadre d'une formation OpenClassrooms.
