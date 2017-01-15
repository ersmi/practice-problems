import sys  #sys.argv

registers = {}
labels = {}
fd = open(sys.argv[1])

def main():
    """
    Recursively read file until EOF returns ''
    """
    input = fd.readline()
    if input == '':
        return
    input = input.lstrip().rstrip('\r\n')
    input = input.split(" ")
    if input[0] == '':
        main()
    elif len(input) > 1:
        instruction = input[0]
        args = input[1].split(',')
        execute(instruction, args)
    elif input[0][-1] == ':':
        labels.update([(input[0].rstrip(':'), fd.tell())])
    else:
        #TODO: Else assumes good input
        execute(input[0], None)
    main()

def execute(instruction, args):
    if instruction == 'ld':
        # TODO: Register a is stored as .* str, b int.
        #       Change for consistency.
        if args[0] == 'a':
            binstr = str(bin(int(args[1]))).lstrip('0b')
            paddedbinstr = ('0' * (8-len(binstr))) + binstr
            ret = paddedbinstr.replace('0','.').replace('1','*')
            registers.update([(args[0], ret)])
        else:
            registers.update([(args[0], int(args[1]))])
    if instruction == 'out':
        print registers.get(args[1], 'ERROR')
    if instruction == 'djnz':
        jumploc = labels.get(args[0], 'ERROR')
        jumpvalue = registers.get('b', 0)
        jumpvalue -= 1
        registers.update([('b', jumpvalue)])
        if jumpvalue != 0:
            fd.seek(jumploc)
    if instruction == 'rrca':
        ledvalue = registers.get('a', 'ERROR')
        ledvalue = ledvalue[-1] + ledvalue
        registers.update([('a', ledvalue[:-1])])
    if instruction == 'rlca':
        ledvalue = registers.get('a', 'ERROR')
        ledvalue = ledvalue + ledvalue[0]
        registers.update([('a', ledvalue[1:])])

main()
