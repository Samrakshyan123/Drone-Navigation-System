import cv2
import torch
import numpy as np


class DepthEstimator:

    def __init__(
        self,
        model,
        transform,
        device
    ):

        self.model = model
        self.transform = transform
        self.device = device

    def estimate_depth(
        self,
        frame
    ):

        rgb = cv2.cvtColor(
            frame,
            cv2.COLOR_BGR2RGB
        )

        input_batch = (
            self.transform(rgb)
            .to(self.device)
        )

        with torch.no_grad():

            prediction = (
                self.model(
                    input_batch
                )
            )

            prediction = torch.nn.functional.interpolate(

                prediction.unsqueeze(1),

                size=rgb.shape[:2],

                mode="bicubic",

                align_corners=False

            ).squeeze()

        depth_map = (
            prediction
            .cpu()
            .numpy()
        )

        return depth_map

    def object_depth(
        self,
        depth_map,
        bbox
    ):

        x, y, w, h = bbox

        roi = depth_map[
            y:y+h,
            x:x+w
        ]

        if roi.size == 0:
            return 0

        return float(
            np.mean(roi)
        )