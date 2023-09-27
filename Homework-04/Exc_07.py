points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    distance = 0
    for cord in range(len(coordinates)):
        if len(coordinates) <= 1:
            return distance
        a = [coordinates[cord], coordinates[cord + 1]]
        distance += points[min(a), max(a)]
    return distance
