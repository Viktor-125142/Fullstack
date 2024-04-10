def find_primes(a: int, b: int) -> list[int]:
    primes = []
    for i in range(max(2, a), b + 1):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


if __name__ == '__main__':
    print(find_primes(2, 10))
    print(x)
