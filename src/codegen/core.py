from lark import Lark, Transformer, v_args
from src.constants import *
from . import literals, variables, functions, controls, expressions, operators, addtions

grammar: Lark = Lark.open(GRAMMAR_PATH, parser="lalr")


def codegen(code: str) -> str:
    tree: Lark = grammar.parse(code)
    cg = CodeGen()
    return cg.transform(tree)


@v_args(inline=True)
class CodeGen(Transformer):
    def __init__(self) -> None:
        super().__init__(self)

    number = literals.number
    string = literals.string
    list = literals.list
    dict = literals.dict
    true = literals.true
    false = literals.false
    null = literals.null

    var_decl = variables.var_decl
    var_auto_decl = variables.var_auto_decl
    var = variables.var

    param = functions.param
    param_list = functions.param_list
    func_decl = functions.func_decl
    func_call = functions.func_call
    ret_stmt = functions.ret_stmt

    if_stmt = controls.if_stmt
    for_stmt = controls.for_stmt
    while_stmt = controls.while_stmt

    block = expressions.block
    expr_stmt = expressions.expr_stmt
    semicolon = expressions.semicolon

    aug_assign = operators.aug_assign
    add = operators.add
    sub = operators.sub
    mul = operators.mul
    div = operators.div
    neg = operators.neg
    GT = operators.GT
    LT = operators.LT
    GE = operators.GE
    LE = operators.LE
    EQ = operators.EQ
    NE = operators.NE
    comparison = operators.comparison

    cpp_embed = addtions.cpp_embed
    import_c = addtions.import_c

    def start(self, *stmts) -> str:
        top_level = f'#include "{PYLIB_PATH}"\n'
        top_level += "\n".join(headers) + "\n" if headers else ""
        top_level += "\n".join(decls) + "\n" if decls else ""

        codes = top_level
        codes += "int main(void) {"
        for stmt in stmts:
            codes += f"{stmt}\n"
        codes += "}"

        return codes
