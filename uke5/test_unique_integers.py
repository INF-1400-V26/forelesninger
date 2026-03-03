import pytest  # pip install pytest
from unique_integers import UniqueIntegers


def test_unique_integers():
    my_ints = UniqueIntegers()
    my_ints.append(3)
    my_ints.append(4)
    my_ints.append(3)
    assert my_ints.as_list() == [3, 4]


def test_unique_int_invalid_input():
    my_ints = UniqueIntegers()
    my_ints.append(3)
    with pytest.raises(TypeError):
        my_ints.append("sushi")
