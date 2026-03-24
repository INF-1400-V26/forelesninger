"""
Use generation of pseudorandom numbers as an example of a problem that requires both state and functionality.

Illustrate an object-oriented design.

Based on a linear congruential generator (LCG) with increment:

X_{n+1} = (a X_n + c) mod m

See table of good parameters:
https://www.ams.org/journals/mcom/1999-68-225/S0025-5718-99-00996-5/S0025-5718-99-00996-5.pdf

"""


class RandomNumberGenerator:
    def __init__(
        self,
        modulus: int,
        multiplier: int,
        increment: int,
        seed: int,
    ) -> None:
        # Encapsulation
        self._modulus = modulus
        self._multiplier = multiplier
        self._increment = increment
        self._current = seed

    def next(self) -> int:
        self._current = (self._multiplier * self._current + self._increment) % self._modulus
        return self._current


if __name__ == "__main__":
    # Create object that holds all parameters and state
    rng = RandomNumberGenerator(modulus=251, multiplier=213, increment=101, seed=42)

    # Cleanly generate numbers
    for _ in range(50):
        print(rng.next())
