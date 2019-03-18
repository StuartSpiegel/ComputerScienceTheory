import thread
import time

#Has multiple of K, takes a single ASCII String as input containing
#a positive integer k, followed by a semicolon, followed by a list
#of positive integers m1...mi. Each Mi and K is represented in decimal form
#solve the problem non-deterministically using a separate thread for each integer
#m in the input

def hasMultipleOfK(numK, divide):
    if ((numK % divide == 0)):
        return true
    else:
        return false

def main():

    for n in numK:
        try:
            thread.start_new_thread(hasMultipleOfK, args[n, divide])

        except:
            print("Error cant start thread")
