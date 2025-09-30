def aug_assign(_, name, op, expr) -> str:
    return f"{name} {op} {expr};"


def add(_, a, b) -> str:
    return f"({a} + {b})"


def sub(_, a, b) -> str:
    return f"({a} - {b})"


def mul(_, a, b) -> str:
    return f"({a} * {b})"


def div(_, a, b) -> str:
    return f"({a} / {b})"


def neg(_, a) -> str:
    return f"(-{a})"


def GT(_, token) -> str:
    return ">"


def LT(_, token) -> str:
    return "<"


def GE(_, token) -> str:
    return ">="


def LE(_, token) -> str:
    return "<="


def EQ(_, token) -> str:
    return "=="


def NE(_, token) -> str:
    return "!="


def comparison(_, first, *rest) -> str:
    if not rest:
        return first
    left = first
    i = 0
    while i < len(rest):
        op = rest[i]
        right = rest[i + 1]
        left = f"({left} {op} {right})"
        i += 2
    return left
