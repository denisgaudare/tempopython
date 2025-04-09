import os
from pathlib import Path

script_dir = os.path.dirname(__file__)

DATA = Path(script_dir) / "data"
DATA = DATA.absolute()

TEMPLATE = Path(script_dir) / "templates"
TEMPLATE = TEMPLATE.absolute()
