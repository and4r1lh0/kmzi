import matplotlib.pyplot as plt
 
def plot(a,b,p):
    #data to be plotted
    resx=[];resy=[]
    for x in range(p):
        for y in range(p):
            if (y**2)%p==(x**3+a*x+b)%p:
                resx.append(x%p);resy.append(y%p)
    #preprocessing
    result=[]
    for el in range(len(resx)) and range(len(resy)):
        processing = '('+str(resx[el])+', '+str(resy[el])+') '
        result.append(processing)
    print('Точки: ',*result, sep=",  "[1:-1])
  
def add(x1,y1,x2,y2,p):
    lam = ((y2-y1)*pow(x2-x1,-1,p))%p
    x3 = (lam**2-x1-x2)%p
    y3 = (lam*(x1-x3)-y1)%p
    return x3%p,y3%p

def mul(x1,y1,a,p):
    lam = ((3*x1**2+a)*(pow(2*y1,-1,p)))%p
    x3 = (lam**2-2*x1)%p
    y3 = (lam*(x1-x3)-y1)%p
    return x3%p,y3%p

#параметры кривой
a=2
b=6
p=7

plot(a,b,p) #построение графика кривой

#параметры точек
x1=4
y1=6
x2=4#=x1
y2=6#=y2

if x1!=x2:
    print(add(x1,y1,x2,y2,p)) #сложение точек
elif y1==y2:
    print(mul(x1,y1,a,p)) #удвоение точек
else:
    print('особая точка')