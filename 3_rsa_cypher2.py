# Пользователю системы RSA с параметрами N = 187, d = 3 передано 
# зашифрованное сообщение e=100. Расшифровать это сообщение,
# взломав систему RSA пользователя.

#N=187
N=int(input('N='))
#d=3
d=int(input('d='))
#e=100
e=int(input('e='))

e_check=0
m=0
while e_check!=e:
    e_check=pow(m,d,N)
    m+=1
print('m = ',m-1)