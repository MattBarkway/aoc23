import pathlib


def load_input(filename: str) -> list[str]:
    file_obj = pathlib.Path("../inputs") / filename
    with file_obj.open() as f:
        return f.readlines()


def load_raw(filename: str) -> str:
    file_obj = pathlib.Path("../inputs") / filename
    with file_obj.open() as f:
        return f.read()


def write_output(filename: str, lines: list[str]) -> None:
    file_obj = pathlib.Path("../outputs") / filename
    with file_obj.open("w") as f:
        return f.writelines("\n".join(lines))
