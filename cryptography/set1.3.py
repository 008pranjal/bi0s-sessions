def xor():
    a= bytearray.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

    c = bytearray(len(a))
    for j in range(0,256):
        for i in range(len(a)):
            c[i] = a[i] ^ j
        print("KEY:"+str(j)+":"+str(chr(j)))
        print(c)
             

if __name__=="__main__":
    xor()
