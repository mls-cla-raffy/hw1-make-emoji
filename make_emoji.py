from emoji import emojize
import argparse
from rich import print
""" Print a chosen emoji and optional message from the command line. """


def build_parser() -> argparse.ArgumentParser:
    # replace desc with something more clear
    parser = argparse.ArgumentParser(description="Creates a parser that takes in two args: (1) [name] and (2) [args].")
    # replace default with whatever and provide proper help
    parser.add_argument("--name", default=":cigarette:", help="Your emoji alias goes here! (i.e. :cat_with_wry_smile:)")
    # replace default, and provide proper help
    parser.add_argument("--msg", default="Smoke Break", help="Your message goes here! Make sure to surround them in single ('') OR double (\"\") quotes!")
    return parser

def render_emoji(name: str, msg: str) -> str:
    """ Return the combined emoji + message string. """
    symbol = emojize(name, language="alias")
    # build f string here to format emoji output
    return f'{msg} {symbol}'

def main(args: argparse.Namespace) -> int:
    """
    Main function to be called with a Namespace object.
    This is to accommodate Jupyter notebook testing.
    """
    name = str(args.name)
    msg = str(args.msg)

    result = render_emoji(name,msg)
    print(f'\n\n{result}\n\n')

def main_with_return(args: argparse.Namespace) -> int:
    """
    Same as main but returns instead of prints.
    For testing purposes only!
    """
    name = str(args.name)
    msg = str(args.msg)

    result = render_emoji(name,msg)
    return f'\n\n{result}\n\n'

def run_from_cli():
    """
    Entry point for command-line execution.
    Handles CLI parsing.
    """
    parser = build_parser()
    args = parser.parse_args()
    main(args)

if __name__ == "__main__":
    # conventions or whatever
    # exit code 0 (see main) means success
    raise SystemExit(run_from_cli())