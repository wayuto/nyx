from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PYLIB_PATH = ROOT / "src" / "cpp" / "nyxlibs.hpp"
PYLIB_OUT = ROOT / "build" / "nyxlibs.o"
GRAMMAR_PATH = ROOT / "src" / "grammar.lark"
