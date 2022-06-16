# Используя метод "шаг младенца, шаг великана", решить следующие уравнения:
#a=2
a=int(input('a='))
#b=21
b=int(input('b='))
#p=29
p=int(input('p='))

m=k=int(p**0.5)+1
sqp=m-1
# A
masa=[]
ka=1
while ka<=k:
    masa.append(pow(a,ka*m,p))
    ka+=1
#print(masa)

# B
masb=[]
stepen=1
while stepen<=m-1:
    masb.append(pow(b*(a**stepen),1,p))
    stepen+=1
#print(masb)

findelem = list(set(masa).intersection(set(masb)))
i = masa.index(findelem[0])+1
j = masb.index(findelem[0])+1

x = i*m-j
print('Ai: ',masa)
print('Bj: ',masb)
print('x = ',x)