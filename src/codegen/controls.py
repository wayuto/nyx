def if_stmt(_, cond, then_block, else_block=None) -> str:
    return f"if ({cond}) {then_block}" + (f" else {else_block}" if else_block else "")


def for_stmt(_, var, iterable, body) -> str:
    return f"for (auto {var} : {iterable}) {body}"


def while_stmt(_, cond, body) -> str:
    return f"while ({cond}) {body}"
