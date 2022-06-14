def gcd(a,b):
    while b!=0:
        a,b=b, a%b
    return a

def coprime(a,b):
    return gcd(a,b)==1

def find(num):
    a=1
    res = False
    while res == False:
        a+=1
        res = (coprime(a,num))
        print(res)
    return a


num = 382958857983422
print(find(num))
print(coprime(num,382958857983428))