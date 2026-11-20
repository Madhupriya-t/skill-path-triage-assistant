"""Command-line entry point for Skill Path Triage Assistant."""

import argparse
from app.core import milestone_3


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        prog="skill-path-triage-assistant",
        description="Recommend relevant next skills for employee career development."
    )

    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("hello", help="Check that everything is working")

    recommend_parser = sub.add_parser(
        "recommend",
        help="Get an AI-powered next-skill recommendation"
    )

    recommend_parser.add_argument(
        "--skills",
        nargs="+",
        required=True,
        help="Enter the employee's existing skills"
    )

    args = parser.parse_args(argv)

    if args.command == "hello":
        print("Skill Path Triage Assistant is ready!")

    elif args.command == "recommend":
        print("\nCurrent skills:", ", ".join(args.skills))
        print("\nGenerating recommendation...\n")

        try:
            result = milestone_3(args.skills)
            print("AI Recommendation:")
            print(result)

        except Exception as error:
            print("Unable to generate recommendation:", error)


if __name__ == "__main__":
    main()