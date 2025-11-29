# ⚽ Score Predictor

Un programme open source qui simule la **prédiction de score exact ou approximatif** entre deux équipes, basé sur leurs performances récentes et leurs confrontations directes.

## 🚀 Fonctionnement

1. L’utilisateur saisit deux équipes.
2. Le programme analyse :
   - les anciens face-à-face (moyennes)
   - la forme récente (buts marqués / encaissés)
3. Il calcule :
   - un score exact probable
   - une prédiction approximative (BTTS, Under 2.5, etc.)

## 🧩 Exemple d’exécution

```bash
$ python main.py
=== SIMULATEUR DE PREDICTION DE SCORE ===
Nom de l'équipe A : Real Madrid
Nom de l'équipe B : FC Barcelone

===== RESULTAT =====
Score probable : 2 - 1
Prediction approximative : BTTS
