class FormularError(Exception):
    pass


while True:
    inn = input('>>>')
    if inn == "quit":
        break

    x1 = inn.split(' ')
    try:
        x1[0] = float(x1[0])
        x1[2] = float(x1[2])
    except ValueError as e:
        raise FormularError('Unable to process input') from e
    if len(x1) != 3:
        raise FormularError('There should be 3 parts')

    if x1[1] == '+':
        result = x1[0] + x1[2]
    elif x1[1] == '-':
        result = x1[0] - x1[2]
    else:
        print('the funtion is not supported')
    print(result)
