def fast_exp(a, x, p):
    r = 1
    if 1 & x:
        r = a
    while x:
        x >>= 1
        a = (a * a) % p
        if x & 1:
           r = (r * a) % p
    return r

#a = int(input("a: "))
#x = int(input("x: "))
#p = int(input("p: "))
#res = fast_exp(a, x, p)
#print("{} ^ {} mod {} ≡ {}".format(a, x, p, res))

#a = int(input('a = '))
#x = int(input('x = '))
#p = int(input('p = '))

#def res(count):
#     mod=1
#     while count!=0:
#        mod *=a**2%p
#        count-=1
#     return mod

#if x%2==0:
#    count=x/2
#    b = res(count)
#    print(b%p)
#else:
#    count=(x-1)/2
#    b = res(count)
#    b*=a
#    print(b%p)