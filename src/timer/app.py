import time
from importlib.resources import as_file, files

import typer
from playsound3 import playsound
from rich.console import Console
from rich.progress import track

app = typer.Typer()
console = Console()


@app.command()
def start(minutes: int):
    """Starts a timer for the specified number of minutes."""
    console.print(f"Starting timer for {minutes} minutes")
    for i in track(range(minutes*60), description="Counting down..."):
        time.sleep(1)
    sound_resource = files("timer").joinpath("res", "alarm.mp3")
    with as_file(sound_resource) as sound_path:
        sound = playsound(sound_path, block=False)
    console.print("Stop", style="bold red")
    sound.wait()
