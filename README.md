# Learning Python End to End

A chapter-by-chapter Python learning repository with hands-on scripts, inline comments, and small projects. Each folder covers one topic so you can learn concepts in order and run examples as you go.

## Prerequisites

- [Python 3](https://www.python.org/downloads/) (3.8 or newer recommended)
- A terminal or code editor (e.g. [VS Code](https://code.visualstudio.com/))

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/aashwinshukla/learning-python-end-to-end.git
   cd learning-python-end-to-end
   ```

2. Run any script with Python:

   ```bash
   python Chapter-01-Introduction/hello.py
   ```

   On some systems you may need `python3` instead of `python`.

## Repository Structure

| Chapter | Topic | Key Files |
|---------|-------|-----------|
| **Chapter 01** — Introduction | Hello World, variables, data types | `hello.py`, `variable-and-data-type.py`, `shape.py` |
| **Chapter 02** — Strings | Working with strings and numbers | `working_with_string.py`, `working_with_number.py` |
| **Chapter 03** — Input | User input | `getting-input.py` |
| **Chapter 04** — Building | First mini projects | `basic-calculator.py`, `mad-libs.py` |
| **Chapter 05** — Lists | Lists, tuples, list functions | `list.py`, `tuples.py`, `list-functions.py` |
| **Chapter 06** — Functions | Defining and using functions | `functions.py`, `exponent.py` |
| **Chapter 07** — Statements | Conditionals and return values | `if.py`, `if-comparision.py`, `return.py` |
| **Chapter 08** — Building Part 02 | Improved calculator | `better-calculator.py` |
| **Chapter 09** — Dictionary | Key–value data structures | `dictionary.py` |
| **Chapter 10** — Loops | `for` and `while` loops | `for.py`, `while.py` |
| **Chapter 11** — Building Part 03 | Guessing game, custom translator | `guess.py`, `translator.py` |
| **Chapter 12** — 2D Lists & Nested Loops | Multi-dimensional lists | `2dlist.py`, `nestedloop.py` |
| **Chapter 13** — Try and Except | Error handling | `tryExcept.py` |

## Suggested Learning Path

Work through chapters **01 → 13** in order. Each script is self-contained and includes comments explaining the concepts.

**Highlights along the way:**

- **Mad Libs** (`Chapter-04-Building/mad-libs.py`) — combine `input()` and string concatenation
- **Guess the word** (`Chapter-11-Building_Part_03/guess.py`) — `while` loops, conditions, and game logic
- **Vowel translator** (`Chapter-11-Building_Part_03/translator.py`) — functions and string iteration
- **Error handling** (`Chapter-13-Try-And-Except/tryExcept.py`) — `try` / `except` for invalid input

## Example

```bash
python Chapter-11-Building_Part_03/translator.py
```

Enter a phrase when prompted; vowels are replaced with `z` (e.g. `dog` → `dzg`).

## How to Contribute

Contributions are welcome. To suggest changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-chapter-05`)
3. Commit your changes
4. Open a pull request

Please keep the chapter-based layout and beginner-friendly comment style.

## License

This project is licensed under the [MIT License](LICENSE).

Copyright (c) 2026 [aashwinshukla](https://github.com/aashwinshukla)
