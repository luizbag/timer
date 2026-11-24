from importlib import resources

from typer.testing import CliRunner

from timer.app import app

runner = CliRunner()


def test_help():
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "Usage:" in result.stdout


def test_bundled_alarm_exists():
    alarm = resources.files("timer").joinpath("res/alarm.mp3")
    assert alarm.is_file()
