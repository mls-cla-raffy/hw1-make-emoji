# CLA HW1 - Emoji Make

This is a hw designed to get more practice on setting up python environments!

## Setup

1. Setup your python environment with the name of your choice. The snippet below went with `testenv`:

```bash
python3 -m venv testenv
```

2. Install all dependencies.

```bash
pip3 install -r requirements.txt
```

> Dependencies included: [Ruff](https://docs.astral.sh/ruff/) (linter and formatter), [Jupyter](https://jupyter.org/), [Emoji](https://pypi.org/project/emoji/)

## Usage

The tool takes in two arguments through the CLI (Command Line Interface):
  1. `--name` indicates which emoji to append to your message. See this [cheat sheet](https://www.webfx.com/tools/emoji-cheat-sheet/) for all the emoji aliases.
  2. `--msg` lets you provide your own message!

Leaving it blank will run the script with default arguments. Below is an example output when providing a \<name\> and \<message\> argument.
```bash
> python3 -m make_emoji.py --name :cat_with_wry_smile: --msg "Hello everynyan~"

Hello everynyan 😼
```

> [Commands not working?](#troubleshooting)

## Performance

Using Python's `timeit` module:

```bash
25.8 ns ± 1.06 ns per loop (mean ± std. dev. of 7 runs, 10,000,000 loops each)
Average time: 0.0000 seconds
```

## Running Tests

```bash
pytest -q
```

## Troubleshooting

CLI commands not working? Make sure you're in a local python environment:

```bash
source testenv/bin/activate
```
