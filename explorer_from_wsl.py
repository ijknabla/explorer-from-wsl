
import sys
from pathlib import PosixPath, PureWindowsPath

if sys.version_info < (3, 2):
    import subprocess32 as sp
else:
    import subprocess as sp


def posix2windows(posixpath):
    # type: (PosixPath) -> PureWindowsPath
    wslpath = sp.check_output(
        ["wslpath", "-w", str(posixpath)],
        universal_newlines=True,
    )
    return PureWindowsPath(wslpath)


def call_explorer(posixpath):
    # type: (PosixPath) -> int
    return sp.call(
        ["explorer.exe", str(posix2windows(posixpath))],
    )


def main():
    # type: () -> None
    import argparse
    parser = argparse.ArgumentParser(
        description="Windows Explorer"
    )

    parser.add_argument(
        "posixpath",
        nargs='?',
        default='.',
    )

    args = parser.parse_args()

    call_explorer(
        posixpath=PosixPath(args.posixpath)
        )


if __name__ == "__main__":
    main()
