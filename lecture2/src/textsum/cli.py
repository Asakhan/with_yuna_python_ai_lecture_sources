from __future__ import annotations

import argparse
import sys
from typing import Optional
from src.common.errors import UserFacingError


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="textsum",
        description="Text summarization CLI (Step 1: basic input handling).",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    summarize = subparsers.add_parser(
        "summarize",
        help="Summarize input text (Step 1: echo input text).",
    )
    summarize.add_argument(
        "--text",
        type=str,
        required=True,
        help="Input text to summarize.",
    )
    return parser


def validate_text(text: str) -> str:
    cleaned = text.strip()
    if not cleaned:
        raise UserFacingError(
            "입력 텍스트가 비어 있습니다. 공백이 아닌 문장을 입력해 주세요."
        )
    return cleaned


def run_summarize(text: str) -> int:
    cleaned = validate_text(text)
    print(cleaned)
    return 0


def main(argv: Optional[list[str]] = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    parser = build_parser()
    try:
        args = parser.parse_args(argv)

        if args.command == "summarize":
            return run_summarize(args.text)

        raise UserFacingError("지원하지 않는 명령입니다.")

    except UserFacingError as e:
        print(f"[ERROR] {e}", file=sys.stderr)
        return e.exit_code


if __name__ == "__main__":
    raise SystemExit(main())