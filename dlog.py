import math;
 
def dlog(a, b, m):
 
    n = int(math.sqrt (m) + 1);
    an = 1;
    for i in range(n):
        an = (an * a) % m;
 
    value = [0] * m;
 
    cur = an;
    for i in range(1, n + 1):
        if (value[ cur ] == 0):
            value[ cur ] = i;
        cur = (cur * an) % m;
     
    cur = b;
    for i in range(n + 1):
         
        if (value[cur] > 0):
            ans = value[cur] * n - i;
            if (ans < m):
                return ans;
        cur = (cur * a) % m;
 
    return None;
 

# проверка
#print(dlog(7894352216, 355407489, 604604729))
#print(dlog(2, 238217112, 1170278003))