def get_discipline_score(plan_respected: bool, risk_respected: bool, tilt_detected: bool):
    score = 100
    details = []

    if not plan_respected:
        score -= 40
        details.append("❌ Plan non respecté")
    else:
        details.append("✅ Plan respecté")

    if not risk_respected:
        score -= 30
        details.append("❌ Risk Management non respecté")
    else:
        details.append("✅ Risk Management respecté")

    if tilt_detected:
        score -= 20
        details.append("⚠️ Tilt détecté (Overtrade / Revenge)")
    else:
        details.append("✅ Pas de tilt")

    emoji = "🟩" if score >= 80 else "🟨" if score >= 50 else "🟥"

    return f"""📊 **Discipline Score du jour** {emoji}

**Score : {score}/100**

• {'\n• '.join(details)}

🧠 Objectif : rester au-dessus de 80 pour rester constant.
"""