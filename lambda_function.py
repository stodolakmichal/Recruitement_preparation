# Sumowanie liczb: Napisz funkcję lambda, która przyjmuje dwie liczby jako argumenty i zwraca ich sumę.
# Następnie użyj tej funkcji do dodania dwóch dowolnych liczb.
import pytest

add_two_numbers = lambda x, y: x + y


def test_two_numbers():
    assert add_two_numbers(5, 6) == 11


# Mnożenie: Stwórz funkcję lambda, która przyjmuje trzy liczby jako argumenty i zwraca ich iloczyn.

multiply_three_numbers = lambda x, y, z: x * y * z


@pytest.mark.parametrize("x, y, z, expected_output", [(1, 2, 3, 6), (3, 4, 5, 60), (4, 5, 6, 120)])
def test_multiply_three_numbers(x, y, z, expected_output):
    assert multiply_three_numbers(x, y, z) == expected_output


# Filtracja listy: Użyj funkcji filter() i funkcji lambda,
# aby utworzyć nową listę zawierającą tylko liczby nieparzyste z podanej listy.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))


def test_odd_numbers():
    print(odd_numbers)
    assert odd_numbers == [1, 3, 5, 7, 9]
