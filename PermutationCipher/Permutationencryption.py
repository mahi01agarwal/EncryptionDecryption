import random


def encryption(message):
    
    message_ascii=[]
    for i in range(len(message)):
        p = ord(message[i])
        message_ascii.append(p)

    # print(message_ascii)
    random_list=[]

    for r in range(len(message)*len(message)):
        permutation = random.randint(0,len(message)-1)
        if permutation not in random_list:
            random_list.insert(r,permutation)
            if len(random_list) == len(message_ascii):
                break
    # print (random_list)
    file = open("Keys/randomList.bin",'wb')
    for i in random_list:
        file.write(str.encode((f"{str(i)}\n")))
    file.close()    
        



    encrypted_ascii=[]


    for j in range(len(random_list)):
        indx_1=random_list.index(j)

        encrypted_ascii.append(message_ascii[indx_1])
    # print(encrypted_ascii)
    
    

    string =""
    for q in range(len(random_list)):
        encrypted_value=encrypted_ascii[q]
        string = string+chr(encrypted_value)

    return string





