def calculate_score(score):
    if score >=8.0:
        return "highly relevent"
    elif score>=7.0:
        return " relevent"
    else:
        return "not relevent"

result = calculate_score(9.5)
print(result)