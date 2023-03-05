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
