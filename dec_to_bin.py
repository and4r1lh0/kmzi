def bin(dec):
    bin = ''
    while dec > 0:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin