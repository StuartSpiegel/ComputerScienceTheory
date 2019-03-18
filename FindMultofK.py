import thread
import time

#Find Multiple of K, non decision problem of has multiple of K
#stuart spiegel, 3.2.2019

def hasMultipleOfK(numK, divide):
    if ((numK % divide == 0)):
        return true
    else:
        return false

def findMultipleOfK(numThreads, numK, div1, div2):
    for k in range (0 to numThreads):
        try:
            thread1 = newThread(k, "thread1")
            thread1.start_new_thread(hasMultipleOfK, args[k, div1, div2])
            if(hasMultipleOfK(k, divide) == 'true'):
                return thread1.self
