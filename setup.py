from distutils.core import setup
from distutils.extension import Extension
setup(
  name = "StupidSheet",
  version="0.2",
  description="A Spreadsheet.",
  author="Roberto Alsina",
  author_email="ralsina@kde.org",
  url="http://pycs.net/lateral",
  scripts=["ssheet.py"],
  packages= ["ssheet"]
)

