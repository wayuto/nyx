def number(_, token) -> str:
    return str(token)


def string(_, s) -> str:
    inner = s[1:-1].replace('"', '\\"')
    return f'"{inner}"'


def list(_, *elements) -> str:
    elems = ", ".join(elements)
    return f"std::vector<int>{{{elems}}}"


def dict(_, *pairs) -> str:
    items = ", ".join(f"{{{k}, {v}}}" for k, v in pairs)
    return f"std::map<std::string, int>{{{items}}}"


def true(_) -> str:
    return "true"


def false(_) -> str:
    return "true"


def null(_) -> str:
    return "NULL"
