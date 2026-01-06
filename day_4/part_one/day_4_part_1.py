with open("../input.txt", "r") as f:
    raw_content_lines = f.readlines()

# for line in raw_content_lines:
#     print(list(line.strip()))
# print(raw_content_lines)

class Position:
    def __init__(self, x: int, y: int, value: str):
        self.row = x
        self.col = y
        self.is_roll = True if value == "@" else False
        self.adjacent_rolls = 0
        self.adjacent_spots = []

    def __repr__(self):
        return f"({self.row}, {self.col}, {self.is_roll})"


class Grid:
    def __init__(self, raw_content: list[str]):
        self.content: list[str] = [content_line.strip() for content_line in raw_content]
        # print(self.content)
        self.grid_list: list[Position] = []
        self.rows_count = 0
        self.columns_count = 0
        self.counter = 0

        self._get_rows_count()
        self._get_columns_count()
        self._get_grid_list()
        self._process_grid()

        # print(self.content)
        # print(self.rows_count)
        # print(self.columns_count)
        # print(self.grid_list)

    def _get_rows_count(self) -> None:
        self.rows_count = len(self.content)

    def _get_columns_count(self):
        if self.content:
            self.columns_count = len(self.content[0])

    def _get_grid_list(self):
        for i in range(len(self.content)):
            for j in range(len(self.content[i])):
                new_position = Position(i, j, self.content[i][j])
                # print(self.content[j])
                # print(type(self.content[j]))
                self.grid_list.append(new_position)

    @staticmethod
    def is_accessible(position: Position) -> bool:
        if position.adjacent_rolls < 4:
            return True
        return False

    def _process_grid(self):
        for position in self.grid_list:
            self.count_adjacent_rolls(position)
            # print(position.adjacent_rolls)

        for position in self.grid_list:
            # print(self.counter)
            if self.is_accessible(position) and position.is_roll:
                self.counter += 1
            # print(self.counter)

    def count_adjacent_rolls(self, position: Position):
        self.get_available_adjacent_spots(position)

        for spot in position.adjacent_spots:
            if isinstance(spot, tuple):
                for grid_element in self.grid_list:
                    if grid_element.row == spot[0] and grid_element.col == spot[1] and grid_element.is_roll:
                        position.adjacent_rolls += 1

    def get_available_adjacent_spots(self, position: Position):
        # Top line spots
        position.adjacent_spots.append((position.row - 1, position.col - 1))
        position.adjacent_spots.append((position.row - 1, position.col))
        position.adjacent_spots.append((position.row - 1, position.col + 1))

        # Same line spots
        position.adjacent_spots.append((position.row, position.col - 1))
        position.adjacent_spots.append((position.row, position.col + 1))

        # Bottom line spots
        position.adjacent_spots.append((position.row + 1, position.col - 1))
        position.adjacent_spots.append((position.row + 1, position.col))
        position.adjacent_spots.append((position.row + 1, position.col + 1))

        if position.row == 0:
            position.adjacent_spots[0] = "-"
            position.adjacent_spots[1] = "-"
            position.adjacent_spots[2] = "-"

        if position.row == self.rows_count - 1:
            position.adjacent_spots[5] = "-"
            position.adjacent_spots[6] = "-"
            position.adjacent_spots[7] = "-"

        if position.col == 0:
            position.adjacent_spots[0] = "-"
            position.adjacent_spots[3] = "-"
            position.adjacent_spots[5] = "-"

        if position.col == self.columns_count - 1:
            position.adjacent_spots[2] = "-"
            position.adjacent_spots[4] = "-"
            position.adjacent_spots[7] = "-"

        # print(position.adjacent_spots)



grid = Grid(raw_content_lines)
print(grid.counter)