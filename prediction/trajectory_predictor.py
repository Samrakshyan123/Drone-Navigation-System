class TrajectoryPredictor:

    def __init__(self):
        pass

    def predict(
        self,
        current_position,
        velocity,
        seconds=1
    ):

        x, y = current_position

        vx = velocity["vx"]
        vy = velocity["vy"]

        future_x = int(
            x + vx * seconds
        )

        future_y = int(
            y + vy * seconds
        )

        return (
            future_x,
            future_y
        )

    def predict_multiple(
        self,
        current_position,
        velocity
    ):

        return {
            "1s": self.predict(
                current_position,
                velocity,
                1
            ),

            "2s": self.predict(
                current_position,
                velocity,
                2
            ),

            "5s": self.predict(
                current_position,
                velocity,
                5
            )
        }