from src.constants import headers


def cpp_embed(self, s) -> str:
    return s[1:-1].replace(r"\"", '"').replace(r"\n", "\n")


def import_c(self, s) -> str:
    path = s[1:-1].replace(r"\"", '"')
    headers.append(f'#include "{path}"')
    return ""
