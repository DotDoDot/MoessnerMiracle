# Import argparse module
import argparse

# Import sys module
import sys

# Import array module
import array

# Declare function to define command-line arguments
def readOptions(args=sys.argv[1:]):
  parser = argparse.ArgumentParser(description="The parsing commands lists.")
  parser.add_argument("-n", "--number_count", help="Number of natural numbers to go through.")
  parser.add_argument("-s", "--sequence_dimension", help="Dimension number to highlight.")
  opts = parser.parse_args(args)
  return opts

# Call the function to read the argument values
options = readOptions(sys.argv[1:])
#print(options.number_count)
#print(options.sequence_dimension)
dimension = int(options.sequence_dimension)
numberCount = int(options.number_count)
MMarray = [0] * dimension
for x in range(dimension) :
    size = numberCount - x
    if(size == numberCount): #initialize the first row will natural numbers 1..number_count
        MMarray[x] = []
        for y in range(size):
            MMarray[x].append(y + 1)
    else:
        sum = 0
        MMarray[x] = []
        size = len(MMarray[x - 1])
        dimensionDiv = (dimension - (x - 1))
        for y in range(size):
            if((y + 1) %  dimensionDiv != 0):
                yindex = int(y / (dimensionDiv - 1))
                sum = MMarray[x - 1][y] + sum
                MMarray[x].append(sum)
print(MMarray)

# def prettyPrintMoessnerMiracle(MMarray):
#     numStrLen = largestNumberStrSize(MMarray)
#     row = 1
#     for x in MMarray:
#         index = 0
#         rowstr = ''
#         spaces = (dimension + (row - dimension))
#         row += 1
#         for y in x:
#             rowstr += str(y).ljust(numStrLen + 1, " ")
#             if (index) % spaces == 0:
#                 rowstr = rowstr.ljust(numStrLen * spaces, " ")
#             else:
#                 rowstr += ' ' * (numStrLen * spaces)
#             index += 1
#         print(rowstr)

# def largestNumberStrSize(MMarray):
#     maxLen = 0
#     for x in MMarray:
#         for y in x:
#             numStr = str(y)
#             if(len(numStr) > maxLen):
#                 maxLen = len(numStr)
#     return maxLen
# prettyPrintMoessnerMiracle(MMarray)