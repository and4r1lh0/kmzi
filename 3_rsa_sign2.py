# Для указанных открытых ключей пользователя RSA
# проверить подлинность подписанных сообщений.

#N=55
N=int(input('N='))
#d=3
d=int(input('d='))
#m=7
m=int(input('m='))
#s=28
s=int(input('s='))

h=pow(s,d,N)
if h==m:
    print('h = ',h, ' - подпись верна')
else:
    print('h = ',h, ' - подпись неверная')