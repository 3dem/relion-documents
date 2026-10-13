import argparse
import pathlib
import subprocess
from textwrap import indent
import os
from typing import Iterable


def make_parser():
    """
    Returns the argument parser
    """
    parser = argparse.ArgumentParser(
        description="Produces a .rst documentation file describing the relion CLI, on stdout"
    )
    parser.add_argument(
        "relion_path",
        help="Path to the relion binary. For example /path/to/bin/relion",
        type=pathlib.Path,
    )
    return parser


def skip_to_options(code: Iterable[str]) -> Iterable[str]:
    """
    Skips all lines until the line containing +++ RELION, since the preceding lines
    are largely useless
    """
    found = False
    for line in code:
        if "+++ RELION" in line:
            found = True
        if found:
            yield line


def filter_traceback(code: Iterable[str]) -> Iterable[str]:
    """
    Remove the .cpp file traceback, since it contains the full user path
    """
    for line in code:
        if ".cpp, line" not in line:
            yield line


def main(relion_path: pathlib.Path):
    segments = [
        """
Command Line Reference
======================
"""
    ]
    binary_root = relion_path.parent
    os.environ["PATH"] += ":" + str(binary_root)
    for binary in binary_root.glob("relion_*"):
        try:
            result = subprocess.run(
                [binary.name], capture_output=True, encoding="utf-8", shell=True
            )
            # rst_output = docs_path / f'{binary}.rst'
            header = f"``{binary.stem}``"
            underline = "-" * (len(str(binary)) + 4)
            # Remove the /path/to/bin from all help
            raw_code = indent(result.stdout or result.stderr, prefix="    ").replace(
                str(binary_root), ""
            )
            code_lines = raw_code.splitlines()
            # Remove the .cpp path
            code_lines = list(filter_traceback(code_lines))
            if "+++ RELION" in raw_code:
                # The first lines of some MPI commands have unnecessary info about the local machine's MPI setup
                code_lines = skip_to_options(code_lines)
            code = "\n".join(code_lines)

            segments.append(
                f"""{header}
{underline}

.. code-block:: text

{code}
"""
            )
        except FileNotFoundError:
            pass
    print("\n".join(segments))


if __name__ == "__main__":
    parser = make_parser()
    args = parser.parse_args()
    main(**vars(args))
