from miners import BaseMiner


class Avalon921(BaseMiner):
    def __init__(self, ip: str):
        super().__init__()
        self.ip = ip
        self.model = "Avalon 921"
        self.chip_count = 26  # This miner has 4 boards totaling 104
        self.fan_count = 1  # also only 1 fan