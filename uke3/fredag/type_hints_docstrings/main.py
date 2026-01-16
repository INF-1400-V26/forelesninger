"""The module provides access to an animal reserve simulation module."""


class Animal:
    """Represents a single animal in the enclosed animal reserve.

    Attributes:
        habitat (str): Preferred surrounding, e.g. Jungle or FreshWater.
        position (list[int]): Current [x, y] coordinates of the animal.
        Initializes to [0,0].
    """

    def __init__(self, habitat: str) -> None:
        self.habitat = habitat
        self.position: list[int] | None = [0, 0]

    def move_to(self, destination: list[int] | None) -> None:
        """Update the position of where the animal was last observed.
        Set to None if the animal is missing.
        """
        self.position = destination


if __name__ == "__main__":
    monkey = Animal("Jungle")
    monkey.move_to([4, 6])

    # monkey = Animal(900)
    # monkey.move_to("Norway")

    print(monkey.position)

    # prekode sudoku

    # type hints + mypy
    # docstrings + pylint
