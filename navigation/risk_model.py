class RiskModel:

    def __init__(self):
        pass

    def compute_risk(
        self,
        occupancy_percent,
        corridor_width
    ):

        occupancy_risk = occupancy_percent

        corridor_risk = max(
            0,
            1 - (corridor_width / 20)
        )

        risk = (
            occupancy_risk * 0.6 +
            corridor_risk * 0.4
        )

        risk = min(
            1.0,
            max(0.0, risk)
        )

        return risk

    def classify(self, risk):

        if risk > 0.7:
            return "DANGER"

        if risk > 0.4:
            return "WARNING"

        return "SAFE"