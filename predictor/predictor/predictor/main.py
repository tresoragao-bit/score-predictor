from predictor.simulator import simulate_match

print("=== SIMULATEUR DE PREDICTION DE SCORE ===")

team_a = input("Nom de l'équipe A : ")
team_b = input("Nom de l'équipe B : ")

result = simulate_match(team_a, team_b)

print("\n===== RESULTAT =====")
print(f"Score probable : {result['exact_score']}")
print(f"Prediction approximative : {result['approx']}")
