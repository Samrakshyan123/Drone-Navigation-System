import cv2

from detector.motion_detector import MotionDetector

from tracker.centroid_tracker import CentroidTracker
from tracker.track_manager import TrackManager

from prediction.velocity_estimator import VelocityEstimator
from prediction.trajectory_predictor import TrajectoryPredictor
from prediction.occupancy_predictor import OccupancyPredictor

from navigation.occupancy_grid import OccupancyGrid
from navigation.corridor_generator import CorridorGenerator
from navigation.risk_model import RiskModel
from navigation.decision_engine import DecisionEngine


cap = cv2.VideoCapture(0)

ret, frame = cap.read()

if not ret:
    print("Camera error")
    exit()

H, W = frame.shape[:2]

motion_detector = MotionDetector()

tracker = CentroidTracker()
track_manager = TrackManager()

velocity_estimator = VelocityEstimator()
trajectory_predictor = TrajectoryPredictor()
occupancy_predictor = OccupancyPredictor()

occupancy_grid = OccupancyGrid(
    W,
    H,
    cell_size=20
)

corridor_generator = CorridorGenerator()

risk_model = RiskModel()

decision_engine = DecisionEngine(
    W
)


while True:

    ret, frame = cap.read()

    if not ret:
        break

    detections = motion_detector.detect(
        frame
    )

    centroids = []

    for x, y, w, h in detections:

        cx = x + w // 2
        cy = y + h // 2

        centroids.append(
            (cx, cy)
        )

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (255, 255, 255),
            2
        )

    tracked_objects = tracker.update(
        centroids
    )

    zones = []

    for object_id, center in tracked_objects.items():

        track_manager.update(
            object_id,
            center
        )

        history = track_manager.get_positions(
            object_id
        )

        velocity = velocity_estimator.calculate(
            history
        )

        future_position = (
            trajectory_predictor.predict(
                center,
                velocity,
                seconds=2
            )
        )

        zone = (
            occupancy_predictor.build_zone(
                future_position,
                velocity["speed"]
            )
        )

        zones.append(zone)

        cv2.putText(
            frame,
            f"ID:{object_id}",
            (
                center[0],
                center[1] - 10
            ),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0,255,0),
            2
        )

        cv2.circle(
            frame,
            center,
            5,
            (0,255,0),
            -1
        )

        if len(history) > 1:

            for i in range(
                1,
                len(history)
            ):

                cv2.line(
                    frame,
                    history[i-1],
                    history[i],
                    (255,0,0),
                    2
                )

        cv2.line(
            frame,
            center,
            future_position,
            (255,0,0),
            2
        )

        cv2.circle(
            frame,
            future_position,
            6,
            (0,0,255),
            -1
        )

        cv2.circle(
            frame,
            zone["center"],
            zone["radius"],
            (0,255,255),
            2
        )

    occupancy_grid.add_zones(
        zones
    )

    occupancy_grid.draw(
        frame
    )

    corridor = (
        corridor_generator.find_best_corridor(
            occupancy_grid
        )
    )

    corridor_width = 0

    if corridor is not None:

        corridor_width = corridor["width"]

        corridor_generator.draw(
            frame,
            corridor,
            occupancy_grid.cell_size
        )

    occupancy_percent = (
        occupancy_grid.occupancy_percentage()
    )

    risk = risk_model.compute_risk(
        occupancy_percent,
        corridor_width
    )

    decision = (
        decision_engine.decide(
            corridor,
            risk
        )
    )

    cv2.putText(
        frame,
        f"Risk:{risk:.2f}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,255),
        2
    )

    cv2.putText(
        frame,
        f"Decision:{decision}",
        (20,80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0,255,0),
        2
    )

    cv2.imshow(
        "Drone Navigation",
        frame
    )

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()