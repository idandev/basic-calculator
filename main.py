import sys

from intepreter import Interpreter
from lexer import Lexer
from parser import Parser


def main():
    print('->', end=' ')
    sys.stdout.flush()
    for line in sys.stdin:
        lexer = Lexer(line)
        tokens = lexer.lex()
        # for token in tokens:
        #     print(token)

        parser = Parser(tokens)
        ast = parser.parse()
        # print(ast)

        interpreter = Interpreter(ast)
        interpreter.run()
        print('->', end=' ')
        sys.stdout.flush()


if __name__ == '__main__':
    main()
