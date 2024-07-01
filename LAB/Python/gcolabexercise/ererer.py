def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_twin_primes(limit):
    """Find all twin primes less than the given limit."""
    twin_primes = []
    for i in range(3, limit, 2):
        if is_prime(i) and is_prime(i + 2):
            twin_primes.append((i, i + 2))
    return twin_primes

# Find twin primes less than 1000
twin_primes = find_twin_primes(1000)
print(twin_primes)