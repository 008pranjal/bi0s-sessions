def decrypt():
    a=input()
    
    
    
    for i in range(1,27):

        s=''
        for j in a:
        
             if  j.isupper():
                 s = s + chr((ord(j) - i - 65) % 26 + 65)
             else:
                 s = s + chr((ord(j) - i - 97) % 26 + 97)
        
           
        print(s)
             






if __name__=="__main__":
    decrypt()
