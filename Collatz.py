# Implementacja problemu Collatza, gdzie dla danej liczby n: jeśli n jest parzyste,
# dzielimy ją przez 2, a jeśli nieparzyste, mnożymy przez 3 i dodajemy 1. Kontynuujemy do uzyskania 1.
# Przykład: collatz(6) zwróci [6, 3, 10, 5, 16, 8, 4, 2, 1].
import pytest


def collatz(n: int):
    collatz_list = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        collatz_list.append(n)
    return collatz_list


@pytest.mark.parametrize("test_input,expected",
                         [(6, [6, 3, 10, 5, 16, 8, 4, 2, 1]),
                          (3, [3, 10, 5, 16, 8, 4, 2, 1]),
                          (4, [4, 2, 1])])
def test_collatz(test_input, expected):
    assert collatz(test_input) == expected
