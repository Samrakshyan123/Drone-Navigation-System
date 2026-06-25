import cv2


class CorridorGenerator:

    def __init__(self):
        pass

    def find_best_corridor(self, occupancy_grid):

        grid = occupancy_grid.get_grid()

        rows, cols = grid.shape

        bottom_row = grid[rows - 1]

        corridors = []

        start = None

        for col in range(cols):

            if bottom_row[col] == 0:

                if start is None:
                    start = col

            else:

                if start is not None:
                    corridors.append((start, col - 1))
                    start = None

        if start is not None:
            corridors.append((start, cols - 1))

        if len(corridors) == 0:
            return None

        best = max(
            corridors,
            key=lambda x: x[1] - x[0]
        )

        return {
            "start": best[0],
            "end": best[1],
            "center": (best[0] + best[1]) // 2,
            "width": best[1] - best[0]
        }

    def draw(self, frame, corridor, cell_size):

        if corridor is None:
            return frame

        x1 = corridor["start"] * cell_size
        x2 = corridor["end"] * cell_size

        cv2.rectangle(
            frame,
            (x1, 0),
            (x2, frame.shape[0]),
            (0, 255, 0),
            2
        )

        return frame