from predictor.calculator import (
    get_head_to_head_stats,
    get_recent_form,
    calculate_score_prediction
)

def simulate_match(team_a, team_b):
    """Simule le score probable entre deux équipes."""
    h2h = get_head_to_head_stats(team_a, team_b)
    form_a = get_recent_form(team_a)
    form_b = get_recent_form(team_b)

    return calculate_score_prediction(h2h, form_a, form_b)
