import pytest


def silnia(n: int):
    temp_var = 1
    if n == 0 or n == 1:
        return temp_var
    for i in range(2, n + 1):
        temp_var *= i
    return temp_var


def silnia_recursive(n: int):
    if n == 0:
        return 1
    factorial = n * silnia_recursive(n - 1)
    return factorial


@pytest.mark.parametrize("input, output", [(3, 6), (4, 24), (5, 120)])
def test_silnia(input, output):
    assert silnia(input) == output
