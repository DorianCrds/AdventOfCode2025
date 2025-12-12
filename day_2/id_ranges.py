class IdRange:
    def __init__(self, id_range: str):
        self.id_min = int(id_range.split("-")[0])
        self.id_max = int(id_range.split("-")[1])

    def __repr__(self):
        return f"{self.id_min}-{self.id_max}"
