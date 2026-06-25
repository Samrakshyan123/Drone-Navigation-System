import cv2


class DepthVisualizer:

    def draw(

        self,

        frame,

        bbox,

        depth

    ):

        x, y, w, h = bbox

        cv2.putText(

            frame,

            f"D:{depth:.2f}",

            (x, y - 10),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.6,

            (255, 255, 0),

            2

        )

        return frame