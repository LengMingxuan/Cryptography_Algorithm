import os
import sys
# define a 2
str1:str = sys.argv[1]
K:int = sys.argv[2]
print("str1 = ",str1,'\n',"K = ",K)


dirWordToNum = {
    "A": 1, "B": 2, "C": 3, "D": 4,
    "E": 5, "F": 6, "G": 7, "H": 8,
    "I": 9, "J": 10, "K": 11, "L": 12,
    "M": 13, "N": 14, "O": 15, "P": 16,
    "Q": 17, "R": 18, "S": 19, "T": 20,
    "U": 21, "V": 22, "W": 23, "X": 24,
    "Y": 25, "Z": 26
}
dirNumToWord = {
    1:'A' , 2: 'B',3:'C',4:'D',
    5:'E',6:'F',7:'G',8:'H',9:'I',
    10:'J',11:'K',12:'L',13:'M',
    14:'N',15:'O',16:'P',17:'Q',
    18:'R',19:'S',20:'T',21:'U',
    22:'V',23:'W',24:'X',25:'Y',
    26:'Z'
}
for str in str1:
    m:int = dirWordToNum[str]
    C:int = (int(m) * int(K)) % 26
    print(dirNumToWord[C],end='')
print('\n')
