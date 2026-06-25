import math


def distance(p1, p2):

    return math.sqrt(
        (p1[0] - p2[0])**2 +
        (p1[1] - p2[1])**2
    )


def midpoint(p1, p2):

    return (
        int((p1[0] + p2[0]) / 2),
        int((p1[1] + p2[1]) / 2)
    )


def angle_between(p1, p2):

    dx = p2[0] - p1[0]
    dy = p2[1] - p1[1]

    return math.degrees(
        math.atan2(dy, dx)
    )


def bbox_center(bbox):

    x, y, w, h = bbox

    return (
        x + w // 2,
        y + h // 2
    )


def circle_overlap(c1, r1, c2, r2):

    d = distance(c1, c2)

    return d <= (r1 + r2)