import glob
import os


def scan_db():
    # All files and directories ending with .db and that don't begin with a dot:
    return glob.glob(os.path.join("data", "*.db"))

