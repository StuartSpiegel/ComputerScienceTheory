#Stuart Spiegel
#Program solves Pythagorean Triangles

import math
#solve for the hypotenuse given two legs
def solveHyp():
    firstLeg = int(input("What is the length of side a?: "))
    secondLeg = int(input("What is the lenth of side b?: "))
    side_c = sqrt(math.pow(firstLeg) + math.pow(secondLeg))
    return side_c

#Main function
def main():
    print(solveHyp())
