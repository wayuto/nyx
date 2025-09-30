def expr_stmt(_, expr: str) -> str:
    if expr.strip() == "" or expr.strip == ";":
        return ""
    return f"{expr};"


def block(_, *stmts):
    body = "\n".join(s for s in stmts if s)
    return "{{\n{}\n}}".format(body)


def semicolon(_) -> str:
    return ";"
