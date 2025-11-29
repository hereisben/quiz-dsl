# Quiz DSL – A Tiny Language for Generating Multiple-Choice Quizzes

## 1. Project Overview

This project is a small language (DSL – Domain Specific Language) for describing multiple-choice quizzes.

The long-term goal is:

- Start with a human-readable quiz language (`.quiz` files).
- Compile it into a structured format (JSON).
- Use that JSON to drive:
  - A command-line quiz runner.
  - A simple web-based quiz UI.
  - An AI-powered quiz generator that can read user content and propose quiz questions.

This project is a **practice project** to learn:

- How to design and evolve a DSL.
- How to build a mini compiler pipeline:
  - Lexer → Parser → AST → Semantic Checker → Interpreter.
- How to expose the compiler as:
  - A CLI tool.
  - A Flask web API.
- How to later plug in an AI model that produces quiz DSL from raw text.

There is **no SVG or graphics requirement**. The main outputs are **JSON** and **HTML**.

---

## 2. What This DSL Should Do

The Quiz DSL lets you declare a quiz and its questions in a clean, structured way.

Example (tentative):

```text
quiz {
  title: "CS152 Midterm Practice";
  description: "Questions about programming languages and lambda calculus.";

  question {
    text: "What does the Y combinator enable in lambda calculus?";
    choice: "It defines booleans.";
    choice: "It enables recursion.";
    choice: "It computes derivatives.";
    answer: 2;
    difficulty: "medium";
    tag: "lambda_calculus";
  }

  question {
    text: "Under static scoping, how is a variable reference resolved?";
    choice: "By the most recent stack frame.";
    choice: "By the lexical structure of the program.";
    choice: "Randomly.";
    answer: 2;
    difficulty: "easy";
    tag: "scope";
  }
}
```
