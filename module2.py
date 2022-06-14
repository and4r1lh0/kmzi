alph = ['а','б','в','г','д','е','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ш','щ','ь','ы','ъ','э','ю','я']
str1=list(str(input()))
key=1
i = 1
while i<len(alph):
    if i+key>len(alph):
        a = (i+key)%len(alph)
        print(a)
        index = alph.index(str1[a])
    else:
        index=alph.index(str1[i])
    findex = index+key
    print(alph[findex])
    i+=1

    #вариант 5