import subprocess
import sys
import argparse
from pathlib import Path
from src.codegen import codegen
from src.constants import *


def load_code(path: str | None) -> str:
    if path is None:
        raise ValueError("No source file provided")
    p = Path(path)
    if p.is_file():
        return p.read_text()
    p2 = ROOT / path
    if p2.is_file():
        return p2.read_text()
    raise FileNotFoundError(path)


def compile_cpp(src: str, exe: str, opt: str = "-O2") -> None:
    o_file = Path(src).with_suffix(".o")
    subprocess.run(["g++", opt, "-o", o_file, "-c", src], check=True)
    subprocess.run(["g++", "-o", exe, o_file, PYLIB_OUT], check=True)
    o_file.unlink()
    print(f"Compiled: {exe}")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Nyx v0.1",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="source file to translate (if omitted, show this help)",
    )
    parser.add_argument(
        "-c",
        "--compile",
        action="store_true",
        help="invoke g++ to compile the generated C++ code",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="a.out",
        help="name of the output executable (default: a.out)",
    )
    parser.add_argument(
        "-O",
        "--opt",
        default="-O2",
        help="compiler optimization level (default: -O2)",
    )
    parser.add_argument(
        "-a",
        "--ast",
        action="store_true",
        help="generate and print the AST (for debugging)",
    )
    args = parser.parse_args()

    if args.source is None:
        parser.print_help()
        sys.exit(0)

    code = load_code(args.source)
    c_code = codegen(code)

    if args.ast:
        from src.codegen import grammar, preprocess

        tree = grammar.parse(preprocess(code))
        print(tree.pretty())
    else:
        with open("out.cpp", "w", encoding="utf-8") as f:
            f.write(c_code)
        print("Generated: out.cpp")

        if args.compile:
            compile_cpp(src="out.cpp", exe=args.output, opt=args.opt)


if __name__ == "__main__":
    main()
