def if_stmt(_, cond, then_block, else_block=None) -> str:
    return f"if ({cond}) {then_block}" + (f" else {else_block}" if else_block else "")


def for_stmt(_, var, iterable, body) -> str:
    return f"for (auto {var} : {iterable}) {body}"


def while_stmt(_, cond, body) -> str:
    return f"while ({cond}) {body}"


def case_stmt(_, value, body) -> str:
    if value == "_":
        return f"default: {body}break;"
    return f"case {value}: {body}break;"


def match_stmt(_, target, *cases):
    return f"switch({target}) {{\n{''.join(cases)}}}"
