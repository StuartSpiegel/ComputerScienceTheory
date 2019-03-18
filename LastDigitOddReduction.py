#Program for the reduction from LastDigitIsEven to IsODD.

def P1(inString):
    n = int(inString)
    if n % 2==0: return 'yes'
    else: return 'no'

def P2(inString):
    if inString[-1] in '02468': return 'yes'
    else: return 'no'


def reduction(inString):
    output = P1(inString)
    return reduction(output)

def isODD(inString):
    if (reduction(inString) == 'yes'): return 'no'
    else: return 'yes'
