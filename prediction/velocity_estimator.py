import math
import numpy as np


class VelocityEstimator:

    def __init__(self):

        self.weights = [
            0.4,
            0.3,
            0.2,
            0.1
        ]

    def calculate(self, positions):

        if len(positions) < 2:
            return {
                "vx": 0,
                "vy": 0,
                "speed": 0,
                "direction": 0
            }

        velocities = []

        for i in range(1, len(positions)):

            x1, y1 = positions[i - 1]
            x2, y2 = positions[i]

            velocities.append(
                (
                    x2 - x1,
                    y2 - y1
                )
            )

        velocities = velocities[-4:]

        weights = self.weights[-len(velocities):]
        weights = np.array(weights)
        weights = weights / weights.sum()

        vx = 0
        vy = 0

        for w, (dx, dy) in zip(weights, velocities):

            vx += dx * w
            vy += dy * w

        speed = math.sqrt(vx**2 + vy**2)

        direction = math.degrees(
            math.atan2(vy, vx)
        )

        return {
            "vx": vx,
            "vy": vy,
            "speed": speed,
            "direction": direction
        }