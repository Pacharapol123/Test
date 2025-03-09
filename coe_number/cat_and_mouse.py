def cat_and_mouse(x, y, z):
    distance_1 = abs(x - z)

    distance_2 = abs(y - z)

    if distance_1 < distance_2:
        return "Cat A"
    elif distance_2 < distance_1:
        return "Cat B"
    else:
        return "Mouse C"
