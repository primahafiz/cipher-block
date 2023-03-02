import random

# Use prime number closest to 255 for modulo
MOD = 251

class MatrixRoundKey:
    def __init__(self):
        self.matrix = [[0 for i in range(16)] for j in range(16)]
        for i in range(16):
            for j in range(16):
                self.matrix[i][j] = random.randint(0,MOD-1)

    def writeMatrixToFile(self,fileName : str):
        with open(fileName,'w') as matrixFile:
            for row in self.matrix:
                matrixFile.write(' '.join([str(x) for x in row]) + '\n')
    

if __name__ == '__main__':
    matrixRoundKey = MatrixRoundKey()
    matrixRoundKey.writeMatrixToFile('matrixRoundKey.txt')