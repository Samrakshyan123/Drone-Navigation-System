import cv2


class MotionDetector:

    def __init__(self):

        self.background = None

    def detect(self, frame):

        gray = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2GRAY
        )

        gray = cv2.GaussianBlur(
            gray,
            (21, 21),
            0
        )

        if self.background is None:

            self.background = gray
            return []

        frame_delta = cv2.absdiff(
            self.background,
            gray
        )

        thresh = cv2.threshold(
            frame_delta,
            25,
            255,
            cv2.THRESH_BINARY
        )[1]

        thresh = cv2.dilate(
            thresh,
            None,
            iterations=2
        )

        contours, _ = cv2.findContours(
            thresh,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        detections = []

        for contour in contours:

            if cv2.contourArea(contour) < 500:
                continue

            x, y, w, h = cv2.boundingRect(
                contour
            )

            detections.append(
                (
                    x,
                    y,
                    w,
                    h
                )
            )

        self.background = gray

        return detections