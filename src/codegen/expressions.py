def lbrace(_) -> str:
    return "{"


def rbrace(_) -> str:
    return "}"


def expr_stmt(_, expr: str) -> str:
    if expr.strip() == "" or expr.strip == ";":
        return ""
    return f"{expr};"


def block(_, *stmts) -> str:
    return "\n".join(s for s in stmts if s)


def semicolon(_) -> str:
    return ";"
