def isprime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ispalindrome(n):
    """Check if a number is a palindrome."""
    return str(n) == str(n)[::-1]

def isperfect(n):
    """Check if a number is perfect."""
    if n <= 0:
        return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

