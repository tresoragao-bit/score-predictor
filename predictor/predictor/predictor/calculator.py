import random

def get_head_to_head_stats(a, b):
    """Retourne les stats moyennes des confrontations directes (exemple statique)."""
    return {
        "avg_goals_a": 1.4,
        "avg_goals_b": 1.2
    }

def get_recent_form(team):
    """Retourne les 5 derniers résultats de l'équipe (exemple statique)."""
    return {
        "scored": [random.randint(0, 3) for _ in range(5)],
        "conceded": [random.randint(0, 3) for _ in range(5)]
    }

def calculate_score_prediction(h2h, form_a, form_b):
    """Calcule un score probable et une prédiction approximative."""
    avg_a = (h2h["avg_goals_a"] + sum(form_a["scored"]) / len(form_a["scored"])) / 2
    avg_b = (h2h["avg_goals_b"] + sum(form_b["scored"]) / len(form_b["scored"])) / 2

    goal_a = round(avg_a)
    goal_b = round(avg_b)

    approx = "BTTS" if goal_a > 0 and goal_b > 0 else "Under 2.5"

    return {
        "exact_score": f"{goal_a} - {goal_b}",
        "approx": approx
  }
