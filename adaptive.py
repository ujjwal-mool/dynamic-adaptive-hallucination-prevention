def should_continue(confidence, current_responses, max_responses, risk):

    if current_responses >= max_responses:
        return False

    # Dynamic threshold
    if risk < 0.20:
        threshold = 0.75
    elif risk < 0.50:
        threshold = 0.82
    else:
        threshold = 0.90

    return confidence < threshold