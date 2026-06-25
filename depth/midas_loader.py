import torch


class MiDaSLoader:

    def __init__(self):

        self.device = torch.device(
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self.model = torch.hub.load(
            "intel-isl/MiDaS",
            "MiDaS_small"
        )

        self.model.to(
            self.device
        )

        self.model.eval()

        transforms = torch.hub.load(
            "intel-isl/MiDaS",
            "transforms"
        )

        self.transform = (
            transforms.small_transform
        )

    def get_model(self):

        return (
            self.model,
            self.transform,
            self.device
        )