
import sys
from setuptools import setup

requires = []  # type: list

if sys.version_info < (3, 2):
    requires.append("subprocess32")
if sys.version_info < (3, 4):
    requires.append("pathlib")

setup(
    name="ExplorerFromWSL",
    description="call explorer.exe from wsl shell by unix-style path",
    long_description="see (github)[https://github.com/ijknabla/explorer-from-wsl]",
    license="MIT License",
    version="1.0.0",
    url="https://github.com/ijknabla/explorer-from-wsl",
    author="ijknabla",
    author_email="ijknabla@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Topic :: Desktop Environment :: File Managers",
    ],
    py_modules=["explorer_from_wsl"],
    install_requires=requires,
    entry_points={
        'console_scripts': [
            'explorer = explorer_from_wsl:main',
        ],
    },
)
