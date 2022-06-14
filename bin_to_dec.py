def bin_to_dec(digit):
    dec=0
    for i in range(0, len(digit)):
        dec=dec+int(digit[i])*(2**(len(digit)-i-1))
    return dec