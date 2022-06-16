# Для шифра Эль-Гамаля с заданными параметрами p,g,c_b,k найти недостающие 
# параметры и описать процесс передачи сообщения пользователю B.
#p=19
p=int(input('p='))
#g=2
g=int(input('g='))
#c_b=5
c_b=int(input('c_b='))
#k=7
k=int(input('k='))
#m=5
m=int(input('m='))

q=int((p-1)/2)
x=c_b
y=pow(g,x,p)
r=pow(g,k,p)
e=pow(m*pow(y,k,p),1,p)     #A=>B: (r,e)
m=pow(e*pow(r,p-1-x,p),1,p) #B

print('q =',q,'\nx = ',x,'\ny = ',y,'\nr = ',r,'\ne = ',e,'\nm = ',m)