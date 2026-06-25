import math


class MotionCluster:

    def __init__(

        self,

        distance_threshold=80,
        velocity_threshold=5

    ):

        self.distance_threshold = (
            distance_threshold
        )

        self.velocity_threshold = (
            velocity_threshold
        )

    def cluster(
        self,
        objects
    ):

        clusters = []

        used = set()

        for i, obj1 in enumerate(objects):

            if i in used:
                continue

            cluster = [obj1]

            used.add(i)

            for j, obj2 in enumerate(objects):

                if j in used:
                    continue

                d = self.distance(
                    obj1["center"],
                    obj2["center"]
                )

                dv = self.velocity_difference(
                    obj1["velocity"],
                    obj2["velocity"]
                )

                if (
                    d < self.distance_threshold
                    and
                    dv < self.velocity_threshold
                ):

                    cluster.append(obj2)
                    used.add(j)

            clusters.append(
                self.merge(cluster)
            )

        return clusters

    def distance(
        self,
        p1,
        p2
    ):

        return math.sqrt(
            (p1[0]-p2[0])**2 +
            (p1[1]-p2[1])**2
        )

    def velocity_difference(
        self,
        v1,
        v2
    ):

        return math.sqrt(
            (v1[0]-v2[0])**2 +
            (v1[1]-v2[1])**2
        )

    def merge(
        self,
        cluster
    ):

        xs = []
        ys = []

        for obj in cluster:

            xs.append(
                obj["center"][0]
            )

            ys.append(
                obj["center"][1]
            )

        center = (
            int(sum(xs)/len(xs)),
            int(sum(ys)/len(ys))
        )

        return {
            "center": center,
            "members": cluster
        }