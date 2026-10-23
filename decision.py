def decide(confidence, risk):

    if confidence >= 0.90:
        return "HIGH CONFIDENCE"

    if confidence >= 0.80 and risk < 0.60:
        return "HIGH CONFIDENCE"

    if confidence >= 0.65:
        return "MEDIUM CONFIDENCE"

    return "LOW CONFIDENCE (Possible Hallucination)"