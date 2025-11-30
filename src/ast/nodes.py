from dataclasses import dataclass
from typing import List, Optional, Union

# AST Node Definitions
@dataclass
class QuestionNode: # AST Node for a question
    text: str
    choices: List[str]
    answer: int
    difficulty: str
    tags: List[str]

class QuizNode: # AST Node for a quiz
    title: Optional[str] # Optional title of the quiz
    description: Optional[str] # Optional description of the quiz
    questions: List[QuestionNode] # List of questions in the quiz