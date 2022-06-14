alpha = 'абвгдежзийклмнопрстуфхцчшщьыъэюя'
def encrypt(s,key):
    res=''
    for c in s:
        res+=alpha[((alpha.index(c)+key)%len(alpha))]
    print('Шифрограмма: ',res)

def decrypt(s,key):
    res=''
    for c in s:
        res+=alpha[(alpha.index(c)-key)%len(alpha)]
    print('Ключ: ',key,'  | Текст: ',res)

while(1):
    key=1
    menu = int(input('1 - зашифровать | 2 - расшифровать: '))
    if menu ==1:
        s = input('Исходный текст: ').strip()
        key = int(input('Ключ: '))
        encrypt(s,key)
    elif menu ==2:
        s = input('Зашифрованный текст: ').strip()
        key=1
        while key<len(alpha):
            decrypt(s,key)
            key+=1
