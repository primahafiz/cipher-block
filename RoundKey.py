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
        if(n % 2 == 1):
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
    
    # Arithmetic right shit (x >> k)
    def arithmeticRightShift(self, x : int, k : int):
        mask = (1 << 64)
        for i in range(k):
            if(x & 1 != 0):
                x >>= 1
                x |= mask
            else:
                x >>= 1
        
        return x
    
    def bitCount(self, x: int):
        res = 0
        while(x != 0):
            if(x % 2 == 1):
                res += 1
            x >>= 1
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

            # Xor l and r (l^r)
            xor = l ^ r

            # Power matrix by xor (mat**xor)
            newMat = self.matPow(self.matrixRoundKey,xor)

            # Multply matrix and l r split per 8 bit -> result list length 16 [[e1,e2,...,]]
            listKey = self.mul(newMat,[self.splitTo8Bit(l,r)])

            # Convert listKey to integer
            keyL = 0
            for i in range(8):
                keyL += listKey[0][i]
                keyL <<= 8

            keyR = 0
            for i in range(8):
                keyR += listKey[0][i + 8]
                keyR <<= 8
            
            keyL = self.arithmeticRightShift(keyL,self.bitCount(keyL))
            keyR = self.arithmeticRightShift(keyR,self.bitCount(keyR))

            key = keyL ^ keyR

            res.append(key)

            # Swap key l = last 64 bit, r = first 64 bit
            l = keyR
            r = keyL

        # Copy to listRoundKey
        for i in range(16):
            self.listRoundKey.append(res[i])
        
        return res


if __name__ == "__main__":
    x = RoundKey(146160920599406919205645990694686082803)
    print(x.getListRoundKey())

