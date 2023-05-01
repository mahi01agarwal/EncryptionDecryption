def decryption(Encrypted_message):
    # with open('SubstitutionCipher/DecryptedText.txt','r') as file:
    #     Encrypted_message = file.read()
    with open('Keys/ShiftCipherKeysUsed.bin','rb') as file:
        KeyUsed = file.read()

        
    Key = int(KeyUsed)   


    problist= []
    with open('Keys/ShiftCipherProbKeys.bin','rb') as file:
        for line in file:
            curr_place = line[:-1]
            problist.append(int(curr_place))
            
    value_y = []        
    with open('Keys/ShiftCipherValue_y.bin','rb') as file:
        for line in file:
            curr_place = line[:-1]
            value_y.append(int(curr_place))       
            
    # print(problist)
    # print(Key)
    # print(value_y)

    DecryptedText=[]
    for i in range(len(Encrypted_message)):
        if i in problist:
            value_j = value_y[i] - 33
            x = (value_j - Key)%127
            DecryptedText.append(chr(x))
        else:
            x = (value_y[i] - Key)%127 
            DecryptedText.append(chr(x))


    string = ""
    for d in DecryptedText:
        string = string +(d)         
    return string    