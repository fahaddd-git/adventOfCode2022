import typer
import requests
from rich import print
from pathlib import Path
import os
from dotenv import load_dotenv
from string import Template

load_dotenv()


URL = Template("https://adventofcode.com/2022/day/$num/input")
INPUT_FILE_NAMES = "input.txt"


def main(day_number: int):
    """
    Downloads input to specified folder. Set SESSION_COOKIE in .env file.
    """
    if day_number > 25 or day_number < 1:
        print("[bold red] :boom: Alert! Invalid day selection[/bold red]")
        raise typer.Exit(code= 1)
    day_path = Path(__file__).parent.resolve() / str(day_number)
    SESSION_COOKIE = os.getenv('SESSION_COOKIE')
    if SESSION_COOKIE is None:
        print("[bold yellow] :ghost::person_pouting: SESSION_COOKIE not set in .env file[/bold yellow]")
        raise typer.Exit(code= 1)

    try:
        os.mkdir(day_path)
        print("Creating folder")
    except FileExistsError:
        print(":warning::warning: Folder already exists...continuing :star: :star:")
    finally:
        with open(day_path / INPUT_FILE_NAMES, "w") as inputfile:
            URL = "https://adventofcode.com/2022/day/1/input"
            req = requests.get(URL.substitute(num=day_number), cookies={"session": SESSION_COOKIE})
            if req.text == "Puzzle inputs differ by user.  Please log in to get your puzzle input.\n":
                print(":giraffe::pancakes:Something went wrong...input not received. Aborting.")
                raise typer.Exit(code=1)
            print(":camel::cactus: getting input")
            inputfile.write(req.text)
    print(f":bikini::grinning_face_with_smiling_eyes: input download completed to [bold blue]{day_path / INPUT_FILE_NAMES}[/bold blue]")
        
if __name__ == "__main__":
    typer.run(main)