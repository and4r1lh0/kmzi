# Абоненты некоторой сети применяют подпись Эль-Гамаля с общими параметрами p=23,g=5.
# Для указанных секретных параметров абонентов найти открытый ключ (y) и построить
# подпись лля сообщения m.

#p=23
p=int(input('p='))
#g=5
g=int(input('g='))

#x=11
x=int(input('x='))
#k=3
k=int(input('k='))
#m=h=15
m=h=int(input('m='))

r=pow(g,k,p)
s=pow(pow(h-x*r,1,p-1)*pow(k,-1,p-1),1,p-1)

print('Подпись m: ','<',m,r,s,'>')

#проверка
y=pow(g,x,p)
left = pow((y**r)*(r**s),1,p)
right = pow(g,h,p)
if left==right:
    print(left,'=',right,'=> подпись верна')
else:
    print(left,'!=',right,'=> подпись неверна')