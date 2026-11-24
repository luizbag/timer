# ⏱️ Timer

[![Python 3.12+](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/downloads/)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Built with uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json)](https://github.com/astral-sh/uv)

A lightweight command-line countdown timer built with Python, Typer, Rich, and `playsound3`.

## ✨ Features

* **Simple CLI interface:** Start a countdown immediately with `timer <minutes>`
* **Rich terminal UI:** Live progress bar and remaining time display
* **Self-contained audio alert:** Plays a bundled alarm sound upon completion—works from any working directory

## 📋 Requirements

* Python 3.12 or newer
* [uv](https://docs.astral.sh/uv/) or [pipx](https://pipx.pypa.io/) (for global CLI installation)
* An audio output device supported by `playsound3`

## 📦 Installation

Install globally as an isolated CLI tool using **uv** (recommended):

```bash
uv tool install git+https://github.com/luizbag/timer.git
```

Or using **pipx**:

```bash
pipx install git+https://github.com/luizbag/timer.git
```

To install from a local clone instead:

```bash
git clone https://github.com/luizbag/timer.git
cd timer
uv tool install .
```

## 🚀 Usage

Start a 5-minute countdown from anywhere in your terminal:

```bash
timer 5
```

Example output:

```text
Timer ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Stop!
```

View all available options and help:

```bash
timer --help
```

## 🛠️ Development

Clone the repository and sync dependencies:

```bash
git clone https://github.com/luizbag/timer.git
cd timer
uv sync
```

Run from source:

```bash
uv run timer 1
```

Build source and wheel distributions:

```bash
uv build
```

## 📄 License

This project is licensed under the [GNU General Public License v3.0](LICENSE).