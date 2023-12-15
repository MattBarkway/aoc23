import pathlib

import click


def load_template(path: pathlib.Path):
    with path.open() as f:
        return f.read()


def write_template(path: pathlib.Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w") as f:
        return f.write(content)


def year_exists(year: int):
    return pathlib.Path(str(year)).exists()


def generate_year_template(year: int, day=1):
    templates = {
        pathlib.Path("aoc")
        / "templates"
        / "test_{day}.py.tmpl": pathlib.Path("{year}")
        / "python"
        / "tests"
        / "test_{day}.py",
        pathlib.Path("aoc")
        / "templates"
        / "day_{day}.py.tmpl": pathlib.Path("{year}")
        / "python"
        / "day_{day}.py",
    }
    copies = {
        pathlib.Path("aoc")
        / "templates"
        / "loading.py": pathlib.Path("{year}")
        / "python"
        / "loading.py",
        pathlib.Path("aoc")
        / "templates"
        / "pyproject.toml": pathlib.Path("{year}")
        / "python"
        / "pyproject.toml",
    }
    extras = [pathlib.Path("{year}") / "inputs" / "{day}.txt"]

    for templ, out in templates.items():
        templ_str = load_template(templ)
        formatted = templ_str.format(day=day)
        formatted_path = str(out).format(year=year, day=day)
        out_path = pathlib.Path(formatted_path)
        if out_path.exists():
            continue
        write_template(out_path, formatted)

    for copy, out in copies.items():
        copy_str = load_template(copy)
        formatted_path = str(out).format(year=year)
        out_path = pathlib.Path(formatted_path)
        if out_path.exists():
            continue
        write_template(out_path, copy_str)

    for extra in extras:
        formatted_path = str(extra).format(year=year, day=day)
        out_path = pathlib.Path(formatted_path)
        if out_path.exists():
            continue
        write_template(pathlib.Path(out_path), " ")


def generate_day_template(day: int, year: int):
    generate_year_template(year, day)


@click.command()
@click.option("--year", "-y", help="Year number")
@click.option("--day", "-d", help="Day number")
def run(year=None, day=None):
    if not (year and day):
        print("Please a day and year")

    generate_day_template(day, year)


if __name__ == "__main__":
    run()
