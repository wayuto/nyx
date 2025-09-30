from src.constants import ctypes, decls


def param(_, name, typ="auto") -> str:
    return f"{ctypes.get(str(typ), "auto")} {name}"


def param_list(_, *params) -> str:
    return ", ".join(str(p) for p in params)


def func_decl(_, name, params="", ret=None, body="") -> str:
    ret_type = ctypes.get(str(ret), "auto") if ret else "auto"
    decl = f"{ret_type} {name}({params}) {body}"
    decls.append(decl)
    return ""


def func_call(_, name, *args) -> str:
    args_str = ", ".join(args)
    return f"{name}({args_str})"


def ret_stmt(_, expr) -> str:
    return f"return {expr};"
