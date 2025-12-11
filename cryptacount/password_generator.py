import math
import secrets
from dataclasses import dataclass
from typing import Dict, List

# Character classes available
CHAR_CLASSES = {
    "lower": "abcdefghijklmnopqrstuvwxyz",
    "upper": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "digits": "0123456789",
    "symbols": "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~",
}


@dataclass
class PasswordArguments:
    length: int
    included_classes: List[str]
    exact_counts: Dict[str, int]


def multinomial_coefficient(counts: List[int]) -> int:
    """Compute multinomial coefficient: L! / (k1! * k2! * ... * km!)."""
    total = sum(counts)
    numer = math.factorial(total)
    denom = 1
    for c in counts:
        denom *= math.factorial(c)
    return numer // denom


def calculate_search_space(ps_args: PasswordArguments) -> int:
    """
    Calculate the total number of possible passwords (search space N).
    - length: password length L
    - included_classes: list of allowed character classes
    - exact_counts: mapping like {"digits": 2}
    """
    L = ps_args.length
    req_sum = sum(ps_args.exact_counts.values())
    if req_sum > L:
        raise ValueError("Sum of exact counts exceeds password length.")

    sizes = {k: len(CHAR_CLASSES[k]) for k in ps_args.included_classes}
    r = L - req_sum  # remaining positions

    # classes allowed to fill the remaining positions
    other_classes = [
        c for c in ps_args.included_classes if c not in ps_args.exact_counts
    ]
    C_other = sum(sizes[c] for c in other_classes) if other_classes else 0

    if r > 0 and C_other == 0:
        return 0  # impossible

    # multinomial placement ways
    counts_vector = list(ps_args.exact_counts.values()) + [r]
    place_ways = multinomial_coefficient(counts_vector)

    # fill choices for required positions
    required_fill = 1
    for cls, k in ps_args.exact_counts.items():
        required_fill *= sizes[cls] ** k

    # fill choices for remaining positions
    other_fill = (C_other**r) if r > 0 else 1

    return place_ways * required_fill * other_fill


def generate_password(ps_args: PasswordArguments) -> str:
    """Generate a password that satisfies exact constraints."""
    L = ps_args.length
    req_sum = sum(ps_args.exact_counts.values())
    if req_sum > L:
        raise ValueError("Sum of exact counts exceeds password length.")

    other_classes = [
        c for c in ps_args.included_classes if c not in ps_args.exact_counts
    ]
    other_pool = "".join(CHAR_CLASSES[c] for c in other_classes)

    chars = []

    # Add required characters
    for cls, k in ps_args.exact_counts.items():
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


def print_report(
    ps_args: PasswordArguments,
    search_space: int,
    entropy_bits: float,
    generated_pw: str,
) -> None:
    print(f"Length: {ps_args.length}")
    print(f"Included classes: {ps_args.included_classes}")
    print(f"Exact counts: {ps_args.exact_counts}")
    print(f"Search space (N): {search_space:,}")
    print(f"Entropy: {entropy_bits:.2f} bits")
    print(f"Sample password: {generated_pw}")


def __example() -> None:
    print("Example Run:\n")

    ps_args: PasswordArguments = PasswordArguments(
        8, ["lower", "upper", "digits"], {"digits": 2}
    )

    N = calculate_search_space(ps_args)
    pw = generate_password(ps_args)
    H = entropy_bits(N)

    print_report(ps_args, N, H, pw)


if __name__ == "__main__":
    __example()
