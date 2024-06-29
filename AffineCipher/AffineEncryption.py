
import random
def a_inverse(a):
        c=1
        if a==1:
            return 1
        else:
            for i in range(127*127*127):
                c=c+127
                f=c%a
                if f==0:
                    ans=c/a
                    ans=int(ans)
                    break
        return ans
    
    
    
    
def encryption(message):

    #Generates two random keys key1 and key2
    key1 = random.randint(0,126)
    key2= random.randint(2,126)
   

    #stores key1
    with open('Keys/AffineCipherkey1.bin','wb') as file:
        file.write(str.encode(str(key1)))
        
    #stores key2   
    with open('Keys/AffineCipherkey2.bin','wb') as file:
        file.write(str.encode(str(key2)))
    
    #prob stores the index at which the value present is less than 33      
    prob=[]
    
    #value_y stores the ord value of encrypted characters
    value_y=[]
    for i in range(len(message)):
        p = ord(message[i])
        y= (key2*p+key1)%127
        
        # Add 33 to those values which are less than 33
        if y<33:
            y=y+33
            prob.append(i)
        value_y.append(y)

    #This is a string to store the encrypted string       
    string="" 
    for y in value_y:
        string = string + chr(y)
      
            
    #This will store the prob keys in a file   
    file = open('Keys/AffineCipherProbKeys.bin','wb')
    for p in prob:
        file.write(str.encode((f"{str(p)}\n")))     
            
    #This will store the value_y in a file     
    file = open('Keys/AffineCipherValue_y.bin','wb') 
    for y in value_y:
        file.write(str.encode((f"{str(y)}\n")))
    file.close()   
    
    
    return string

    
    








