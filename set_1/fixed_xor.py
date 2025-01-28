BUFFER1 = "1c0111001f010100061a024b53535009181c"
BUFFER2 = "686974207468652062756c6c277320657965"
RESULT =  "746865206b696420646f6e277420706c6179"

def fixed_xor(hex_str1,hex_str2):
    bytes1 = bytes.fromhex(hex_str1)
    bytes2 = bytes.fromhex(hex_str2)

    print(bytes1,bytes2)
    if len(bytes1) != len(bytes2):
        raise ValueError("The buffers must be of equal size ! ")

    else:
        xored_str = []
        for i in range(len(bytes1)):
            xored_str.append(bytes1[i] ^ bytes2[i])


        return bytes(xored_str)


fixed_xor(BUFFER1,BUFFER2)