from argparse import ArgumentParser, Namespace
from typing import Dict, List

import password_generator


def __create_parser() -> ArgumentParser:
    parser: ArgumentParser = ArgumentParser(
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

    return parser


def __create_password_args(args: Namespace) -> password_generator.PasswordArguments:
    length: int = args.length
    included: List[str] = args.include
    exact: Dict[str, int] = __parse_exact_constrains(args.exact)

    return password_generator.PasswordArguments(length, included, exact)


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
    parser: ArgumentParser = __create_parser()

    args: Namespace = parser.parse_args()

    pw_args: password_generator.PasswordArguments = __create_password_args(args)

    search_space: int = password_generator.calculate_search_space(pw_args)
    entropy_bits: float = password_generator.entropy_bits(search_space)
    generated_pw: str = password_generator.generate_password(pw_args)

    password_generator.print_report(pw_args, search_space, entropy_bits, generated_pw)


if __name__ == "__main__":
    __main()
