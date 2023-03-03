def byte_xor(ba1, ba2):
    return bytes([_a ^ _b for _a, _b in zip(ba1, ba2)])

def faestel(L,R, key):
    LL = L[:4]
    LR = L[4:]
    RL = R[:4]
    RR = R[4:]

    key1 = key[:4]
    key2 = key[4:12]
    key3 = key[12:]

    x1 = byte_xor(LL,key1)
    x3 = byte_xor(RR,key3)

    kiri = x1 + LR
    kanan = RL + x3

    x2 = byte_xor(kiri,key2)
    newL = byte_xor(x2,kanan)
    newR = kiri
    return newL, newR



plain_text = b'nama saya dimas!'
key1 = b'opfjbcjfrtsdfed?'
key2 = b'fehbfahdbshabcns'
key3 = b'fadksjbdawydbyas'
mid = len(plain_text)//2

L = plain_text[:mid]
R = plain_text[mid:]

L, R = faestel(L,R,key1)
L, R = faestel(L,R,key2)
L, R = faestel(L,R,key3)

print(L,R)
L, R = faestel(R,L,key3)
L, R = faestel(L,R,key2)
L, R = faestel(L,R,key1)

print(L,R)



# new_kiri = newR
# new_x1 = new_kiri[:4]

# new_x2 = byte_xor(new_kiri,key2)
# new_kanan = byte_xor(newL,new_x2)

# new_LL = byte_xor(new_x1, key1)

# new_x3 = new_kanan[4:]
# new_RR = byte_xor(new_x3,key3)
# new_RL = new_kanan[:4]
# new_LR = new_kiri[4:]
# print(new_LL,new_LR,new_RL,new_RR)


