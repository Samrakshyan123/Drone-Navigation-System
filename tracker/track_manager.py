from collections import defaultdict
from datetime import datetime


class TrackManager:

    def __init__(self, history_size=30):

        self.history_size = history_size

        self.tracks = defaultdict(
            lambda: {
                "positions": [],
                "timestamps": [],
                "bboxes": [],
                "depths": []
            }
        )

    def update(
        self,
        object_id,
        position,
        bbox=None,
        depth=None
    ):

        track = self.tracks[object_id]

        track["positions"].append(position)
        track["timestamps"].append(datetime.now())

        if bbox is not None:
            track["bboxes"].append(bbox)

        if depth is not None:
            track["depths"].append(depth)

        track["positions"] = track["positions"][-self.history_size:]
        track["timestamps"] = track["timestamps"][-self.history_size:]
        track["bboxes"] = track["bboxes"][-self.history_size:]
        track["depths"] = track["depths"][-self.history_size:]

    def get_positions(self, object_id):

        return self.tracks[object_id]["positions"]

    def get_depths(self, object_id):

        return self.tracks[object_id]["depths"]

    def get_track(self, object_id):

        return self.tracks[object_id]

    def get_all_tracks(self):

        return self.tracks