"""Command-line interface for the MSI Orchestrator."""

from __future__ import annotations

import argparse
import sys

from . import __version__
from .orchestrator import Orchestrator


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="msi-engine",
        description="AI-Led MSI Orchestrator.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"msi-engine {__version__}",
    )

    sub = parser.add_subparsers(dest="command", required=True)

    run = sub.add_parser("run", help="Execute a natural language workflow.")
    run.add_argument("--query", required=True, type=str, help="The user's request.")
    
    return parser


def main(argv: list[str] | None = None) -> None:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command != "run":
        parser.print_help()
        sys.exit(2)

    orchestrator = Orchestrator()
    sys.exit(orchestrator.run(args.query))


if __name__ == "__main__":
    main()
