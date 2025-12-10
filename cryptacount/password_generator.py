import math
import secrets
from typing import Dict, List

# Character classes available
CHAR_CLASSES = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "symbols": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
}


def multinomial_coefficient(counts: List[int]) -> int:
    """Compute multinomial coefficient: L! / (k1! * k2! * ... * km!)."""
    total = sum(counts)
    numer = math.factorial(total)
    denom = 1
    for c in counts:
        denom *= math.factorial(c)
    return numer // denom


def calculate_search_space(
    length: int, included_classes: List[str], exact_counts: Dict[str, int]
) -> int:
    """
    Calculate the total number of possible passwords (search space N).
    - length: password length L
    - included_classes: list of allowed character classes
    - exact_counts: mapping like {"digits": 2}
    """
    L = length
    req_sum = sum(exact_counts.values())
    if req_sum > L:
        raise ValueError("Sum of exact counts exceeds password length.")

    sizes = {k: len(CHAR_CLASSES[k]) for k in included_classes}
    r = L - req_sum  # remaining positions

    # classes allowed to fill the remaining positions
    other_classes = [c for c in included_classes if c not in exact_counts]
    C_other = sum(sizes[c] for c in other_classes) if other_classes else 0

    if r > 0 and C_other == 0:
        return 0  # impossible

    # multinomial placement ways
    counts_vector = list(exact_counts.values()) + [r]
    place_ways = multinomial_coefficient(counts_vector)

    # fill choices for required positions
    required_fill = 1
    for cls, k in exact_counts.items():
        required_fill *= sizes[cls] ** k

    # fill choices for remaining positions
    other_fill = (C_other**r) if r > 0 else 1

    return place_ways * required_fill * other_fill


def generate_password(
    length: int, included_classes: List[str], exact_counts: Dict[str, int]
) -> str:
    """Generate a password that satisfies exact constraints."""
    L = length
    req_sum = sum(exact_counts.values())
    if req_sum > L:
        raise ValueError("Sum of exact counts exceeds password length.")

    other_classes = [c for c in included_classes if c not in exact_counts]
    other_pool = "".join(CHAR_CLASSES[c] for c in other_classes)

    chars = []

    # Add required characters
    for cls, k in exact_counts.items():
        for _ in range(k):
            chars.append(secrets.choice(CHAR_CLASSES[cls]))

    # Fill the remaining
    r = L - req_sum
    for _ in range(r):
        chars.append(secrets.choice(other_pool))

    # Shuffle to create a permutation
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def entropy_bits(N: int) -> float:
    """Compute entropy (bits)."""
    if N <= 0:
        return 0.0
    return math.log2(N)


def _print_report(length: int, included: List[str], exact: Dict[str, int]) -> None:
    pass


def __example() -> None:
    print("Example Run:\n")

    length = 8
    included = ["lower", "upper", "digits"]
    exact = {"digits": 2}

    N = calculate_search_space(length, included, exact)
    pw = generate_password(length, included, exact)
    H = entropy_bits(N)

    print(f"Length: {length}")
    print(f"Included classes: {included}")
    print(f"Exact counts: {exact}")
    print(f"Search space (N): {N:,}")
    print(f"Entropy: {H:.2f} bits")
    print(f"Sample password: {pw}")


if __name__ == "__main__":
    __example()
