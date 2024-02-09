#!/usr/bin/env python3
# Inspired from https://github.com/kennethreitz/setup.py

from pathlib import Path
from setuptools import setup, find_packages

NAME = "auraloss"
DESCRIPTION = "Audio-focused loss functions in PyTorch"
URL = "https://github.com/csteinmetz1/auraloss"
EMAIL = "c.j.steinmetz@qmul.ac.uk"
AUTHOR = "Christian Steinmetz"
REQUIRES_PYTHON = ">=3.6.0"
VERSION = "0.4.0"

HERE = Path(__file__).parent

# try:
#     with open(HERE / "README.md", encoding="utf-8") as f:
#         long_description = "\n" + f.read()
# except FileNotFoundError:
#     long_description = DESCRIPTION

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=["auraloss"],
    install_requires=["torch", "numpy"],
    extras_require={"test": ["resampy"], "all": ["matplotlib", "librosa", "scipy"]},
    include_package_data=True,
    license="Apache License 2.0",
)
