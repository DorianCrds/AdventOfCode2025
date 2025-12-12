class IdString:
    def __init__(self, value: int):
        self.id_as_str = str(value)
        self.errors = 0
        self.slices_list = []
        self.available_slicing_values = []

        self.get_availables_slicing_values()

    def get_availables_slicing_values(self) -> None:
        for slice_length in range(1, len(self.id_as_str)):
            result = len(self.id_as_str) / slice_length
            # print(f"on cut une str len : {len(self.id_as_str)} par {slice_length}, ça donne {result}")
            if result.is_integer():
                # print("ok")
                self.available_slicing_values.append(slice_length)

    def slice_id(self, slice_size: int) -> list[int]:
        return [int(self.id_as_str[i:i + slice_size]) for i in range(0, len(self.id_as_str), slice_size)]
