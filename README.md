# Timer

A command-line countdown timer built with Python, Typer, Rich, and playsound3.

## Features

- Start a countdown for a specified number of minutes
- Display a live terminal progress bar
- Play `res/alarm.mp3` when the countdown finishes

## Requirements

- Python 3.12 or newer
- [uv](https://docs.astral.sh/uv/) (recommended)
- An audio device supported by playsound3

## Installation

Clone the repository and install it in a local virtual environment:

```bash
git clone https://github.com/luizbag/timer.git
cd timer
uv sync
```

Run from the repository root so the timer can find `res/alarm.mp3`.

## Usage

Start a countdown by passing the number of minutes:

```bash
uv run timer 5
```

This starts a five-minute countdown and prints a `Stop` message after the alarm finishes playing.

The CLI also provides built-in help:

```bash
uv run timer --help
```

## Development

Run the application directly from the source checkout:

```bash
uv run timer 1
```

Build source and wheel distributions with:

```bash
uv build
```

Generated packages are written to `dist/`.

## License

This project is licensed under the GNU General Public License v3.0. See [LICENSE](LICENSE).
