# Для шифра Шамира с заданными параметрами p, c_a, c_b найдите недостающие 
# параметры о опишите процесс передачи сообщения m от A к B:

#p=19
p=int(input('p='))
#c_a=5
c_a=int(input('c_a='))
#c_b=7
c_b=int(input('c_b='))
#m=4
m=int(input('m='))

d_a = pow(c_a,-1,p-1) 
print('d_a: ',d_a)
d_b = pow(c_b,-1,p-1)
print('d_b: ',d_b)

x1 = pow(m,c_a,p)   # A=>B
x2 = pow(x1,c_b,p)  # B=>A
x3 = pow(x2,d_a,p)  # A=>B
x4 = m = pow(x3,d_b,p)  # B:
print('x1 =',x1,'\nx2= ',x2,'\nx3= ',x3,'\nx4= ',x4)