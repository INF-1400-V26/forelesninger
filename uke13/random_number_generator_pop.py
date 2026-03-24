"""
Use generation of pseudorandom numbers as an example of a problem that requires both state and functionality.

Illustrate a procedural programming design.

Based on a linear congruential generator (LCG):

X_{n+1} = (a X_n + c) mod m

"""


def generate_random_number(
    modulus: int,
    multiplier: int,
    increment: int,
    seed: int,
):
    return (multiplier * seed + increment) % modulus


if __name__ == "__main__":
    # Lots of "free" variables
    modulus = 251
    multiplier = 213
    increment = 101
    current = 42

    for _ in range(50):
        # Need to save "current" to keep state
        current = generate_random_number(
            modulus=modulus, multiplier=multiplier, increment=increment, seed=current
        )
        print(current)
