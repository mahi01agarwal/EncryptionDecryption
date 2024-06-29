import numpy

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


def decryption(message):
    
    
    #Reads the keymatrix and stores it in Key_matrix
    with open('Keys/HillCipherKeyMatrix.bin','rb') as file:
        a = file.readline()
        b = file.readline()
        c = file.readline()
        d = file.readline()
    Key_matrix = numpy.matrix([[int(a),int(b)],[int(c),int(d)]])    
    # print(Key_matrix)
    
    #reads length of message stored in file
    with open("Keys/HillCipherlength.bin",'rb') as file:
        length = int((int(file.read())))

    #reads problist from file
    problist= []
    file = open('Keys/HillCipherProbKeys.bin','rb')
    for line in file:
        problist.append(int(line))


    #reads the cipher matrices and stores it in cipher_matrices
    cipher_matrices =[]
    value=[]
    # file=open('Encrypted.txt','r') 
    # message = file.read() 
    for i in range(length):
        if i in problist:
            value_j =(ord(message[i]))-33 
            value.append(value_j)
        else:
            value.append(ord(message[i]))  
    file.close()  
    i=0
    while i<length :
        cipher_matrix = numpy.matrix([value[i],value[i+1]]) 
        cipher_matrices.append(cipher_matrix)
        i=i+2
    # print(cipher_matrices)    
            




    determinantKeyMatrix = Key_matrix[0,0]*Key_matrix[1,1] -Key_matrix[0,1]*Key_matrix[1,0] 
    # print(determinantKeyMatrix)


    adjointOfKeyMatrix =  (numpy.matrix([[Key_matrix[1,1],(-1*Key_matrix[0,1])],[(-1*Key_matrix[1,0]),Key_matrix[0,0]]]))
    # print(adjointOfKeyMatrix)

    InverseOfDeterminant = a_inverse(determinantKeyMatrix)
    # print(InverseOfDeterminant)


    FinalInverseMatrix = (InverseOfDeterminant * adjointOfKeyMatrix)
    # print(f"Inverse Matrix : {FinalInverseMatrix}")
    file = open("Keys/HillCiphermessage.bin","rb") 
    message1 = file.read()
    file.close()

    if len(message)==len(message1):
        List=[]  
        for i in range(len(cipher_matrices)):
            Decrypted_matrix = (cipher_matrices[i] * FinalInverseMatrix)%127
        #   print(f"DEcryptedMatrix : {Decrypted_matrix}")
            DecryptedCharactersMatrix = numpy.matrix([(chr(Decrypted_matrix[0,0]),chr(Decrypted_matrix[0,1]))])
        
        #   print(DecryptedCharactersMatrix) 
            List.append(DecryptedCharactersMatrix[0,0])   
            List.append(DecryptedCharactersMatrix[0,1])
        string = ""
        for i in range(len(List)):
            string = string +(List[i])
        
        return string             
    else:
        
        List=[]
        for i in range(len(cipher_matrices)):
            Decrypted_matrix = (cipher_matrices[i] * FinalInverseMatrix)%127
        #   print(f"DEcryptedMatrix : {Decrypted_matrix}")
            DecryptedCharactersMatrix = numpy.matrix([(chr(Decrypted_matrix[0,0]),chr(Decrypted_matrix[0,1]))])
        
        # #   print(DecryptedCharactersMatrix) 
        #     file.write(DecryptedCharactersMatrix[0,0])   
        #     file.write(DecryptedCharactersMatrix[0,1])
            List.append(DecryptedCharactersMatrix[0,0])
            List.append(DecryptedCharactersMatrix[0,1])
            
        List.pop()    
        # print(List)
        string = ""
        for i in range(len(List)):
            string = string +(List[i])
        
        return string
        


        
                
            

            