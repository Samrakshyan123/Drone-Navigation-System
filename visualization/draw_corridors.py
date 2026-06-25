import cv2


class CorridorVisualizer:

    def draw(

        self,

        frame,

        corridor,

        decision,

        risk

    ):

        if corridor is not None:

            x1 = corridor["start"] * 20
            x2 = corridor["end"] * 20

            cv2.rectangle(

                frame,

                (x1, 0),

                (x2, frame.shape[0]),

                (0, 255, 0),

                3

            )

        cv2.putText(

            frame,

            f"Decision: {decision}",

            (20, 40),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 0),

            2

        )

        cv2.putText(

            frame,

            f"Risk: {risk:.2f}",

            (20, 80),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.8,

            (0, 255, 255),

            2

        )

        return frame