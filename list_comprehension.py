import pytest

list_example = [1, 2, 3, 4, 5]
words = ["apple", "banana", "cherry"]


# Napisz list comprehension, który dla danej listy liczb zwróci nową listę z podwojonymi wartościami.

def doubled_list(list_of_numbers: list):
    doubled = [x * 2 for x in list_of_numbers]
    return doubled


def test_doubled_list():
    assert doubled_list(list_example) == [2, 4, 6, 8, 10]


# Napisz list comprehension, który zwróci listę zawierającą tylko liczby parzyste z danej listy.

def only_even_numbers(list_of_numbers: list):
    even_numbers = [x for x in list_of_numbers if x % 2 == 0]
    return even_numbers


def test_only_even_numbers():
    assert only_even_numbers(list_example) == [2, 4]


# Napisz list comprehension, który dla danej listy słów zwróci listę ich długości.

def len_of_words(words_list: list):
    words_length = [len(word) for word in words_list]
    return words_length


def test_len_of_words():
    assert len_of_words(words) == [5, 6, 6]


# Napisz list comprehension, który zwróci listę liczb od 1 do 50, które są podzielne przez 3.

def list_of_numbers_divisible_by_three():
    return [x for x in range(1, 50) if x % 3 == 0]


def test_list_of_numbers_divisible_by_three():
    assert list_of_numbers_divisible_by_three() == [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48]


# Napisz list comprehension, który zamieni wszystkie litery w liście słów na wielkie litery.
def letters_to_upper(list_of_words: list):
    return [word.upper() for word in list_of_words]


def test_letters_to_upper():
    assert letters_to_upper(words) == ["APPLE", "BANANA", "CHERRY"]


# Napisz list comprehension, który wygeneruje wszystkie możliwe kombinacje dwóch list liczb (produkt kartezjański).
# Input: [1, 2], [3, 4]
# Output: [(1, 3), (1, 4), (2, 3), (2, 4)]

first_list = [1, 2]
second_list = [3, 4]
output = [(1, 3), (1, 4), (2, 3), (2, 4)]


def cartezian_product(first_list, second_list):
    return [(x, y) for x in first_list for y in second_list]


def test_cartezian_product():
    cartezian_product(first_list, second_list) == output


# Napisz list comprehension, który zwróci listę kwadratów liczb z przedziału od 1 do 10.

def square_numbers():
    return [x ** 2 for x in range(1, 11)]


def test_square_numbers():
    assert square_numbers() == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Napisz list comprehension, który odwróci kolejność liter w każdym słowie w liście.

def reversed_words(words):
    return [word[::-1] for word in words]


def test_reversed_words():
    assert reversed_words(words) == ["elppa", "ananab", "yrrehc"]


# Napisz list comprehension, który zwróci wszystkie wielokrotności liczby 5 z listy liczb.

def multiplied_numbers(list_example):
    return [x for x in list_example if x % 5 == 0]


def test_multiplied_numbers():
    assert multiplied_numbers(list_example) == [5]


# Napisz list comprehension, który stworzy listę zawierającą zagnieżdżone listy (macierz) dla liczb od 1 do 3,
# gdzie każda wewnętrzna lista zawiera liczby od 1 do 3.

def matrix_list():
    return [[x for x in range(1, 4)] for _ in range(3)]


def test_matrix_list():
    assert matrix_list() == [[1, 2, 3], [1, 2, 3], [1, 2, 3]]


# Napisz list comprehension, który zwróci tylko te słowa z listy, które zaczynają się na literę "a".
# Input: ["apple", "banana", "avocado", "cherry"]
# Output: ["apple", "avocado"]

input = ["apple", "banana", "avocado", "cherry"]
output = ["apple", "avocado"]


def words_starting_with_a(input):
    return [word for word in input if word[0] == "a"]


def test_words_starting_with_a():
    assert words_starting_with_a(input) == output


# Napisz list comprehension, który usunie duplikaty z listy liczb i zwróci listę unikalnych liczb.
# Input: [1, 2, 2, 3, 4, 4, 5]
# Output: [1, 2, 3, 4, 5]
# !!! W tym bez sensu uzywac list comprehension!!!

input = [1, 2, 2, 3, 4, 4, 5]
output = [1, 2, 3, 4, 5]


def numbers_without_duplicates(list_of_numbers: list):
    return list(set(list_of_numbers))


def test_numbers_without_duplicates():
    numbers_without_duplicates(input) == output
