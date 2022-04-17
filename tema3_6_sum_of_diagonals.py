"""Given 2D array calculate the sum of diagonals elements."""

string = [[1,3,5],[1,4,6],[7,6,9]]
substring1 = string[0]
substring2 = string[1]
substring3 = string[2]
SUM_OF_DIAGONALS = substring1[0] + substring2[1] + substring3[-1] + \
                   substring1[-1] + substring2[1] + substring3[0]
print(SUM_OF_DIAGONALS)

#or
string = [[1,3,5],[1,4,6],[7,6,9]]
SUM_OF_DIAGONALS = string[0][0] + string[1][1] + string[-1][-1] + \
                   string[0][-1] + string[1][1] + string[2][0]
print(SUM_OF_DIAGONALS)
