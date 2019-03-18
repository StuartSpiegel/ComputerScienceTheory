#yesOnStringApprox

def yesOnStringApprox(inputString):
    value = yesOnStringApprox(inputString)
    if (value == 'yes'):
        return 'yes'
    else:
        return 'no'

def modifiedYesOnStringApprox(inputString):
    value = crashOnSelf(inputString)
    if (val == 'yes'):
        return 'did not crash'
    else:
        #crash deliberately
        x = 1 / 0
