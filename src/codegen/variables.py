from src.constants import ctypes


def var(_, name) -> str:
    return str(name)


def var_decl(_, name, type_token, expr) -> str:
    t = str(type_token)
    decl = f"{ctypes.get(t, "auto")} {name} = {expr};"
    return decl


def var_auto_decl(_, name, expr) -> str:
    return f"auto {name} = {expr};"
