from dataclasses import dataclass
from typing import List, Optional

from src.ast.nodes import QuestionNode, QuizNode


@dataclass
class Token:
    type: str
    lexeme: str
    line: int
    col: int

class ParserError(SyntaxError):
    pass

class Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.i = 0

    def _peek(self) -> Optional[Token]:
        return self.tokens[self.i] if self.i < len(self.tokens) else None
    
    def _match(self, *types: str) -> Optional[Token]:
        tok = self._peek()
        if tok and tok.type in types:
            self.i += 1
            return tok
        return None
    
    def _expect(self, *type: str, msg: str = "") -> Token:
        tok = self._match(*type)
        if not tok:
            got = self._peek()
            where = f" at line {got.line}, col {got.col}" if got else ""
            raise ParserError(f"Expected {type} {msg}, got {got.type if got else 'EOF'}{where}")
        return tok
    
    def parse(self) -> QuizNode:
        node = self._parse_quiz()
        extra = self._peek()
        if extra and extra.type != "EOF":
            raise ParserError(f"Extra tokens after quiz block at line {extra.line}, col {extra.col}")
        return node
    
    def _parse_quiz(self) -> QuizNode:
        self._expect("QUIZ", msg="to start quiz block")
        self._expect("LBRACE", msg="after 'quiz'")

        title = None
        description = None

        while True:
            tok = self._peek()
            if not tok:
                break
            if (tok.type == "TITLE" and title is None):
                self._expect("TITLE")
                self._expect("COLON", msg="after title")
                title = self._expect("STRING").lexeme
                self._expect("SEMI", msg="after title string")
            elif (tok.type == "DESCRIPTION" and description is None):
                self._expect("DESCRIPTION")
                self._expect("COLON", msg="after title")
                description = self._expect("STRING").lexeme
                self._expect("SEMI", msg="after description string")
            else:
                break
        
        questions = []
        while True:
            tok = self._peek()
            if not tok or tok.type in ("RBRACE", "EOF"):
                break
            questions.append(self._parse_question())

        self._expect("RBRACE", msg="to close quiz block")
        return QuizNode(title=title, description=description, questions=questions)
    
    def _parse_question(self) -> QuestionNode:
        self._expect("QUESTION", msg="to start question block")
        self._expect("LBRACE", msg="after 'question'")
        text = None
        choices = []
        answer = None
        difficulty = None
        tags = []
        while True:
            tok = self._peek()
            if not tok or tok.type in ("RBRACE", "EOF"):
                break
            elif (tok.type == "TEXT" and text is None):
                text = self._parse_text_stmt()
            elif (tok.type == "CHOICE"):
                choices.append(self._parse_choice_stmt())
            elif (tok.type == "ANSWER" and answer is None):
                answer = int(self._parse_answer_stmt())
            elif (tok.type == "DIFFICULTY" and difficulty is None):
                difficulty = self._parse_difficulty_stmt()
            elif (tok.type == "TAG"):
                tags.append(self._parse_tag_stmt())
            else:
                raise ParserError(f"Unexpected token {tok.type} in question body at line {tok.line}, col {tok.col}")
        self._expect("RBRACE", msg="to close question block")
        return QuestionNode(text=text, choices=choices, answer=answer, difficulty=difficulty, tags=tags)
        

    def _parse_text_stmt(self) -> str:
        self._expect("TEXT", msg="to open text stmt")
        self._expect("COLON", msg="after 'text'")
        s = self._expect("STRING", msg="for question content").lexeme
        self._expect("SEMI", msg="to close text stmt")
        return s
    
    def _parse_choice_stmt(self) -> str:
        self._expect("CHOICE", msg="to open choice stmt")
        self._expect("COLON", msg="after 'choice'")
        s = self._expect("STRING", msg="for choice content").lexeme
        self._expect("SEMI", msg="to close choice stmt")
        return s
    
    def _parse_answer_stmt(self) -> str:
        self._expect("ANSWER", msg="to open answer stmt")
        self._expect("COLON", msg="after 'answer'")
        s = self._expect("INT", msg="for answer index").lexeme
        self._expect("SEMI", msg="to close answer stmt")
        return s

    def _parse_difficulty_stmt(self) -> str:
        self._expect("DIFFICULTY", msg="to open difficulty stmt")
        self._expect("COLON", msg="after 'difficulty'")
        s = self._expect("STRING", msg="for difficulty level").lexeme
        self._expect("SEMI", msg="to close difficulty stmt")
        return s
        
    def _parse_tag_stmt(self) -> str:
        self._expect("TAG", msg="to open tag stmt")
        self._expect("COLON", msg="after 'tag'")
        s = self._expect("STRING", msg="for tag content").lexeme
        self._expect("SEMI", msg="to close tag stmt")
        return s
    
