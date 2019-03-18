#python program that counts the number of lines

toRead = input("File to read from: ")
num_Lines = 0;

def countLines(toRead):
    with open(toRead, 'r') as f
    for line in f:
        num_Lines+=1
print(num_Lines)

#def countLines(inputString):
# return str( len (inputString.split("\n")))
# lines = inputString.split('\n')
# count = len(lines)
# output = str(count)
# return output
