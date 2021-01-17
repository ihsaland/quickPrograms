import numpy as np
from bigO import bigO
from bigO import algorithm

def pairsArr(s,n,matrix):
    stack = []

    for i in range(0,n):
        if i not in stack:
            stack.append(matrix[i]) #consider binary tree

            for j in range(i + 1,n):
                if matrix[i] + matrix[j] == s:
                    print(matrix[i], " + ", matrix[j], " = ", s)
                else:
                    pass
                    #print(matrix[i], " + ", matrix[j], " /= ", s)

def pairsDict(matrix):
    dct = {matrix[i]: matrix[i + 1] for i in range(0, len(matrix), 2)}
    print(dct)


if __name__ == '__main__':
    arr = np.array([[3,5],[-1,0],[9,3],[4,1]])
    flat_arr = arr.flatten()
    n = len(flat_arr)
    sum = 8

    #pairsArr(sum,n,flat_arr)

    lib = bigO()
    lib.test_all(pairsArr(sum,n,flat_arr))



