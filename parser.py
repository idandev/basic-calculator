from typing import List

from structs import (Token, AST, Program, ExpressionStatement, UnaryExpression, BinaryExpression, Literal, ASTNodeTypes,
                     TokenTypes)


class Parser:
    _tokens: List[Token]
    _index: int = 0

    @property
    def _current(self) -> Token:
        return self._tokens[self._index]

    @property
    def _previous(self) -> Token:
        return self._tokens[self._index - 1]

    def __init__(self, tokens: List[Token]):
        self._tokens = tokens

    def parse(self):
        ast: Program = Program(ASTNodeTypes.Program, [])

        while self._index < len(self._tokens):
            ast.body.append(self._plus_minus())

        return ast

    def _match(self, *args: TokenTypes):
        if value := (self._index < len(self._tokens) and self._current.type in args):
            self._index += 1
        return value

    def _plus_minus(self) -> Literal:
        expr = self._mult_div()

        while self._match(TokenTypes.PLUS, TokenTypes.MINUS):
            operator = self._previous
            right = self._plus_minus()
            expr = BinaryExpression(expr, right, operator)

        return expr

    def _mult_div(self) -> Literal:
        expr = self._unary()

        while self._match(TokenTypes.MULT, TokenTypes.DIV):
            operator = self._previous
            right = self._mult_div()
            expr = BinaryExpression(expr, right, operator)

        return expr

    def _unary(self) -> Literal:
        while self._match(TokenTypes.PLUS, TokenTypes.MINUS):
            operator = self._previous
            value = self._unary()
            return UnaryExpression(operator, value)

        return self._literal()

    def _literal(self) -> Literal:
        if self._match(TokenTypes.INT, TokenTypes.FLOAT):
            return Literal(self._previous.value)

        if self._match(TokenTypes.OPEN_PAREN):
            expr = self._plus_minus()
            if not self._match(TokenTypes.CLOSE_PAREN):
                raise Exception(f'Expected for close parentheses ")" at line {self._previous.line}.')
            return expr
