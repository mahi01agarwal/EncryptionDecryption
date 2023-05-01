def decryption(Encrypted_list):
    Encrypted_lisT =[]
    # with open('HillCipher\DecryptedText.txt','r') as file:
    #     Encrypted_list = file.read()
    for i in range(len(Encrypted_list)):    
        Encrypted_lisT.append(ord(Encrypted_list[i]))
    # print(Encrypted_list)    
    probList= []
    with open('Keys/VignereCipherProbKeys.bin','rb') as file:
        for line in file:
            probList.append(int(line))

    randomList = []        
    with open('Keys/VignereCipherRandomList.bin','rb') as file:
        for line in file:
            randomList.append(int(line))        

    # print(Encrypted_lisT)
    # print(randomList)

    DecryptedList=[]
    for i in range(len(Encrypted_list)):
        if i in probList:
            Encrypted_lisT[i]=Encrypted_lisT[i] -33
            x=( Encrypted_lisT[i]-randomList[i]) %127   
            DecryptedList.append(chr(x))
        else:
            x=( Encrypted_lisT[i]-randomList[i]) %127   
            DecryptedList.append(chr(x))  
    string =""
    for i in range(len(DecryptedList)):
        string = string +(DecryptedList[i])
    return string