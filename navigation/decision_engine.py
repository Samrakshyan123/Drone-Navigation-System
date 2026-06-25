class DecisionEngine:

    def __init__(
        self,
        frame_width
    ):

        self.frame_width = frame_width

    def decide(
        self,
        corridor,
        risk
    ):

        if corridor is None:
            return "STOP"

        if risk > 0.85:
            return "STOP"

        frame_center = (
            self.frame_width // 2
        )

        corridor_center = (
            corridor["center"]
        )

        corridor_center_px = (
            corridor_center * 20
        )

        offset = (
            corridor_center_px -
            frame_center
        )

        if abs(offset) < 80:
            return "FORWARD"

        if offset < 0:
            return "LEFT"

        return "RIGHT"