# В системе RSA с заданными параметрами p_a, q_a, d_a найти недостающие параметры
# и описать процесс передачи сообщения m пользователю A.

#p=5
p=int(input('p_a='))
#q=11
q=int(input('q_a='))
#d=3
d=int(input('d_a='))
#m=12
m=int(input('m='))

N=p*q
phi_N=(p-1)*(q-1)
c=pow(d,-1,phi_N)
e=pow(m,d,N)
m_s=pow(e,c,N)

print('N =',N,'\nphi_N = ',phi_N,'\nc = ',c,'\ne = ',e,'\nm_s = ',m_s)