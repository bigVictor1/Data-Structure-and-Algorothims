class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def is_empty(self):
        return len(self.items) == 0


def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0


def apply_operator(op, a, b):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b
    return 0


def evaluate_expression(expr):
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i].isdigit():
            num = 0
            while i < len(expr) and expr[i].isdigit():
                num = num * 10 + int(expr[i])
                i += 1
            tokens.append(num)
            continue
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
        i += 1

    values = Stack()
    operators = Stack()

    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, int):
            values.push(token)
        elif token == '(':
            operators.push(token)
        elif token == ')':
            while not operators.is_empty() and operators.peek() != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = operators.pop()
                values.push(apply_operator(op, val1, val2))
            if not operators.is_empty():
                operators.pop()
        else:
            while (not operators.is_empty() and operators.peek() != '(' and
                   precedence(operators.peek()) >= precedence(token)):
                val2 = values.pop()
                val1 = values.pop()
                op = operators.pop()
                values.push(apply_operator(op, val1, val2))
            operators.push(token)
        i += 1

    while not operators.is_empty():
        val2 = values.pop()
        val1 = values.pop()
        op = operators.pop()
        values.push(apply_operator(op, val1, val2))

    return values.pop()


with open('input.txt', 'r') as f:
    lines = f.readlines()

results = []
for line in lines:
    line = line.strip()
    if line == '-----':
        results.append('-----')
    elif line:
        result = evaluate_expression(line)
        res_str = str(int(result)) if isinstance(result, float) and result.is_integer() else str(result)
        results.append(res_str)

with open('output.txt', 'w') as f:
    f.write('\n'.join(results) + '\n')