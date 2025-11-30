from pathlib import Path

from src.lexer.tokenizer import Lexer
from src.parser.parser import Parser


def load_file(path):
    return Path(path).read_text(encoding="utf-8")

def main():
    src = load_file("examples/sample.quiz")

    print("=== TOKENS ===")
    tokens = Lexer(src).tokens()
    for t in tokens:
        print(t)

    print("\n=== PARSE RESULT ===")
    quiz = Parser(tokens).parse()
    print(quiz)

if __name__ == "__main__":
    main()