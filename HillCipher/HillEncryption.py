import numpy
import random

def a_inverse(a):
    c=1
    if a==1:
        return 1
    else:
        for i in range(127*127):
            c=c+127
            f=c%a
            if f==0:
                ans=c/a
                ans=int(ans)
                break
    return ans

def encryption(message):
    message1=message
    #This will store the original mesaage
    with open('Keys/HillCiphermessage.bin','wb') as file:
        file.write(str.encode((message1)))
     
     
    #Checks if the message is of odd length and adds x at the end for odd length message    
    if len(message1)%2 ==1:
        message = message1 +"x"
    else:
        message = message1       
            
    #Stores length of message in file
    with open('Keys/HillCipherlength.bin','wb') as file:
        file.write(str.encode((str(len(message)) ))  ) 
    
    
    #Generates a random key matrix  ensuring that its determinant should not be zero
    while True:
        Key_matrix = numpy.matrix([[random.randint(1,127),random.randint(1,127)],[random.randint(1,127),random.randint(1,127)]])
        determinantKeyMatrix = Key_matrix[0,0]*Key_matrix[1,1] -Key_matrix[0,1]*Key_matrix[1,0]
        if determinantKeyMatrix==0:
            continue
        else:
            break
        
        
    #Stores key matrix in a file
    file = open('Keys/HillCipherKeyMatrix.bin','wb')
    for i in range(0,2):
        for j in range(0,2):
            file.write(str.encode((f"{str(Key_matrix[i,j])}\n")))     
    file.close()

    #Generates  cipher matrix  for every two characters and adds it in the cipher matrices list
    cipher_matrices =[]
    i =0
    while i<=(len(message)-2):
        message_matrix = numpy.array([[ord(message[i]),ord(message[i+1])]])
        # print(f"Message Matrix:{message_matrix}")
        i=i+2
        cipher_matrix = (message_matrix*Key_matrix)%127
        # print(f"Cipher matrix:{cipher_matrix}")
    
        cipher_matrices.append(cipher_matrix)   
    # print(cipher_matrices)
    # print(len(cipher_matrices))

    
    #Generates cipherkeys list from cipher matrices , cipher keys list stores ord value of each encrypted character
    CipherKeys =[]
    for i in range(len(cipher_matrices)):
        for j in range(0,1):
            for k in range(0,2):
                CipherKeys.append(int(cipher_matrices[i][j,k]))
    # print(CipherKeys)
    # print(len(CipherKeys))

    #Convert the ord values of encrypted charcter into its corresponding character values and store in string to return it.
    string =""
    probKeys=[]
    for i in range(len(CipherKeys)):
        if CipherKeys[i]<33:
            CipherKeys[i]=CipherKeys[i]+33
            probKeys.append(i)
            string = string +(chr(CipherKeys[i]))
        else:
            string = string +(chr(CipherKeys[i]))
    
    
    
    #This store the prob keys in a file        
    file = open('Keys/HillCipherProbKeys.bin','wb')
    for p in probKeys:
        file.write(str.encode((f"{str(p)}\n")))  
                
        
    return string


        


                    
                    


    