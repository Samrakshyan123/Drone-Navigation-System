import csv
import os
from datetime import datetime


class ExperimentLogger:

    def __init__(

        self,

        filename="experiment_log.csv"

    ):

        self.filename = filename

        if not os.path.exists(filename):

            with open(

                filename,

                "w",

                newline=""

            ) as f:

                writer = csv.writer(f)

                writer.writerow([

                    "timestamp",

                    "object_count",

                    "risk",

                    "decision"

                ])

    def log(

        self,

        object_count,

        risk,

        decision

    ):

        with open(

            self.filename,

            "a",

            newline=""

        ) as f:

            writer = csv.writer(f)

            writer.writerow([

                datetime.now(),

                object_count,

                risk,

                decision

            ])