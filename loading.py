import pathlib


def load_input(filename):
    file_obj = pathlib.Path("inputs") / filename
    with file_obj.open() as f:
        return f.readlines()


def write_output(filename, lines):
    file_obj = pathlib.Path("outputs") / filename
    with file_obj.open("w") as f:
        return f.writelines("\n".join(lines))
