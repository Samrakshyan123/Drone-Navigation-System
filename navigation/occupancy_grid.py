import numpy as np
import cv2


class OccupancyGrid:

    def __init__(
        self,
        frame_width,
        frame_height,
        cell_size=20
    ):

        self.frame_width = frame_width
        self.frame_height = frame_height

        self.cell_size = cell_size

        self.cols = frame_width // cell_size
        self.rows = frame_height // cell_size

        self.grid = np.zeros(
            (self.rows, self.cols),
            dtype=np.uint8
        )

    def clear(self):

        self.grid.fill(0)

    def add_zone(self, zone):

        cx, cy = zone["center"]
        radius = zone["radius"]

        for row in range(self.rows):

            for col in range(self.cols):

                cell_x = col * self.cell_size + self.cell_size // 2
                cell_y = row * self.cell_size + self.cell_size // 2

                distance = np.sqrt(
                    (cell_x - cx) ** 2 +
                    (cell_y - cy) ** 2
                )

                if distance <= radius:
                    self.grid[row, col] = 1

    def add_zones(self, zones):

        self.clear()

        for zone in zones:
            self.add_zone(zone)

    def get_grid(self):

        return self.grid

    def is_safe(self, x, y):

        col = int(x / self.cell_size)
        row = int(y / self.cell_size)

        if (
            row < 0 or
            row >= self.rows or
            col < 0 or
            col >= self.cols
        ):
            return False

        return self.grid[row, col] == 0

    def occupancy_percentage(self):

        occupied = np.sum(self.grid)

        total = self.rows * self.cols

        return occupied / total

    def draw(self, frame):

        overlay = frame.copy()

        for row in range(self.rows):

            for col in range(self.cols):

                x1 = col * self.cell_size
                y1 = row * self.cell_size

                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                if self.grid[row, col] == 1:

                    cv2.rectangle(
                        overlay,
                        (x1, y1),
                        (x2, y2),
                        (0, 0, 255),
                        -1
                    )

        cv2.addWeighted(
            overlay,
            0.25,
            frame,
            0.75,
            0,
            frame
        )

        for row in range(self.rows):

            y = row * self.cell_size

            cv2.line(
                frame,
                (0, y),
                (self.frame_width, y),
                (50, 50, 50),
                1
            )

        for col in range(self.cols):

            x = col * self.cell_size

            cv2.line(
                frame,
                (x, 0),
                (x, self.frame_height),
                (50, 50, 50),
                1
            )

        return frame