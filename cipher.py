from RoundFunction import round_function

def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])


def faestel(a,b,c,d,key):
    resF1 = round_function(a,key)
    resF2 = round_function(c,key)
    resXor1 = byte_xor(b,resF1)
    resXor2 = byte_xor(d,resF2)
    return resXor1, c, resXor2, a

def f_function(input,key):
    return byte_xor(input,key)



plain_text = b'nama saya dimas!'
key1 = b'opfjbcjf'
key2 = b'sfgvqerg'
key3 = b'jadjifbn'
key4 = b'ssadaswd'
key5 = b'fsfac3fd'
key6 = b'thgfh6ud'

L = plain_text[:8]
R = plain_text[8:]

a = L[:4]
b = L[4:]
c = R[:4]
d = R[4:]

a,b,c,d = faestel(a,b,c,d,key1)
a,b,c,d = faestel(a,b,c,d,key2)
a,b,c,d = faestel(a,b,c,d,key3)
a,b,c,d = faestel(a,b,c,d,key4)
a,b,c,d = faestel(a,b,c,d,key5)
a,b,c,d = faestel(a,b,c,d,key6)

# arr = [a,b,c,d]
# a,b,c,d = faestel(a,b,c,d,key2)
print(a,b,c,d) 
a,b,c,d = faestel(d,a,b,c,key6)
a,b,c,d = faestel(c,d,a,b,key5)
a,b,c,d = faestel(c,d,a,b,key4)
a,b,c,d = faestel(c,d,a,b,key3)
a,b,c,d = faestel(c,d,a,b,key2)
a,b,c,d = faestel(c,d,a,b,key1)

print(d,a,b,c)

