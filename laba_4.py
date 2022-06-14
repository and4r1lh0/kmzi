# Шифр Эль-Гамаля | Задание 1 | Написать программный модуль, вычисляющий открытый ключ YB и передачу 
# сообщения m от абонента А абоненту В (r,e,m') по заданным p,g,m,k и 
# секретному ключу XB. Проверить условие m=m'.

import cypher as c
m_text = 'двенадцать'
p = 1001946480241570103
g = 10
m = c.enc(m_text) #143122273862236
k = 662818379273261268
X_Bob = 956333284754940149

Y_Bob = pow(g,X_Bob,p)
r=pow(g,k,p)
e=pow(m*pow(Y_Bob,k,p),1,p)
m_s = pow(e*pow(r,p-1-X_Bob,p),1,p) # m_s == m

print('----------Задание 1----------\nm = ',m_text,
      '\np = ',p,
      '\ng = ',g,
      '\nm = ',m,
      '\nk = ',k,
      '\nX_Bob = ',X_Bob,
      '\n\nY_Bob = ',Y_Bob,
      '\nr = ',r,
      '\ne = ',e,
      '\nm_s = ',m_s,)

import time
# Задание 2 | Написать программный модуль, вычисляющий по заданным числам p и g,
# открытому ключу YB и сообщению (r,e) секретный ключ XB и сообщение m'. 
# Проверить условие m m=m'. Оценить время расчёта, в зависимости от значений
# простого числа p, заданного преподавателем.

p = 1410023
g = 5
Y_Bob = 381823
r = 1038249
e = 642344

print('\n----------Задание 2 | Часть 1----------\np = ',p,
      '\ng = ',g,
      '\nY_Bob = ',Y_Bob,
      '\nr = ',r,
      '\ne = ',e)
start_time = time.time()
Y_Bob_check=0
X_Bob=0
while Y_Bob_check!=Y_Bob:
    Y_Bob_check = pow(g,X_Bob,p) #381823
    X_Bob+=1
X_Bob -=1 #544019
print('\nX_Bob = ',X_Bob)

m_s = pow(e*pow(r,p-1-X_Bob,p),1,p) # m_s == m
print('m̒ = ',m_s)
m_text = c.dec(str(m_s))
print('m(текст) = ',m_text.lstrip('а'))
print("Время расчёта X_Bob и m̒:  %s секунд" % (time.time() - start_time))
r_check=0
k=0
while r_check!=r:
    r_check = pow(g,k,p)
    k+=1
k -=1
print('k = ',k)

e_check=0
m=0
while e_check!=e:
    e_check = pow(m*pow(Y_Bob,k,p),1,p)
    m+=1
m -=1
print('m = ',m)
print("Общее время расчёта:  %s секунд" % (time.time() - start_time))

###

p = 44818547
g = 2
Y_Bob = 27715800
r = 25375975
e = 28734097

print('\n----------Задание 2 | Часть 2-----------\np = ',p,
      '\ng = ',g,
      '\nY_Bob = ',Y_Bob,
      '\nr = ',r,
      '\ne = ',e)
start_time = time.time()
Y_Bob_check=0
X_Bob=0
while Y_Bob_check!=Y_Bob:
    Y_Bob_check = pow(g,X_Bob,p) #381823
    X_Bob+=1
X_Bob -=1 #544019
print('\nX_Bob = ',X_Bob)

m_s = pow(e*pow(r,p-1-X_Bob,p),1,p) # m_s == m
print('m̒ = ',m_s)
m_text = c.dec(str(m_s))
print('m(текст) = ',m_text.lstrip('а'))
print("Время расчёта X_Bob и m̒:  %s секунд" % (time.time() - start_time))
r_check=0
k=0
while r_check!=r:
    r_check = pow(g,k,p)
    k+=1
k -=1
print('k = ',k)

e_check=0
m=0
while e_check!=e:
    e_check = pow(m*pow(Y_Bob,k,p),1,p)
    m+=1
m -=1
print('m = ',m)
print("Общее время расчёта:  %s секунд" % (time.time() - start_time))

###

p = 1170278003
g = 2
Y_Bob = 238217112
r = 1032729867
e = 422295684

print('\n----------Задание 2 | Часть 3-----------\np = ',p,
      '\ng = ',g,
      '\nY_Bob = ',Y_Bob,
      '\nr = ',r,
      '\ne = ',e)
start_time = time.time()
Y_Bob_check=0
X_Bob=0
while Y_Bob_check!=Y_Bob:
    Y_Bob_check = pow(g,X_Bob,p) #381823
    X_Bob+=1
X_Bob -=1 #544019
print('\nX_Bob = ',X_Bob)

m_s = pow(e*pow(r,p-1-X_Bob,p),1,p) # m_s == m
print('m̒ = ',m_s)
m_text = c.dec(str(m_s))
print('m(текст) = ',m_text.lstrip('а'))
print("Время расчёта X_Bob и m̒:  %s секунд" % (time.time() - start_time))
r_check=0
k=0
while r_check!=r:
    r_check = pow(g,k,p)
    k+=1
k -=1
print('k = ',k)

e_check=0
m=0
while e_check!=e:
    e_check = pow(m*pow(Y_Bob,k,p),1,p)
    m+=1
m -=1
print('m = ',m)
print("Общее время расчёта:  %s секунд" % (time.time() - start_time))