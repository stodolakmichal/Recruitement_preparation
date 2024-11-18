def verify_if_prime_number(number: int):
    if number < 2:
        return False
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# print(is_prime(4))
print(verify_if_prime_number(6))
