class FormularError(Exception):
    pass


def repl():
    while True:
        try:
            user_input = input('>>>')
            if user_input == 'quit':
                print('bye')
                break
            else:
                print(evaluate_formula(user_input))
        except FormularError as e:
            print(f'Error: {e}')


def evaluate_formula(user_input):
    tokens = user_input.split(' ')
    if len(tokens) != 3:
        raise FormularError('Malformed formula')
    try:
        operand1 = float(tokens[0])
        operand2 = float(tokens[2])
    except ValueError as e:
        raise FormularError('Could not parse operands') from e

    operator = tokens[1]
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    else:
        raise FormularError('Unknown operator')


if __name__ == "__main__":
    repl()
