def allocate(risk):

    if risk < 0.20:
        return 1

    elif risk < 0.40:
        return 2

    elif risk < 0.60:
        return 3

    elif risk < 0.80:
        return 4

    else:
        return 5
    