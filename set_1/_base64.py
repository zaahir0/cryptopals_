STRING = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
B64STRING = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex_to_bytes(text):
    return bytes.fromhex(text)

def bytes_to_sextet(byte_data):
    BASE64_DICT = {
        0: "A", 1: "B", 2: "C", 3: "D", 4: "E", 5: "F", 6: "G", 7: "H",
        8: "I", 9: "J", 10: "K", 11: "L", 12: "M", 13: "N", 14: "O", 15: "P",
        16: "Q", 17: "R", 18: "S", 19: "T", 20: "U", 21: "V", 22: "W", 23: "X",
        24: "Y", 25: "Z", 26: "a", 27: "b", 28: "c", 29: "d", 30: "e", 31: "f",
        32: "g", 33: "h", 34: "i", 35: "j", 36: "k", 37: "l", 38: "m", 39: "n",
        40: "o", 41: "p", 42: "q", 43: "r", 44: "s", 45: "t", 46: "u", 47: "v",
        48: "w", 49: "x", 50: "y", 51: "z", 52: "0", 53: "1", 54: "2", 55: "3",
        56: "4", 57: "5", 58: "6", 59: "7", 60: "8", 61: "9", 62: "+", 63: "/"
    }
    BYTES_GROUP = 3
    BASE64_GROUP = 4


    base64_chars = []
    masque = 0b111111
    byte_counter,merged_bytes = 0,0



    for i in range(len(byte_data)):
        merged_bytes = (merged_bytes << 8) | byte_data[i]
        byte_counter += 1

        if byte_counter == BYTES_GROUP:
            temp = []
            for j in range(BASE64_GROUP):
                temp.append(BASE64_DICT[merged_bytes & masque])
                merged_bytes >>= 6

            temp.reverse()
            base64_chars.extend(temp)

            byte_counter = 0
            merged_bytes = 0
    return base64_chars


def sextets_to_b64(sextet) :
    textB64= "".join(sextet)
    return textB64





