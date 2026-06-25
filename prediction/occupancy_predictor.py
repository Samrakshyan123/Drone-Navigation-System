import math


class OccupancyPredictor:

    def __init__(self):

        self.base_radius = 40

    def build_zone(
        self,
        future_position,
        speed,
        depth=None
    ):

        radius = self.base_radius

        radius += int(speed * 5)

        if depth is not None:

            if depth > 0:

                radius += int(
                    500 / depth
                )

        radius = max(
            40,
            min(radius, 250)
        )

        return {
            "center": future_position,
            "radius": radius
        }

    def collision_risk(
        self,
        drone_position,
        zone
    ):

        zx, zy = zone["center"]

        dx = drone_position[0] - zx
        dy = drone_position[1] - zy

        distance = math.sqrt(
            dx**2 + dy**2
        )

        if distance <= zone["radius"]:
            return True

        return False