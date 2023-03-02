FILENAME = 'matrixRoundKey.txt'
N = 16
MOD = 251

# Call getListRoundKey function to get list of round key

class RoundKey:
    def __init__(self,externalKey : int):
        self.externalKey = externalKey
        self.matrixRoundKey = [[0 for i in range(N)] for j in range(N)]
        self.copyMatrix(self.readMatrixFile(FILENAME),self.matrixRoundKey)
        self.listRoundKey = []

    # Read random matrix file FILENAME
    def readMatrixFile(self,fileName : str):
        mat = [[0 for i in range(N)] for j in range(N)]
        with open(fileName,'r') as f:
            row = [[int(x) for x in line.split(' ')] for line in f]
            for i in range(N):
                for j in range(N):
                    mat[i][j] = row[i][j]
        return mat
    
    # Copy matrix src to dest
    def copyMatrix(self,src,dest):
        for i in range(N):
            for j in range(N):
                dest[i][j] = src[i][j]

    # Matrix multiplication (mat1 * mat2)
    def mul(self,mat1,mat2):
        row = len(mat1)
        col = len(mat2[0])
        res = [[0 for i in range(col)] for j in range(row)]
        for i in range(row):
            for j in range(col):
                for k in range(len(mat2)):
                    res[i][j] += mat1[i][k] * mat2[k][j]
                    res[i][j] %= MOD
        return res
    
    # Matrix power (mat**n)
    def matPow(self,mat,n : int):
        if(n == 0):
            res = [[0 for i in range(N)] for j in range(N)]
            self.copyMatrix(mat,res)
            return res
        
        new_mat = self.matPow(mat,n//2)
        if(n&1):
            return self.mul(mat,new_mat)
        else:
            return new_mat
        
    def splitTo8Bit(self,l : int, r : int):
        res = []
        for _ in range(8):
            x = r % (1 << 8)
            r >>= 8
            res.append(x)

        for _ in range(8):
            x = l % (1 << 8)
            l >>= 8
            res.append(x)
        
        res.reverse()
        return res

    # Get list of round key (length = 16, each key length is 128 bit)
    def getListRoundKey(self):
        if(len(self.listRoundKey) != 0):
            return self.listRoundKey

        res = []

        # l = first 64 bit, r = last 64 bit
        l = self.externalKey >> 64
        r = self.externalKey % (1 << 64)

        for i in range(N):

            # Left shift one bit for l and r
            l <<= 1
            r <<= 1

            # Xor l and r (l^r)
            xor = l ^ r

            # Power matrix by xor (mat**xor)
            newMat = self.matPow(self.matrixRoundKey,xor)

            # Multply matrix and l r split per 8 bit -> result list length 16 [[e1,e2,...,]]
            listKey = self.mul(newMat,[self.splitTo8Bit(l,r)])

            # Convert listKey to integer
            key = 0
            for i in range(16):
                key += listKey[0][i]
                key <<= 8
        
            res.append(key)

            # Swap key l = last 64 bit, r = first 64 bit
            l = key % (1 << 64)
            r = key >> 64

        # Copy to listRoundKey
        for i in range(16):
            self.listRoundKey.append(res[i])
        
        return res



# x = RoundKey(146160920599406919205645990694686082802)
# print(x.getListRoundKey())