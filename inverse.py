def inverse(a, b):
    if a == 0 :
        return b,0,1
    z,x1,y1 = inverse(b%a, a)
    x = y1 - (b//a) * x1
    y = x1
    return z,x,y

while(1):
    a =  int(input('Элемент: '))
    m = int(input('Модуль: '))
    z, x, y = inverse(a, m)
    if z == 1:
        print((x % m + m) % m)
    else:
        print('Обратного элемента не существует')