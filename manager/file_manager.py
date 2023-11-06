import glob
import os


def scan_db():
    # All files and directories ending with .db and that don't begin with a dot:
    return [
        os.path.basename(filename)
        .replace(".db", "")
        for filename in
        glob.glob(os.path.join("data", "*.db"))
    ]


def validate_input_file(file):
    print(file.name)
    return file.name.split(".")[-1] == "json"
