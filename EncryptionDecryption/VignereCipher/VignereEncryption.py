def encryption(message):    

    import random
    randomListLength = random.randint(2,len(message))
    randomList=[]
    for i in range(0,randomListLength):
        randomList.append(random.randint(33,126))
        
    # print(randomList)    
        
    MessageAscii =[]
    for i in range(len(message)):
        MessageAscii.append(ord(message[i]))

    # print(f"MessageAscii={MessageAscii}")


    for i in range(len(message)-len(randomList)):
        randomList.append(randomList[i])
        
    # print(f"RandomList = {randomList}")  


    file = open('Keys/VignereCipherRandomList.bin','wb')
    for p in randomList:
        file.write(str.encode((f"{str(p)}\n")))

    # print(len(randomList))
    # print(len(message)) 
    probList =[]
    Encrypted_list =[]
    for i in range(len(message)):

        encrypted = ((MessageAscii[i])+(randomList[i])) %127
        if encrypted<33:
            probList.append(i)
            encrypted = encrypted+33
            Encrypted_list.append(encrypted)
        else:
            Encrypted_list.append(encrypted)    
        
    # print(Encrypted_list)    
    # print(probList)


    string =""  
    for y in Encrypted_list:
        string = string +(chr(y))
     


    file = open('Keys/VignereCipherProbKeys.bin','wb')
    for p in probList:
        file.write(str.encode((f"{str(p)}\n"))) 

    return string














