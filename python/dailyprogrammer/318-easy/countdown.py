import operator as op
import itertools as it

OPS = [op.add, op.sub, op.mul, op.div]
OPSTRING = ['+', '-', '*', '/']

def countdown(input, firstresult=True):
    ''' 
    Brute force through all permutations to find possible solutions
        input ->        Input string as space seperated ints.
        firstresult ->  Boolean value to return either first result, or all
                        correct solutions.
    '''
    inputs = input.split(" ")[:-1]
    goal = input.split(" ")[-1]
    inputperms = it.permutations(inputs)
    while True:
        # First loop iterates through operator permutations
        ops = it.product('0123',repeat=(len(inputs)-1))
        try:
            b = map(int,list(inputperms.next()))
            try:
                while True:
                    # Second loop iterates through input permutations
                    c = map(int,list(ops.next()))
                    if checkSolution(b,c,goal):
                        print pprint(b, c, goal)
                        if firstresult:
                            return
            except StopIteration:
                pass
        except StopIteration:
            return

def checkSolution(inputs, ops, goal):
    ''' Check solution for given inputs, ops, goal '''
    ret = 0
    for x in range(len(inputs)):
        if x == 0:
            ret = inputs[x]
            continue
        ret = OPS[ops[x-1]](ret, inputs[x])
    return int(ret) == int(goal)

def pprint(inputs, ops, goal):
    ''' Return result in proper format '''
    ret = str(inputs[0])
    for x in range(len(inputs)-1):
        ret += " %s %d" % (OPSTRING[ops[x]], inputs[x+1])
    ret += ' = %d' % int(goal)
    return ret
        
countdown("1 3 7 6 8 3 250", True)
countdown("25 100 9 7 3 7 881", True)
countdown("6 75 3 25 50 100 952", True)
