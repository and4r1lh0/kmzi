# Для указанных открытых ключей (y) пользователей системы Эль-Гамаля с 
# общими параметрами p=23, g=5 проверить подлинность подписанных сообщений 

#p=23
p=int(input('p='))
#g=5
g=int(input('g='))
#y=22
y=int(input('y='))
#m=h=5
m=h=int(input('m='))
#r=11
r=int(input('r='))
#s=3
s=int(input('s='))

#проверка
left = pow((y**r)*(r**s),1,p)
right = pow(g,h,p)
if left==right:
    print(left,'=',right,'=> сообщение подлинное')
else:
    print(left,'!=',right,'=> сообщение не является подлинным')