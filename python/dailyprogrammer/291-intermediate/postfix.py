import operator
from math import factorial, pow

OPERATORS = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    'x' : operator.mul,
    '/' : operator.div,
    '//' : operator.floordiv,
    '%' : operator.mod,
    '^' : pow,
    '!' : factorial
}

def postfix(input):
    inputlist = input.split(' ')
    for value in inputlist:
        inputlist = inputlist[1:]
        try:
            inputlist += [float(value)]
        except ValueError:
            inputlist += [value]
    print '-> ', parselist(inputlist)[0]

def parselist(inputlist):
    """
    Find first operator in list. Recursively called by calc()
    until length of inputlist is 1
    """
    if len(inputlist) == 1:
        return inputlist[0]
    for index in range(len(inputlist)):
        if type(inputlist[index]) == str:
            calc(index, inputlist)
            break
    return inputlist

def calc_unary(func, index, inputlist):
    value = func(inputlist[index-1])
    del inputlist[index-1:index+1]
    inputlist.insert(index-1, value)
    return inputlist

def calc_binary(func, index, inputlist):
    value = func(inputlist[index-2], inputlist[index-1])
    del inputlist[index-2:index+1]
    inputlist.insert(index-2, value)
    return inputlist

def calc(index, inputlist):
    op = inputlist[index]
    if op == '!':
        calc_unary(OPERATORS.get(op), index, inputlist)
    else:
        calc_binary(OPERATORS.get(op), index, inputlist)
    parselist(inputlist)

# Tests

def test_all():
    test_examples()
    test_floordiv()
    test_modulus()
    test_xmul()

def test_examples():
    """ Examples from problem prompt. """
    ps = [
         '0.5 1 2 ! * 2 1 ^ + 10 + *',
         '1 2 3 4 ! + - / 100 *',
         '100 807 3 331 * + 2 2 1 + 2 + * 5 ^ * 23 10 558 * 10 * + + *'
    ]
    for p in ps:
        print p
        postfix(p)

# Tests for ops not covered in given examples

def test_floordiv():
    ps = [
        '8 2 // 2 //', # ((8 // 2) // 2) -> 2
        '8 3 // 2 //'  # ((8 // 3) // 2) -> 1
    ]
    for p in ps:
        print p
        postfix(p)

def test_modulus():
    p = '8 3 %'
    print p
    postfix(p)

def test_xmul():
    ps = [
         '0.5 1 2 ! x 2 1 ^ + 10 + x',
         '1 2 3 4 ! + - / 100 x',
         '100 807 3 331 x + 2 2 1 + 2 + x 5 ^ x 23 10 558 x 10 x + + x'
    ]
    for p in ps:
        print p
        postfix(p)

if __name__ == '__main__':
    test_all()
