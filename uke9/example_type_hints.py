def concatenate(a, b):
    # "Concatenate" possible for many data types

    pass


def concatenate_str(a: str, b: str) -> str:
    return a + b


def concatenate_int(a: int, b: int) -> int:
    return int(str(a) + str(b))


if __name__ == "__main__":
    # Intentionally use wrong types
    print(concatenate_str(1, "2"))
