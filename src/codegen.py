from lark import Lark, Transformer, v_args
from src.constants import *

grammar = Lark.open(GRAMMAR_PATH, parser="lalr")


def codegen(code: str) -> str:
    tree = grammar.parse(code)
    cg = CodeGenTransformer()
    return cg.transform(tree)


@v_args(inline=True)
class CodeGenTransformer(Transformer):
    def __init__(self) -> None:
        self.decls = []
        self.headers = []
        self.ctypes = {
            "int": "int",
            "float": "double",
            "str": "std::string",
            "bool": "int",
            "list": "std::vector<int>",
            "dict": "std::map<std::string, int>",
        }

    def number(self, token) -> str:
        return str(token)

    def string(self, s) -> str:
        inner = s[1:-1].replace('"', '\\"')
        return f'"{inner}"'

    def list(self, *elements) -> str:
        elems = ", ".join(elements)
        return f"std::vector<int>{{{elems}}}"

    def dict(self, *pairs) -> str:
        items = ", ".join(f"{{{k}, {v}}}" for k, v in pairs)
        return f"std::map<std::string, int>{{{items}}}"

    def var(self, name) -> str:
        return str(name)

    def var_decl(self, name, type_token, expr) -> str:
        t = str(type_token)
        decl = f"{self.ctypes.get(t, "double")} {name} = {expr};"
        self.decls.append(decl)
        return decl

    def var_auto_decl(self, name, expr) -> str:
        return f"auto {name} = {expr};"

    def param(self, name, typ) -> str:
        return f"{self.ctypes.get(str(typ), "double")} {name}"

    def param_list(self, *params) -> str:
        return ", ".join(params)

    def func_decl(self, name, params="", ret=None, body="") -> str:
        ret_type = self.ctypes.get(str(ret), "double") if ret else "double"
        decl = f"auto {name} = []({params}) -> {ret_type} {body};"
        self.decls.append(decl)
        return decl

    def func_call(self, name, *args) -> str:
        args_str = ", ".join(args)
        return f"{name}({args_str})"

    def ret_stmt(self, expr) -> str:
        return f"return {expr};"

    def cpp_embed(self, s) -> str:
        return s[1:-1].replace(r"\"", '"').replace(r"\n", "\n")

    def import_c(self, s) -> str:
        path = s[1:-1].replace(r"\"", '"')
        self.headers.append(f'#include "{path}"')
        return ""

    def aug_assign(self, name, op, expr) -> str:
        return f"{name} {op} {expr};"

    def expr_stmt(self, expr: str) -> str:
        if expr.strip() == "" or expr.strip == ";":
            return ""
        return f"{expr};"

    def block(self, *stmts):
        body = "\n".join(s for s in stmts if s)
        return "{{\n{}\n}}".format(body)

    def if_stmt(self, cond, then_block, else_block=None) -> str:
        return f"if ({cond}) {then_block}" + (
            f" else {else_block}" if else_block else ""
        )

    def for_stmt(self, var, iterable, body) -> str:
        return f"for (auto {var} : {iterable}) {body}"

    def while_stmt(self, cond, body) -> str:
        return f"while ({cond}) {body}"

    def semicolon(self) -> str:
        return ";"

    def add(self, a, b) -> str:
        return f"({a} + {b})"

    def sub(self, a, b) -> str:
        return f"({a} - {b})"

    def mul(self, a, b) -> str:
        return f"({a} * {b})"

    def div(self, a, b) -> str:
        return f"({a} / {b})"

    def neg(self, a) -> str:
        return f"(-{a})"

    def true(self) -> str:
        return "1"

    def false(self) -> str:
        return "0"

    def null(self) -> str:
        return "NULL"

    def GT(self, token) -> str:
        return ">"

    def LT(self, token) -> str:
        return "<"

    def GE(self, token) -> str:
        return ">="

    def LE(self, token) -> str:
        return "<="

    def EQ(self, token) -> str:
        return "=="

    def NE(self, token) -> str:
        return "!="

    def comparison(self, first, *rest) -> str:
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

    def start(self, *stmts) -> str:
        body_lines = []
        body_lines.extend(self.decls)
        i = 0
        while i < len(stmts):
            s = stmts[i]
            if (
                isinstance(s, str)
                and s.isidentifier()
                and i + 1 < len(stmts)
                and isinstance(stmts[i + 1], str)
                and stmts[i + 1].strip().startswith('"')
                and stmts[i + 1].strip().endswith('"')
            ):
                merged = f"{s}({stmts[i + 1]})"
                line = merged if merged.strip().endswith(";") else f"{merged};"
                body_lines.append(line)
                i += 2
                continue

            if isinstance(s, str) and s in self.decls:
                i += 1
                continue
            if isinstance(s, str):
                line = s if s.strip().endswith(";") else f"{s};"
                body_lines.append(line)
            i += 1
        top_level = f'#include "{PYLIB_PATH}"\n\n'
        top_level += "\n".join(self.headers) + "\n" if self.headers else ""
        code = top_level + "int main() {\n"
        for line in body_lines:
            code += line + "\n"
        code += "}\n"
        return code
