import cv2


class PredictionVisualizer:

    def draw(

        self,

        frame,

        current_position,

        future_position,

        occupancy_zone

    ):

        cv2.line(

            frame,

            current_position,

            future_position,

            (255, 0, 0),

            2

        )

        cv2.circle(

            frame,

            future_position,

            6,

            (0, 0, 255),

            -1

        )

        cv2.circle(

            frame,

            occupancy_zone["center"],

            occupancy_zone["radius"],

            (0, 255, 255),

            2

        )

        return frame