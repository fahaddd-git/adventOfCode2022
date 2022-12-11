import typer
import requests
from rich import print
from rich.prompt import Prompt, Confirm
from pathlib import Path
import os
from dotenv import load_dotenv
from string import Template
import shutil

# Session token can be gotten from your browser
# It should be placed in a .env file to be read by this script to make requests.
load_dotenv()


URL = Template("https://adventofcode.com/2022/day/$num/input")
INPUT_FILE_NAMES = "input.txt"
TEMPLATE_FILENAME = "template.py"
TEMPLATE_FILEPATH = Path(__file__).parent.resolve() / TEMPLATE_FILENAME
TESTING_TEMPLATE_FILENAME = "testing_template.py"
TESTING_TEMPLATE_FILEPATH = Path(__file__).parent.resolve() / TESTING_TEMPLATE_FILENAME


def main(day_number: int = typer.Argument(..., min=0, max=25)):
    """
    Downloads input to specified folder. Set SESSION_COOKIE in .env file.
    """
    if day_number > 25 or day_number < 1:
        print("[bold red] :boom: Alert! Invalid day selection[/bold red]")
        raise typer.Exit(code=1)
    day_path = Path(__file__).parents[1].resolve() / str(day_number)
    SESSION_COOKIE = os.getenv("SESSION_COOKIE")
    if SESSION_COOKIE is None:
        print("[bold yellow] :ghost::person_pouting: SESSION_COOKIE not set in .env file[/bold yellow]")
        raise typer.Exit(code=1)

    try:
        os.mkdir(day_path)
        print("Creating folder")
    except FileExistsError:
        print(":warning::warning: Folder already exists...skipping folder creation :star: :star:")
    finally:
        with open(day_path / INPUT_FILE_NAMES, "w") as inputfile:
            req = requests.get(URL.substitute(num=day_number), cookies={"session": SESSION_COOKIE})
            if req.text == "Puzzle inputs differ by user.  Please log in to get your puzzle input.\n":
                print(":giraffe::pancakes:Something went wrong...input not received. Aborting.")
                raise typer.Exit(code=1)
            print(":camel::cactus: getting input")
            inputfile.write(req.text)
    print(
        f":bikini::grinning_face_with_smiling_eyes: input download completed to [bold blue]{day_path / INPUT_FILE_NAMES}[/bold blue]"
    )
    use_template = Confirm.ask(
        f"[blue_violet]Copy [pink3]{TEMPLATE_FILENAME}[/pink3] file to [misty_rose3]{day_path}[/misty_rose3]?[/blue_violet]"
    )
    if use_template:
        desired_template_filename = Prompt.ask(
            "[dark_cyan]:fire_extinguisher::eagle: Enter desired filename without .py[/dark_cyan]"
        )
        shutil.copy(TEMPLATE_FILEPATH, day_path / f"{desired_template_filename}.py")
        print("[bright_green]:zap::party_popper::vulcan_salute: Success! Template used[/bright_green]")

    use_tests = Confirm.ask(
        f"[blue_violet]:warning::warning:Use tests? You should...:fire_extinguisher::fire_extinguisher:[/blue_violet]"
    )

    if use_tests:
        desired_tests_filename = Prompt.ask(
            "[dark_cyan]:fire_extinguisher::eagle: Enter desired filename without .py[/dark_cyan]"
        )
        shutil.copy(TESTING_TEMPLATE_FILEPATH, day_path / f"{desired_tests_filename}.py")
        print("[bright_green]:zap::party_popper::vulcan_salute: Success! Template used[/bright_green]")

    print(f"[yellow1]:star::star: Ready to go at [dark_olive_green1]{day_path}[/dark_olive_green1]![/yellow1]")


def poetry_entrypoint():
    typer.run(main)


if __name__ == "__main__":
    typer.run(main)
