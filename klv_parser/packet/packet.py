from ..klv.misb_0601_19.metadata import Metadata


class Packet:
    def __init__(self, metadata: list[Metadata]) -> None:
        self.metadata = metadata
