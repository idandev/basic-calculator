from dataclasses import dataclass
from typing import Any, List
from enum import auto, IntEnum


class TokenTypes(IntEnum):
    INT = auto()
    FLOAT = auto()
    PLUS = auto()
    MINUS = auto()
    MULT = auto()
    DIV = auto()
    OPEN_PAREN = auto()
    CLOSE_PAREN = auto()
    EOF = auto()


@dataclass()
class Token:
    type: TokenTypes
    value: Any
    line: int


class ASTNodeTypes(IntEnum):
    Program = auto()
    ExpressionStatement = auto()
    BinaryExpression = auto()
    UnaryExpression = auto()
    Literal = auto()


@dataclass()
class AST:
    type: ASTNodeTypes


@dataclass()
class Program(AST):
    body: List[AST]


@dataclass()
class ExpressionStatement(AST):
    expression: AST


@dataclass()
class Literal(AST):
    value: Any

    def __init__(self, value: Any):
        self.type = ASTNodeTypes.Literal
        self.value = value


@dataclass()
class BinaryExpression(AST):
    left: Literal
    right: Literal
    operator: Token

    def __init__(self, left: Literal, right: Literal, operator: Token):
        self.type = ASTNodeTypes.BinaryExpression
        self.left = left
        self.right = right
        self.operator = operator


@dataclass()
class UnaryExpression(Literal):
    operator: Token

    def __init__(self, operator: Token, value: Any):
        self.type = ASTNodeTypes.UnaryExpression
        self.operator = operator
        self.value = value
