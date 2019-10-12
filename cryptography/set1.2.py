import binascii

def xor():
    a= bytearray.fromhex("1c0111001f010100061a024b53535009181c")
    b= bytearray.fromhex("686974207468652062756c6c277320657965")

    c = bytearray(len(a))
    for i in range(len(a)):
        c[i] = a[i] ^ b[i]
    
    
    d=binascii.hexlify(c)
    print(d)
             

if __name__=="__main__":
    xor()
