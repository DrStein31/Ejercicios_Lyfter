def is_prime(number):
    if number < 2:
        return False
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True


def get_prime_numbers(numbers):
    prime_numbers = []

    for number in numbers:
        if is_prime(number):
            prime_numbers.append(number)
    return prime_numbers


numbers = [1, 2, 4, 6, 7, 13, 9, 67]
result = get_prime_numbers(numbers)

print (numbers)
print (result)