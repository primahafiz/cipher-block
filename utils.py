def tobits(s):
    result = []
    for c in s:
        bits = bin(ord(c))[2:]
        bits = '00000000'[len(bits):] + bits
        result.extend([int(b) for b in bits])
    return result

def frombits(bits):
    chars = []
    for b in range(int(len(bits) / 8)):
        byte = bits[b*8:(b+1)*8]
        chars.append(chr(int(''.join([str(bit) for bit in byte]), 2)))
    return ''.join(chars)

def intcaststr(bitlist):
    return int("".join(str(i) for i in bitlist), 2)

def intcastlookup(bitlist):
    return int(''.join('01'[i] for i in bitlist), 2)

def shifting(bitlist):
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def str_to_int(str):
    key =  tobits(str)
    return intcaststr(key)

def bitfield(n):
    return [1 if digit=='1' else 0 for digit in bin(n)[2:]]