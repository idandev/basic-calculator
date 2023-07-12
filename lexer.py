from typing import List

from structs import TokenTypes, Token


KEYS_TO_TOKENS = {
    '+': TokenTypes.PLUS,
    '-': TokenTypes.MINUS,
    '*': TokenTypes.MULT,
    '/': TokenTypes.DIV,
    '(': TokenTypes.OPEN_PAREN,
    ')': TokenTypes.CLOSE_PAREN
}


class Lexer:
    _offset: int = 0
    _string: str
    _line: int = 1

    @property
    def _current(self):
        return self._string[self._offset]

    @property
    def _previous(self):
        return self._string[self._offset - 1]

    def __init__(self, string: str):
        self._string = string

    def _lex_number(self) -> Token:
        number_str = ''
        did_dot_appear = False

        while self._current.isdigit() or self._current == '.':
            if self._current == '.':
                did_dot_appear = True
            number_str += self._current
            self._offset += 1

        if did_dot_appear:
            return Token(TokenTypes.FLOAT, float(number_str), self._line)
        else:
            return Token(TokenTypes.INT, int(number_str), self._line)

    def next(self) -> Token:
        if self._offset >= len(self._string):
            return Token(TokenTypes.EOF, None, self._line)

        if self._current == '\n':
            self._line += 1
            self._offset += 1
            return self.next()
        elif self._current.isspace():
            self._offset += 1
            return self.next()
        elif self._current.isdigit() or self._current == '.':
            return self._lex_number()
        elif self._current in KEYS_TO_TOKENS:
            self._offset += 1
            return Token(KEYS_TO_TOKENS[self._previous], self._previous, self._line)
        raise Exception(f'Invalid token "{self._current}".')

    def lex(self) -> List[Token]:
        tokens = []
        while (token := self.next()).type != TokenTypes.EOF:
            tokens.append(token)
        return tokens
