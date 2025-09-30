from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

PYLIB_PATH: str = ROOT / "src" / "cpp" / "nyxlibs.hpp"
PYLIB_OUT: str = ROOT / "build" / "nyxlibs.o"
GRAMMAR_PATH: str = ROOT / "src" / "grammar.lark"


ctypes: dict[str:str] = {
    "int": "int",
    "float": "double",
    "str": "std::string",
    "bool": "bool",
    "list": "std::vector",
    "dict": "std::map",
}

decls: list[str] = []
headers: list[str] = []
