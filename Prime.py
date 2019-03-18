# Stuart Spiegel
# Python program to check if number is prime.

#read in userInput
def main(inputString):
    num = int (inputString)
#num = some number

#all prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,"is a prime number")

#input is less than 1 and thus is not prime
else:
   print(num,"is not a prime number")
