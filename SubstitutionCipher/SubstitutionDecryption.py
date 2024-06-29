def decryption(Encrypted_message):
    # with open("VignereCipher\Decrypted.txt",'r') as file:
    #     Encrypted_message = file.read()
        
        

    AsciiValueOfEncrypted = []
    for i in range(len(Encrypted_message)):
        AsciiValueOfEncrypted.append(ord(Encrypted_message[i]))   

    # print(AsciiValueOfEncrypted)  


    list_2 =[]
    with open('Keys/SubstitutionCipherList2.bin','rb') as file:
        for line in file:  
            list_2.append(int(line))
    # print(list_2)   

    list_1 =[]
    with open('Keys/SubstitutionCipherList1.bin','rb') as file:
        for line in file:  
            list_1.append(int(line))
    # print(list_1)     


    IndexofThisAscii = []
    for i in range(len(AsciiValueOfEncrypted)):
        IndexofThisAscii.append(list_2.index(AsciiValueOfEncrypted[i])) 

    # print(IndexofThisAscii) 



    #Ab is index pe list 1 ki value check karo
    ValueAtThisIndexInList1 =[]
    for i in range(len(IndexofThisAscii)):
        ValueAtThisIndexInList1.append(list_1[IndexofThisAscii[i]])     


    #ab use decrypt karo

    decrypted = []
    for i in range(len(ValueAtThisIndexInList1)):
        decrypted.append(chr(ValueAtThisIndexInList1[i]))      

    string ="" 
    for d in decrypted:
        string = string +(d)         
    return string     