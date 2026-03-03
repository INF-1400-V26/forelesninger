class UniqueIntegers:
    def __init__(self):
        self.list = []

    def append(self, number: int):
        if not isinstance(number, int):
            raise (TypeError(f"Input {number} is not an int"))
        if number not in self.list:
            self.list.append(number)

    def as_list(self) -> list[int]:
        return self.list
