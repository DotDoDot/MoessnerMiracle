# MoessnerMiracle
The challenge code suggested on [The Moessner Miracle. Why wasn't this discovered for over 2000 years?](https://www.youtube.com/watch?v=rGlpyFHfMgI )

"Challenge for the programmers among you: write a program that turns a sequence of highlighted integers into the corresponding Moessner sequence."

Usage example:

python MoessnerMiracle.py' '-n' '16' '-s' '3'

Output:

[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], [1, 3, 7, 12, 19, 27, 37, 48, 61, 75, 91], [1, 8, 27, 64, 125, 216]]

The output is an array of arrays containing each iteration of summing up the previous arrays non highlighted numbers. The last array in the array of arrays is the Moessner's Miracle sequence. In the above case the sequence is [1, 8, 27, 64, 125, 216] or [1^3, 2^3, 3^3, 4^3, 5^3, 6^3]
