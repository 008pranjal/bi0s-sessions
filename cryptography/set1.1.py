def hextobase64():
    a='49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    b = a.decode("hex")
    print(b)
    c = b.encode("base64") 
    print(c)  
    
    
             

if __name__=="__main__":
    hextobase64()
