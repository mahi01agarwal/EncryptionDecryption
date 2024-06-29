import sys
import os
def findfile(name, path):
    for dirpath, dirname, filename in os.walk(path):
        if name in filename:
            return os.path.join(dirpath, name)


sys.path.insert(0,findfile('AffineDecryption.py','/users'))
sys.path.insert(0,findfile("HillDecryption.py",'/users'))
sys.path.insert(0,findfile("PermutationDecryption.py",'/users'))
sys.path.insert(0,findfile("ShiftDecryption.py",'/users'))
sys.path.insert(0,findfile("VignereDecryption.py",'/users'))
sys.path.insert(0,findfile("SubstitutionDecryption.py",'/users'))


from AffineCipher import AffineDecryption
from ShiftCipher import ShiftDecryption
from SubstitutionCipher import SubstitutionDecryption
from VignereCipher import VignereDecryption
from HillCipher import HillDecryption
from PermutationCipher import PermutationDecryption




with open('Encrypted.txt','r') as file:
    message = file.read()
randomNumList =[]


with open('Keys/randomList.txt','r') as file:
    for line in file:
        randomNumList.append(int(line))
# print(randomNumList)    
    
def decryption(argument):
    match argument:
        case 1:
            return AffineDecryption.decryption(message)
        case 2:
            return HillDecryption.decryption(message)
        case 3:
            return ShiftDecryption.decryption(message)
        case 4:
            return SubstitutionDecryption.decryption(message)
        case 5:
            return VignereDecryption.decryption(message)  
        case 6:
            return PermutationDecryption.decryption(message)
        
        
message = decryption(randomNumList[5])  #message ko overwrite kar diya
# print(message)
message = decryption(randomNumList[4])  #message ko overwrite kar diya
# print(message)
message=decryption(randomNumList[3])
# print(message)
message=decryption(randomNumList[2])
# print(message)
message=decryption(randomNumList[1])
# print(message)
message=decryption(randomNumList[0])
# print(message)

with open('Decrypted.txt',"w") as file:
    file.write(message)





