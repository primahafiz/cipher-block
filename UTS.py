from RoundKey import RoundKey
from RoundFunction import round_function
import utils

def faestel(a,b,c,d,key):
    resF1 = round_function(a,key, 1)
    resF2 = round_function(c,key, 1)
    resXor1 = b ^ resF1
    resXor2 = d ^ resF2
    return resXor1, c, resXor2, a

def encrypt(plain_text:str = '',external_key:str=''):
    
    # Bisa diganti utils.str_to_int
    key =  utils.tobits(external_key)
    key_int = utils.intcaststr(key)

    # Bisa diganti utils.str_to_int
    pt = utils.tobits(plain_text)
    # print(pt, len(pt))
    pt_int = utils.intcaststr(pt)

    pt_left = pt_int >> 64
    pt_right = pt_int % (1 << 64)

    pt_first = pt_left >> 32
    pt_second = pt_left % (1 << 32)
    pt_third = pt_right >> 32
    pt_fourth = pt_right % (1 << 32)

    rk = RoundKey(key_int)
    round_keys : list[int] = rk.getListRoundKey()

    key1 = round_keys[0]

    print(utils.frombits(utils.bitfield(pt_first)))
    print(utils.frombits(utils.bitfield(pt_second)))
    print(utils.frombits(utils.bitfield(pt_third)))
    print(utils.frombits(utils.bitfield(pt_fourth)))
    a,b,c,d = faestel(pt_first,pt_second,pt_third,pt_fourth,key1)
    # print(a, b, c, d)
    a,b,c,d = faestel(d,a,b,c,key1)
    # print(a, b, c, d)
    print(utils.frombits(utils.bitfield(a)))
    print(utils.frombits(utils.bitfield(b)))
    print(utils.frombits(utils.bitfield(c)))
    print(utils.frombits(utils.bitfield(d)))

    # print(pt_first.bit_length())
    # n = 1
    # for bit in utils.bitfield(pt_first):
    #     print(bit, end='')
    #     n += 1
    #     if n == 9:
    #         n = 1
    #         print()
    # print()
    # print(pt_second.bit_length())
    # print(pt_second)
    # n = 1
    # for bit in utils.bitfield(pt_second):
    #     print(bit, end='')
    #     n += 1
    #     if n == 9:
    #         n = 1
    #         print()
    # print()
    # print(pt_third.bit_length())
    # print(pt_fourth.bit_length())

    

    
    # for key in round_keys:
    #     bf = utils.bitfield(key)
    #     print(len(bf))
        
            




if __name__ == "__main__":
    encrypt(plain_text='nama saya dimas=',external_key='sdsdrvdgenboris?')