import re

# (Element(s) in parenthesis) | (Single Element)              
PARSE_REGEX = '\(+[a-zA-Z0-9]*\)*[0-9]*|[A-Z][a-z]?[0-9]*'
CHARS = '[A-Z]+[a-z]*'
DIGITS = '[0-9]+'

def countElements(input):
    ret = {}
    parsedInput = re.findall(PARSE_REGEX, input)
    for x in parsedInput:
        if x[0] == '(':
            # Recursively go inside parenthesis, call returns innerret dictionary
            # Get value to multiply parenthesis elements by
            multval = re.findall('[0-9]+',x)[-1]
            # RE: Remove parenthesis, ending number
            substr = x.lstrip('(')
            innerret = countElements(re.sub('\)[0-9]*','',substr))
            # Multiply elements inside parenth by values.
            innerret = {q : int(w) * int(multval) for q,w in innerret.items()}
            # combine back into ret, dict.update replaces values so merge manually
            for (y,z) in innerret.items():
                try:
                    ret[y] += innerret[y]
                except KeyError:
                    ret[y] = innerret[y]
            continue
        try:
            # RE: Grab last digit found as # of element `element` to add
            num = re.findall(DIGITS, x)[0]
        except IndexError: # No trailing value
            num = 1
        # RE: Strip trailing number(s)
        element = re.findall(CHARS,x)[0]
        try:
            ret[element] += int(num)
        except KeyError: # First occurrence of element, add to dict
            ret[element] = int(num)
    return ret

# Sample and challenge inputs
print countElements('C6H12O6')
print countElements('CCl2F2')
print countElements('NaHCO3')
print countElements('C4H8(OH)2')
print countElements('PbCl(NH3)2(COOH)2')
