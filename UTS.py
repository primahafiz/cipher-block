from RoundKey import RoundKey
import RoundFunction
import utils

def encrypt(plain_text:str = '',external_key:str=''):
    
    # Bisa diganti utils.str_to_int
    key =  utils.tobits(external_key)
    key_int = utils.intcaststr(key)

    rk = RoundKey(key_int)
    round_keys : list[int] = rk.getListRoundKey()

    for key in round_keys:
        bf = utils.bitfield(key)
        print(len(bf))
        # n = 1
        # for bit in bf:
        #     print(bit, end='')
        #     n += 1
        #     if n == 9:
        #         n = 1
        #         print()
            




if __name__ == "__main__":
    encrypt(plain_text='nama saya dimas=',external_key='sdsdrvdgenboris?')