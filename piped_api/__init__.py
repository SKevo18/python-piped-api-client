import typing as t

from pathlib import Path

from .client import PipedClient
from .models.comments import Comments



# For pdoc:
README_PATH = Path(__file__).parent.parent.absolute() / Path('README.md')
try:
    with open(README_PATH, 'r', encoding="UTF-8") as readme:
        __readme__ = readme.read()

except:
    __readme__ = "Failed to read README.md!"

__doc__ = __readme__



# Supress unused-import warnings:
if t.TYPE_CHECKING:
    _ = [PipedClient, Comments]
