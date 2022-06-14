# Система Диффи - Хеллмана | Задание 1 | Написать программный модуль, вычисляющий открытые ключи абонентов А и В ( YA и YВ ) 
# и их общий ключ (ZAB,ZBA ) по заданным p,g и секретным ключам XA,XB . 
# Проверить условие ZAB = ZBA.

q=2000000101943
p=4000000203887
g=19
Xalice=3624834069141
Xbob=443730291506
Ya = pow(g,Xalice,p)
Yb = pow(g,Xbob,p)
Zab = pow(Yb,Xalice,p)
Zba = pow(Ya,Xbob,p)
print('Задание 1\nY_Alice = ',Ya,
	  '\nY_Bob = ',Yb,
	  '\nZ_ab = ',Zab,
	  '\nZ_ba = ',Zba)

# Задание 2 | Написать программный модуль, вычисляющий по заданному простому числу q (p = 2q+1) 
# минимальный подходящий параметр g, случайные секретные ключи абонентов XA, XB, 
# соответствующие им открытые ключи YA, YВ и их общий ключ ( ZAB, ZBA ).
# Проверить условие ZAB = ZBA.

q1 = 4000003001363
p1= 2*q1 + 1
print('p = ',p)
g1=2
while(pow(g1,p1-1,p1)==1 and pow(g1,q1,p1)==1):
	g1+=1
print('g = ',g1)

Xalice1=5078
Xbob1=1650
Ya1 = pow(g1,Xalice1,p1)
Yb1 = pow(g1,Xbob1,p1)
Zab1 = pow(Yb1,Xalice1,p1)
Zba1 = pow(Ya1,Xbob1,p1)
print('Задание 2\nY_Alice = ',Ya1,
	  '\nY_Bob = ',Yb1,
	  '\nZ_ab = ',Zab1,
	  '\nZ_ba = ',Zba1)