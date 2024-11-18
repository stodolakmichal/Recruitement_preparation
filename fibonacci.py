import pytest


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib = fibonacci(n - 1) + fibonacci(n - 2)
        return fib


@pytest.mark.parametrize("input, output", [(3, 2), (4, 3), (5, 5)])
def test_fibonacci(input, output):
    assert fibonacci(input) == output
