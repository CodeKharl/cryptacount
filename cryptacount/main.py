import argparse
from typing import Dict, List

import password_generator


def __parse_exact_constrains(exact_args: List[str]) -> Dict[str, int]:
    exact: Dict[str, int] = {}

    for item in exact_args:
        if "=" not in item:
            raise ValueError(f"Invalid format for --exact: {item}. Expected key=value")

        key, value = item.split("=")

        if key not in password_generator.CHAR_CLASSES:
            raise ValueError(f"Unknown character class: {key}")

        exact[key] = int(value)

    return exact


def __main() -> None:
    parser: argparse.ArgumentParser = argparse.ArgumentParser(
        description="CryptoCount: Password Entropy Analyzer"
    )

    parser.add_argument("--length", type=int, help="Password length", required=True)
    parser.add_argument(
        "--include",
        nargs="+",
        help="Character classes [lower, upper, digits, symbols]",
        required=True,
    )
    parser.add_argument(
        "--exact",
        nargs="*",
        default=[],
        help="Exact counts (e.g., digits=1, symbols=2)",
    )

    args: argparse.Namespace = parser.parse_args()

    length: int = args.length
    included: List[str] = args.include
    exact: Dict[str, int] = __parse_exact_constrains(args.exact)

    generated_password: str = password_generator.generate_password(
        length, included, exact
    )

    print("Generated Password:", generated_password)


if __name__ == "__main__":
    __main()
