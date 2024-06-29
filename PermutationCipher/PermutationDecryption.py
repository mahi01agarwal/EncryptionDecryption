
def decryption(message):
    random_list=[]
    file = open("Keys/randomList.bin","rb")
    for line in file:
        # print(line)
        random_list.append(int(line))


    encrypted_ascii=[]
    for i in range(len(message)):
        encrypted_ascii.append(ord(message[i]))


    decrypted_ascii=[]





    for y in range (len(random_list)):
            indx=random_list[y]
            # print(indx)
            # print(encrypted_ascii[indx])
            decrypted_ascii.append(encrypted_ascii[indx])
        # print(decrypted_ascii)
        


    string =""
    for h in range(len(decrypted_ascii)):
            decrypted_value=decrypted_ascii[h]

            string = string + chr(decrypted_value)
            
    return string   

