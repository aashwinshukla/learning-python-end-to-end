# Learning Python End to End

A chapter-by-chapter Python learning repository with hands-on scripts, inline comments, and small projects. Each folder covers one focused topic so you can learn concepts in order and run examples as you go. Two bonus folders cover variable scope and modules as supplementary material.

---

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Repository Structure](#repository-structure)
- [Chapter Breakdown](#chapter-breakdown)
  - [Chapter 01 — Introduction](#chapter-01--introduction)
  - [Chapter 02 — Strings](#chapter-02--strings)
  - [Chapter 03 — Input](#chapter-03--input)
  - [Chapter 04 — Building (Part 01)](#chapter-04--building-part-01)
  - [Chapter 05 — Lists](#chapter-05--lists)
  - [Chapter 06 — Functions](#chapter-06--functions)
  - [Chapter 07 — Statements](#chapter-07--statements)
  - [Chapter 08 — Building (Part 02)](#chapter-08--building-part-02)
  - [Chapter 09 — Dictionary](#chapter-09--dictionary)
  - [Chapter 10 — Loops](#chapter-10--loops)
  - [Chapter 11 — Building (Part 03)](#chapter-11--building-part-03)
  - [Chapter 12 — 2D Lists & Nested Loops](#chapter-12--2d-lists--nested-loops)
  - [Chapter 13 — Try and Except](#chapter-13--try-and-except)
  - [Chapter 14 — Object-Oriented Programming](#chapter-14--object-oriented-programming)
  - [Bonus — Variable Scope (LEGB)](#bonus--variable-scope-legb)
  - [Bonus — Modules](#bonus--modules)
- [Suggested Learning Path](#suggested-learning-path)
- [How to Contribute](#how-to-contribute)
- [License](#license)

---

## Prerequisites

- [Python 3](https://www.python.org/downloads/) (3.10 or newer recommended — required for `match/case`)
- A terminal or code editor (e.g. [VS Code](https://code.visualstudio.com/))

---

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

   On some systems use `python3` instead of `python`.

---

## Repository Structure

```
learning-python-end-to-end/
├── Chapter-01-Introduction/
│   ├── hello.py
│   ├── variable-and-data-type.py
│   ├── shape.py
│   └── converting.py
├── Chapter-02-Strings/
│   ├── working_with_string.py
│   └── working_with_number.py
├── Chapter-03-Input/
│   ├── getting-input.py
│   └── formate-specifier.py
├── Chapter-04-Building/
│   ├── basic-calculator.py
│   └── mad-libs.py
├── Chapter-05-Lists/
│   ├── list.py
│   ├── list-functions.py
│   ├── tuples.py
│   ├── set.py
│   └── imp.py
├── Chapter-06-Functions/
│   ├── functions.py
│   └── exponent.py
├── Chapter-07-Statements/
│   ├── if.py
│   ├── if-comparision.py
│   ├── conditional.py
│   ├── match-case.py
│   └── return.py
├── Chapter-08-Building-part-02/
│   └── better-calculator.py
├── Chapter-09-Dictionary/
│   └── dictionary.py
├── Chapter-10-Loop/
│   ├── for.py
│   ├── while.py
│   └── list-comprehension.py
├── Chapter-11-Building_Part_03/
│   ├── guess.py
│   ├── translator.py
│   ├── bank.py
│   └── encryption-program.py
├── Chapter-12-2DLists-NestedLoops/
│   ├── 2dlist.py
│   └── nestedloop.py
├── Chapter-13-Try-And-Except/
│   └── tryExcept.py
├── Chapter-14-OOP/
│   ├── object-and-class.py
│   ├── carClass.py
│   ├── class-variable.py
│   ├── class-method.py
│   ├── inheritance.py
│   ├── multilevel-multiple.py
│   ├── super.py
│   ├── polimorphism.py
│   ├── property.py
│   └── static.py
├── 00-Variable-Scope/
│   └── legb.py
└── 00-Module/
    └── module.py
```

---

## Chapter Breakdown

### Chapter 01 — Introduction

**Folder:** `Chapter-01-Introduction/`

The starting point. Covers the very basics of Python before any logic is introduced.

| File | What it covers |
|------|----------------|
| `hello.py` | First `print()` statement — "Hello World" |
| `variable-and-data-type.py` | Declaring variables, the three core data types (string, number, bool), variable reassignment, and f-strings |
| `shape.py` | Using multiple `print()` calls to draw an ASCII triangle |
| `converting.py` | Type casting with `str()`, `int()`, `float()`, `bool()`, and checking types with `type()` |

**Key concepts:** `print()`, variables, strings, integers, floats, booleans, f-strings, type casting.

```python
# f-string example from variable-and-data-type.py
name = "Mike"
print(f"hello {name}!")

# type casting from converting.py
gpa = 3.2
gpa = int(gpa)   # becomes 3
```

---

### Chapter 02 — Strings

**Folder:** `Chapter-02-Strings/`

Deep dive into Python's string and number capabilities.

| File | What it covers |
|------|----------------|
| `working_with_string.py` | Escape characters, string methods (`.lower()`, `.upper()`, `.isupper()`, `.index()`, `.replace()`, `.capitalize()`, `.isdigit()`, `.isalpha()`, `.count()`), string length with `len()`, and character indexing |
| `working_with_number.py` | Arithmetic operators, `abs()`, `pow()`, `max()`, `min()`, `round()`, the `math` module (`floor`, `ceil`, `sqrt`, `pi`, `e`), and a mini circumference calculator |

**Key concepts:** String methods, escape characters `\"`, string indexing `[0]`, arithmetic operators, `math` module, `from math import *`.

```python
# from working_with_string.py
phrase = "Hello World"
print(phrase.replace("World", "India"))  # Hello India
print(phrase.index("W"))                 # 6

# from working_with_number.py
from math import *
print(floor(3.7))   # 3
print(ceil(3.1))    # 4
print(sqrt(36))     # 6.0
```

---

### Chapter 03 — Input

**Folder:** `Chapter-03-Input/`

How to accept and format user input.

| File | What it covers |
|------|----------------|
| `getting-input.py` | Using `input()` to capture user data and printing it back with concatenation |
| `formate-specifier.py` | f-string format specifiers: `:.2f` (decimal precision), `:10` (width), `:010` (zero-padding), `:<`, `:>`, `:^` (alignment), `:+` (sign), `:,` (thousands separator) |

**Key concepts:** `input()`, f-string format specifiers, string alignment and padding.

```python
# from formate-specifier.py
price = 3.14243
print(f"price is {price:.2f}")    # 3.14
print(f"price is {price:,}")      # 3,14243 (thousands comma)
print(f"price is {price:^10}")    # centered in 10-char field
```

---

### Chapter 04 — Building (Part 01)

**Folder:** `Chapter-04-Building/`

First mini-projects combining what was learned in chapters 01–03.

| File | What it covers |
|------|----------------|
| `basic-calculator.py` | Takes two user inputs, converts them to `float`, and prints their sum. Demonstrates why type conversion matters with `input()` |
| `mad-libs.py` | Collects a colour, plural noun, and celebrity name via `input()`, then prints a short story using string concatenation |

```bash
python Chapter-04-Building/mad-libs.py
# Enter a colour: red
# Enter a Plural noun: cats
# Enter a name of a Celebrity: Elon Musk
# Roses are red
# cats are Blue
# I love Elon Musk
```

---

### Chapter 05 — Lists

**Folder:** `Chapter-05-Lists/`

Python's core sequential data structures.

| File | What it covers |
|------|----------------|
| `list.py` | Creating lists, index access, negative indexing, slicing `[1:]`, `[1:3]`, and modifying elements |
| `list-functions.py` | `.extend()`, `.append()`, `.insert()`, `.remove()`, `.clear()`, `.pop()`, `.index()`, `.count()`, `.sort()`, `.reverse()`, `.copy()` |
| `tuples.py` | Tuples with `()` — ordered, unchangeable, faster than lists; list of tuples |
| `set.py` | Sets with `{}` — unordered, no duplicates; `.add()`, `.remove()`, `.pop()`, `.clear()` |
| `imp.py` | Built-in helper functions `dir()`, `help()`, `len()` applicable to any collection |

**Key concepts:** List mutability, tuple immutability, set uniqueness, slicing, collection methods.

```python
friends = ["Kevin", "Karen", "Jim"]
friends.insert(1, "Kelly")   # ["Kevin", "Kelly", "Karen", "Jim"]
friends.sort()               # alphabetical order
print(friends[1:3])          # ['Karen', 'Kelly']

# tuple — cannot be changed after creation
coordinates = (4, 5)

# set — no duplicates
fruits = {"apple", "orange", "banana", "apple"}  # stores only 3 items
```

---

### Chapter 06 — Functions

**Folder:** `Chapter-06-Functions/`

Defining and calling reusable blocks of code.

| File | What it covers |
|------|----------------|
| `functions.py` | `def` keyword, calling functions, passing parameters, multiple calls with different arguments |
| `exponent.py` | Building a custom exponent function using a `for` loop, `return` statement, and the `**` operator shorthand |

**Key concepts:** `def`, parameters, function calls, `return`, `**` exponentiation operator.

```python
# from functions.py
def user(name):
    print("hello " + name)

user("Mike")   # hello Mike
user("Steve")  # hello Steve

# from exponent.py
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result *= base_num
    return result

print(raise_to_power(2, 3))  # 8
```

---

### Chapter 07 — Statements

**Folder:** `Chapter-07-Statements/`

Decision making and control flow.

| File | What it covers |
|------|----------------|
| `if.py` | Basic `if/else`, `or`, `and`, `not()`, `elif` chains with bool variables |
| `if-comparision.py` | Using `if/elif/else` with numeric comparisons to find the maximum of three numbers |
| `conditional.py` | One-line ternary / inline conditional expression |
| `match-case.py` | Python 3.10+ `match/case` statement (similar to switch/case in C) with a day-of-week function and a wildcard `case _` default |
| `return.py` | `return` statement in functions — returning a computed value (`cube`) for use outside the function |

**Key concepts:** `if`, `elif`, `else`, comparison operators, `and`/`or`/`not`, ternary expressions, `match/case`, `return`.

```python
# one-liner conditional from conditional.py
num = int(input("Enter a number"))
print("positive" if num >= 0 else "negative")

# match/case from match-case.py
def day_of_week(day):
    match day:
        case 1: return "it is monday"
        case 2: return "it is tuesday"
        case _: return "not valid input"
```

---

### Chapter 08 — Building (Part 02)

**Folder:** `Chapter-08-Building-part-02/`

Upgraded calculator using functions and conditionals together.

| File | What it covers |
|------|----------------|
| `better-calculator.py` | A `calculator(num1, op, num2)` function that handles `+`, `-`, `*`, `/` operators using `if/elif/else`, takes float inputs, and gracefully handles invalid operators |

```bash
python Chapter-08-Building-part-02/better-calculator.py
# enter first number: 10
# enter an operator: *
# enter second number: 5
# 50.0
```

---

### Chapter 09 — Dictionary

**Folder:** `Chapter-09-Dictionary/`

Key-value pair data structures.

| File | What it covers |
|------|----------------|
| `dictionary.py` | Creating a dictionary, accessing values by key with `[]`, using `.get()` with a default fallback, iterating keys with `.keys()`, iterating values with `.values()` |

**Key concepts:** Dictionary literals `{}`, key access, `.get()`, `.keys()`, `.values()`, default values.

```python
monthConversion = {"Jan": "January", "Feb": "February", ...}

print(monthConversion["Nov"])                          # November
print(monthConversion.get("XYZ", "not a valid key"))   # not a valid key

for value in monthConversion.values():
    print(value)   # prints all full month names
```

---

### Chapter 10 — Loops

**Folder:** `Chapter-10-Loop/`

Repeating code with `for` and `while`.

| File | What it covers |
|------|----------------|
| `for.py` | Iterating over strings, lists, `range()`, `range(start, stop, step)`, `len()` with index-based access, `continue`/`break`, `time.sleep()`, and building a countdown timer in `HH:MM:SS` format |
| `while.py` | Basic `while` loop counting 1–10, using a `while` loop to force valid user input |
| `list-comprehension.py` | List comprehension syntax `[expression for value in iterable if condition]` vs traditional `for` loop; applying methods to each element; filtering positive and negative numbers |

**Key concepts:** `for`, `while`, `range()`, `break`, `continue`, list comprehension, `time.sleep()`.

```python
# for loop with range and step
for index in range(1, 11, 2):
    print(index)   # 1, 3, 5, 7, 9

# list comprehension with condition
numbers = [1, -2, 3, -4, 5, -6]
positive = [n for n in numbers if n >= 0]   # [1, 3, 5]

# while loop forcing input
name = input("Enter your name")
while name == "":
    print("You did not enter your name")
    name = input("Enter your name")
```

---

### Chapter 11 — Building (Part 03)

**Folder:** `Chapter-11-Building_Part_03/`

Four complete mini-projects combining everything learned so far.

| File | What it covers |
|------|----------------|
| `guess.py` | Word guessing game with a move limit — demonstrates `while` loops, boolean flags, and conditionals |
| `translator.py` | Custom vowel-to-`z` translator using string iteration and `if` conditions inside a function |
| `bank.py` | CLI banking app with balance tracking, deposit/withdraw validation, and a main loop — uses functions, `while`, `if/elif`, and the `__name__ == '__main__'` guard |
| `encryption-program.py` | Caesar-cipher-style encryption and decryption using `random.shuffle()`, `string` module constants, and character index mapping |

```bash
# translator
python Chapter-11-Building_Part_03/translator.py
# Enter a phrase: hello world
# hzllz wzrld

# bank app
python Chapter-11-Building_Part_03/bank.py
# Welcome to Our bank
# 1. Check balance  2. deposit  3. Withdraw  4. Exit
```

---

### Chapter 12 — 2D Lists & Nested Loops

**Folder:** `Chapter-12-2DLists-NestedLoops/`

Working with multi-dimensional data.

| File | What it covers |
|------|----------------|
| `2dlist.py` | Declaring a list of lists (2D grid), accessing elements with double indexing `[row][col]` |
| `nestedloop.py` | Using a `for` loop inside another `for` loop to traverse every element in a 2D list |

**Key concepts:** List of lists, double indexing `[0][0]`, nested `for` loops.

```python
number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

print(number_grid[0][0])   # 1 — row 0, column 0
print(number_grid[1][2])   # 6 — row 1, column 2
```

---

### Chapter 13 — Try and Except

**Folder:** `Chapter-13-Try-And-Except/`

Handling runtime errors gracefully.

| File | What it covers |
|------|----------------|
| `tryExcept.py` | Bare `try/except`, catching specific exceptions (`ZeroDivisionError`, `ValueError`), and why broad exception handling should be avoided |

**Key concepts:** `try`, `except`, specific exception types, defensive input handling.

```python
try:
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError:
    print("Divided by zero")
except ValueError:
    print("invalid input")
```

---

### Chapter 14 — Object-Oriented Programming

**Folder:** `Chapter-14-OOP/`

The largest chapter — full coverage of OOP in Python across 10 files.

| File | What it covers |
|------|----------------|
| `carClass.py` | Defining a `Car` class with `__init__`, instance attributes, and methods (`drive`, `stop`, `describe`) |
| `object-and-class.py` | Creating objects from a class, attribute access with `.`, calling methods, importing a class from another file |
| `class-variable.py` | Class variables shared across all instances (`class_year`, `num_student`) vs instance variables; best practice for accessing class variables via the class name |
| `class-method.py` | `@classmethod` decorator with `cls` parameter; computing class-level statistics (student count, average GPA) |
| `inheritance.py` | Single inheritance — `Dog`, `Cat`, `Mouse` all inheriting from `Animal`; reusing `eat()` and `sleep()` without rewriting them |
| `multilevel-multiple.py` | Multilevel inheritance (`Rabbit → Prey → Animal`) and multiple inheritance (`Fish(Prey, Predator)`) |
| `super.py` | `super().__init__()` to call a parent class constructor and extend it with child-specific attributes |
| `polimorphism.py` | Polymorphism via inheritance with abstract base classes (`@abstractmethod`), and duck typing with unrelated classes sharing the same method name |
| `property.py` | `@property` decorator for getters, and `@<name>.setter` for setters with validation logic — controlled attribute access |
| `static.py` | `@staticmethod` for utility methods that belong to the class but don't need access to instance or class data |

**Key concepts:** `class`, `__init__`, `self`, `cls`, instance methods, class methods, static methods, inheritance, `super()`, polymorphism, abstract methods, `@property`, getters/setters.

```python
# inheritance — from inheritance.py
class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    pass   # inherits everything from Animal

dog = Dog("Scooby")
dog.eat()   # Scooby is eating

# property with validation — from property.py
class Rectangle:
    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("width must be greater than zero")

# polymorphism — from polimorphism.py
shapes = [Circle(4), Square(5), Pizza("pepperoni", 15)]
for shape in shapes:
    print(shape.area())   # each class has its own area() implementation
```

---

### Bonus — Variable Scope (LEGB)

**Folder:** `00-Variable-Scope/`

| File | What it covers |
|------|----------------|
| `legb.py` | The four scope levels in Python — **L**ocal, **E**nclosed, **G**lobal, **B**uilt-in — with a code example for each, and how Python resolves variable names by walking up the LEGB chain |

```python
# LEGB resolution order: Local → Enclosed → Global → Built-in
x = 3   # global

def func1():
    print(x)   # uses global x since no local x exists

func1()   # prints 3
```

---

### Bonus — Modules

**Folder:** `00-Module/`

| File | What it covers |
|------|----------------|
| `module.py` | Using `help("modules")` to list all available Python modules and `help("math")` to inspect what a specific module provides |

---

## Suggested Learning Path

Work through chapters **01 → 14** in order. Each script is self-contained and includes comments explaining every concept.

```
Chapter 01  →  Variables & data types
Chapter 02  →  Strings & numbers
Chapter 03  →  User input & formatting
Chapter 04  →  Mini projects (calculator, mad libs)
Chapter 05  →  Lists, tuples, sets
Chapter 06  →  Functions
Chapter 07  →  Conditionals & match/case
Chapter 08  →  Improved calculator project
Chapter 09  →  Dictionaries
Chapter 10  →  Loops & list comprehension
Chapter 11  →  Four complete projects
Chapter 12  →  2D data structures
Chapter 13  →  Error handling
Chapter 14  →  Full OOP deep dive
  ↓
Bonus: Variable Scope (LEGB)
Bonus: Modules
```

**Highlights along the way:**

- **Mad Libs** (`Chapter-04-Building/mad-libs.py`) — `input()` + string concatenation in practice
- **Better Calculator** (`Chapter-08-Building-part-02/better-calculator.py`) — functions + conditionals working together
- **Bank App** (`Chapter-11-Building_Part_03/bank.py`) — the most complete beginner project; combines functions, loops, input validation, and the `__main__` guard
- **Encryption Program** (`Chapter-11-Building_Part_03/encryption-program.py`) — real use of `random`, `string` module, and character mapping
- **OOP Chapter** (`Chapter-14-OOP/`) — ten files progressively building up to abstract classes, polymorphism, and properties

---

## How to Contribute

Contributions are welcome. To suggest changes:

1. Fork the repository
2. Create a feature branch (`git checkout -b improve-chapter-05`)
3. Commit your changes
4. Open a pull request

Please keep the chapter-based layout and beginner-friendly comment style.

---

## License

This project is licensed under the [MIT License](LICENSE).

Copyright (c) 2026 [aashwinshukla](https://github.com/aashwinshukla)
