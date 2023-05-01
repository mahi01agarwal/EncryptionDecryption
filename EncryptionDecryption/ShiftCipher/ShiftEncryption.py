def encryption(message):
    import random
    k= random.randint(0,1000000)
    with open('Keys/ShiftCipherKeysUsed.bin','wb') as file:
        file.write(str.encode((str(k)))) 

    prob = []
    value_y = []
    for i in range(len(message)):
        p = ord(message[i])
        y = (p+k)%127
        
        if y < 33:
            y = y + 33
            prob.append(i)
            
        value_y.append((y))
    # print(value_y)


    
    string = ""
    for y in value_y:
        string = string +(chr(y))
      
            
            
            
    file = open('Keys/ShiftCipherProbKeys.bin','wb')
    for p in prob:
        file.write(str.encode((f"{str(p)}\n")))        
            
            
    file = open('Keys/ShiftCipherValue_y.bin','wb') 
    for y in value_y:
        file.write(str.encode((f"{str(y)}\n")))
    file.close()            

    return string         
                        