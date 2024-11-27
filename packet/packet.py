from klv.misb_0601_19.metadata import Metadata


class Packet:
    def __init__(self, data) -> None:
        self.data = data
        self.metadata = list[Metadata]
