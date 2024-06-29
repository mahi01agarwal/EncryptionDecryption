def a_inverse(a):
    c=1
    if a==1:
        return 1
    else:
        for i in range(127*127*127):
            c=c+127
            f=c%a
            if f==0:
                ans=c/a
                ans=int(ans)
                break
    return ans

def decryption(Encrypted_message):
    
    #Reads the key1
    with open('Keys/AffineCipherkey1.bin','rb') as file:
        Key1Used = file.read()
    #Reads the key2    
    with open('Keys/AffineCipherkey2.bin','rb') as file:
        Key2Used = file.read()

    key1 = int(Key1Used)
    key2= int(Key2Used)    
        
    
    
    
    #Reads the prob Keys and stores them in problist
    problist= []
    with open('Keys/AffineCipherProbKeys.bin','rb') as file:
        for line in file:
            problist.append(int(line))
    
    
    #reads the ord value of encrypted character and stores it in value_y        
    value_y = []        
    with open('Keys/AffineCipherValue_y.bin','rb') as file:
        for line in file:
            value_y.append(int(line))       

    DecryptedText = []
    for i in range(len(Encrypted_message)):
        if i in problist:
            #subtract 33 from those values to which we added 33 while encrypting
            value_j=value_y[i]-33
            a_inv= a_inverse(key2)
            x= a_inv*(value_j-key1)%127
            DecryptedText.append(chr(x))
        else:
            a_inv= a_inverse(key2)
            x= a_inv*(value_y[i]-key1)%127
            DecryptedText.append(chr(x))
            
    
    
    #returns the final decrypted string        
    string ="" 
    for d in DecryptedText:
        string = string +(d)         
    return string         