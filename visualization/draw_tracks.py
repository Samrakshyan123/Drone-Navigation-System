import cv2


class TrackVisualizer:

    def draw(

        self,

        frame,

        object_id,

        center,

        history

    ):

        cv2.putText(

            frame,

            f"ID:{object_id}",

            (center[0], center[1] - 15),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.5,

            (0, 255, 0),

            2

        )

        cv2.circle(

            frame,

            center,

            5,

            (0, 255, 0),

            -1

        )

        if len(history) > 1:

            for i in range(

                1,

                len(history)

            ):

                cv2.line(

                    frame,

                    history[i - 1],

                    history[i],

                    (255, 0, 0),

                    2

                )

        return frame