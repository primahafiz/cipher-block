from RoundKey import RoundKey
from RoundFunction import round_function
import utils

N_ROUND = 16
BLOCK_SIZE = 16

def feistel(a,b,c,d,key, round):
    resF1 = round_function(a,key, round)
    resF2 = round_function(c,key, round)
    resXor1 = b ^ resF1
    resXor2 = d ^ resF2
    return resXor1, c, resXor2, a

def dlr_cipher(plain_text:str = '',external_key:str='', encrypt: bool = True):
    
    # Bisa diganti utils.str_to_int
    key_int =  utils.str_to_int(external_key)

    # Bisa diganti utils.str_to_int
    pt_int = utils.str_to_int(plain_text)

    pt_left = pt_int >> 64
    pt_right = pt_int % (1 << 64)

    pt_first = pt_left >> 32
    pt_second = pt_left % (1 << 32)
    pt_third = pt_right >> 32
    pt_fourth = pt_right % (1 << 32)

    rk = RoundKey(key_int)
    round_keys : list[int] = rk.getListRoundKey()
    a,b,c,d = pt_first,pt_second,pt_third,pt_fourth

    if encrypt:
        for i in range(N_ROUND):
            key = round_keys[i]
            a,b,c,d = feistel(a,b,c,d,key,i+1)
        a,b,c,d = d,a,b,c
    else:
        for i in range(N_ROUND):
            key = round_keys[N_ROUND-1-i]
            a,b,c,d = feistel(a,b,c,d,key,N_ROUND-i)
        a,b,c,d = b,c,d,a

    res = utils.bitfield(a) + utils.bitfield(b) + utils.bitfield(c) + utils.bitfield(d)
    return utils.frombits(res)


def interactive():
    print("Selamat datang di program cipher blok DLR")
    print("Silakan pilih angka mode yang tersedia:")
    print("  1. Enkripsi")
    print("  2. Dekripsi")
    print("  0. Keluar")

    print(">> ",end="")
    mode = int(input())

    while(mode != 1 and mode != 2 and mode != 0):
        print("Input tidak valid. Masukkan ulang!")
        print(">> ",end="")
        mode = int(input())

    match mode:
        case 0:
            exit()
        case 1:
            print("Masukkan plain text")
        case 2:
            print("Masukkan cipher text")
    
    print(">> ",end="")
    text = input()
    print("Masukkan key")
    print(">> ",end="")
    external_key = input()

    # text = 'nama saya dimas='
    # external_key = 'sdsdrvdgenboris?'

    if(len(text) % BLOCK_SIZE != 0):
        sisa = BLOCK_SIZE - (len(text) % BLOCK_SIZE)
        text += '~' * sisa


    result_text = ""
    match mode:
        case 1:
            for i in range(0,len(text),BLOCK_SIZE):
                res = dlr_cipher(text[i:i+BLOCK_SIZE],external_key)
                result_text += res
        case 2:
            for i in range(0,len(text),BLOCK_SIZE):
                res = dlr_cipher(text[i:i+BLOCK_SIZE],external_key,False)
                result_text += res
    
    print(result_text)

def another_main():
    text = 'nama saya dimas='
    external_key = 'sdsdrvdgenboris?'

    if(len(text) % BLOCK_SIZE != 0):
        sisa = BLOCK_SIZE - (len(text) % BLOCK_SIZE)
        text += '~' * sisa


    cipher_text = ""
    for i in range(0,len(text),BLOCK_SIZE):
        res = dlr_cipher(text[i:i+BLOCK_SIZE],external_key)
        cipher_text += res

    print(cipher_text)
    plain_text = ""
    for i in range(0,len(cipher_text),BLOCK_SIZE):
        res = dlr_cipher(cipher_text[i:i+BLOCK_SIZE],external_key,False)
        plain_text += res
    
    print(plain_text)


if __name__ == "__main__":
    # interactive()
    another_main()