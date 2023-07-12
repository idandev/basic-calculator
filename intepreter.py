from typing import Any

from structs import Program, ASTNodeTypes, BinaryExpression, TokenTypes, AST, UnaryExpression


class Interpreter:
    _ast: Program

    def __init__(self, ast):
        self._ast = ast

    def run(self):
        for expr in self._ast.body:
            print(self._run_expr(expr))

    def _run_expr(self, expr: AST):
        match expr.type:
            case ASTNodeTypes.Literal:
                return expr.value
            case ASTNodeTypes.BinaryExpression:
                return self._run_binary(expr)
            case ASTNodeTypes.UnaryExpression:
                return self._run_unary(expr)
            case other:
                raise Exception('Unknown type of expression.')

    def _run_binary(self, expr: BinaryExpression) -> Any:
        left = self._run_expr(expr.left)
        right = self._run_expr(expr.right)
        match expr.operator.type:
            case TokenTypes.PLUS:
                return left + right
            case TokenTypes.MINUS:
                return left - right
            case TokenTypes.MULT:
                return left * right
            case TokenTypes.DIV:
                return left / right
            case other:
                raise Exception('Operator not supported')

    def _run_unary(self, expr: UnaryExpression) -> Any:
        value = self._run_expr(expr.value)
        match expr.operator.type:
            case TokenTypes.PLUS:
                return value
            case TokenTypes.MINUS:
                return -value
            case other:
                raise Exception('Operator not supported')
