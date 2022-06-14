alpha = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
def encrypt(s,key):
    res=''
    for symbol in s:
        res+=alpha[((alpha.index(symbol)+key)%len(alpha))]
    print('Зашифрованный текст: ',res)

def decrypt(s,key):
    res=''
    for symbol in s:
        res+=alpha[(alpha.index(symbol)-key)%len(alpha)]
    print('Ключ: ',key,'  | Текст: ',res)

#while(1):
#    menu = int(input('1 - зашифровать | 2 - расшифровать: '))
#    if menu ==1:
#        encrypt(input('Исходный текст: ').strip(),int(input('Ключ: ')))
#    elif menu ==2:
        
#s = input('Зашифрованный текст: ').strip()
#key=1
#while key<len(alpha):
#    decrypt(s,key)
#    key+=1

def enc(s,key):
    res=''
    for symbol in s:
        res+=alpha[((alpha.index(symbol)+key)%len(alpha))]
    return res

def dec(s,key):
    res=''
    for symbol in s:
        res+=alpha[(alpha.index(symbol)-key)%len(alpha)]
    return res