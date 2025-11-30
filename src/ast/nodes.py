from dataclasses import dataclass, field
from token import OP
from typing import List, Optional, Union

# AST Node Definitions
@dataclass
class QuestionNode: # AST Node for a question
    text: str
    answer: int
    choices: List[str] = field(default_factory=list)
    tags: List[str] = field(default_factory=list)
    difficulty: Optional[str] = None

@dataclass
class QuizNode: # AST Node for a quiz
    questions: List[QuestionNode] = field(default_factory=list) # List of questions in the quiz
    title: Optional[str] = None # Optional title of the quiz
    description: Optional[str] = None # Optional description of the quiz