# Во всех задачах будем предполагать что h(m)=m для всех значений m.
# Построить подпись RSA для сообщения m при следующих параметрах польхователя.

#p=5
p=int(input('p='))
#q=11
q=int(input('q='))
#c=27
c=int(input('c='))
#m=7
m=int(input('m='))

N = p*q
s=pow(m,c,N)
print('Подпись: <',m,',',s,'>')