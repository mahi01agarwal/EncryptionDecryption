
def encryption(message):    
    import random
    list_1 = list(range(32,127))
    list_2 = []

    for i in range(10000000000000000):
        r = random.randint(32,126)
        if r not in list_2:
            list_2.append(r)
            if len(list_1)==len(list_2):
                break

    file = open('Keys/SubstitutionCipherList1.bin' ,'wb')
    for i in range(len(list_1)):
        file.write(str.encode((f"{str(list_1[i])}\n")))  
    file.close()

    file = open('Keys/SubstitutionCipherList2.bin' ,'wb')
    for i in range(len(list_2)):
        file.write(str.encode((f"{str(list_2[i])}\n")))  
    file.close()
        
    # print(f"List 1: {list_1}\n")
    # print(f"list_2:{list_2}\n")

    AsciiValueOfMessage =[]
    for i in range(len(message)):
        AsciiValueOfMessage.append(ord(message[i]))
    # print(AsciiValueOfMessage)    

    FindeIndexOfAsciiVAlue =[]
    for i in range(len(AsciiValueOfMessage)):
        FindeIndexOfAsciiVAlue.append(list_1.index(AsciiValueOfMessage[i]))   

    # print(FindeIndexOfAsciiVAlue)    

    #us index pe list 2 ki value ckeck karo

    list_2Value =[]
    for i in range(len(FindeIndexOfAsciiVAlue)):
        list_2Value.append(list_2[FindeIndexOfAsciiVAlue[i]])   
        
    # print(list_2Value)    

    # list 2 ki in values se charcater banao
    EncryptedChar =[]
    for i in range(len(list_2Value)):
        EncryptedChar.append(chr(list_2Value[i]))
    # print(EncryptedChar)    
    string =""
    for i in range(len(EncryptedChar)):
        string = string+(EncryptedChar[i])
    return string    


        


