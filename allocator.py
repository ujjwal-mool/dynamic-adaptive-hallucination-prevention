def allocate(risk):

    if risk < 0.1:
        return 1

    elif risk > 0.1:
        return 3

    else:
        return 5