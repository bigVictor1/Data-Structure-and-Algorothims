Expression Evaluator
Overview
Python program to evaluate mathematical expressions from input.txt using stacks, outputting results to output.txt.
Requirements

Python 3.x

Files

expression_evaluator.py: Source code.
input.txt: Input file with expressions separated by -----.
output.txt: Generated output file.
README.md: This file.

Input Structure

Expressions on separate lines, e.g., 3 + 5 * 2.
Separators: lines with only -----.
Assumes: Positive integers, binary operators (+, -, *, /), parentheses, no spaces except around operators, no unary minus.

Output Structure

Results replace expressions, separators preserved.
Integers as int, floats as float.

How to Run

Ensure input.txt exists in the same directory.
Run: python expression_evaluator.py
View results in output.txt.

Limitations

No error handling for invalid expressions, mismatched parentheses, or division by zero.
Supports only basic arithmetic; no variables or functions.