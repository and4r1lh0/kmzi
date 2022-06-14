import caesar
import dec_to_bin as db
import bin_to_dec as bd

mydict = {
    '00000':'а',
    '00001':'б',
    '00010':'в',
    '00011':'г',
    '00100':'д',
    '00101':'е',
    '00110':'ж',
    '00111':'з',
    '01000':'и',
    '01001':'й',
    '01010':'к',
    '01011':'л',
    '01100':'м',
    '01101':'н',
    '01110':'о',
    '01111':'п',
    '10000':'р',
    '10001':'с',
    '10010':'т',
    '10011':'у',
    '10100':'ф',
    '10101':'х',
    '10110':'ц',
    '10111':'ч',
    '11000':'ш',
    '11001':'щ',
    '11101':'э',
    '11110':'ю',
    '11111':'я',
    '11010':'ъ',
    '11100':'ь',
    '11011': 'ы',
    }

#def roundUp(number):
#   return number + (10-(number%10))

#inv_dict = dict(reversed(item) for item in mydict.items())
inv_dict = dict(zip(mydict.values(), mydict.keys()))
from math import ceil, sqrt
def dec(mes): #двоичный код
    cypher = mes.split(',')
    mas_cypher = [int(x) for x in cypher]
    result_str = ""
    el=0 
    while el < len(cypher):
        a = int(mas_cypher[el])
        dec_num = db.bin(a)
        a = len(dec_num)
        a +=(10-(a%10))
        #if len(dec_num)==60:
        if len(dec_num)==a:
            pass
        else:
            #dec_num=dec_num.zfill(60)          #   кодирование
            #dec_num=dec_num.rjust(60,'0')      #   декодирование
            dec_num=dec_num.rjust(a,'0')        #   декодирование
        
        result = [dec_num[i:i+5] for i in range(0, len(dec_num),5)]
        for i in result:
            result_str += mydict[i]
            el+=1
    return caesar.dec(result_str,0)

def enc(mes): #текст
    result = [mes[i:i+1] for i in range(0, len(mes),1)]
    result_str = ''
    el=0
    for i in result:
            result_str += inv_dict[i]
            el+=1
    result_str = bd.bin_to_dec(result_str)
    return result_str