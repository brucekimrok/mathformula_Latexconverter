from map import *

def conv0(inputsentence):
    words = inputsentence.split('; ')
    trans0 = []
    for elmt in words:
        if elmt in brc0:
            trans0.append(brc0[elmt])
        elif elmt in div:
            trans0.append(div[elmt])
        elif elmt in brc1b:
            trans0.append(brc1b[elmt])
        elif elmt in brc1f:
            trans0.append(brc1f[elmt])
        else:
            trans0.append(elmt)
    return trans0

def conv1(a):
    bfbrc1 = a
    i = 0
    while i < len(bfbrc1):
        if bfbrc1[i] in brc1bb:
            bfbrc1.insert(i+1, '}')
            bfbrc1[i-1], bfbrc1[i] = bfbrc1[i], bfbrc1[i-1]
        i += 1
    afbrc1 = []
    afbrc1 = bfbrc1
    return afbrc1

def conv2(b):
    bfbrc2 = b
    i = 0
    while i < len(bfbrc2):
        if bfbrc2[i] in brc1ff:
            bfbrc2.insert(i+2, '}')
        i += 1
    afbrc2 = bfbrc2
    return afbrc2


def div1(c):
    bfdiv = c
    i = bfdiv.count('/')
    j = bfdiv.count('=')

    if i > 1:
        print("type one equation at a time")
    else:
        if j == 0:

            divv = bfdiv.index('/')
            bfdiv.append('}')
            bfdiv.insert(divv + 1, '{')
            bfdiv.insert(divv, '}')
            bfdiv.insert(0, '\\frac{')

        elif j == 1:
            eqq = bfdiv.index('=')
            divv = bfdiv.index('/')
            bfdiv.insert(eqq, '}')
            bfdiv.insert(divv+1, '{')
            bfdiv.insert(divv, '}')
            bfdiv.insert(0, '\\frac{')
    rmv_divv = bfdiv.index('/')
    bfdiv.pop(rmv_divv)
    return bfdiv

def main():
    trans0 = conv0(input("Enter: "))
    afbrc1 = conv1(trans0)
    afbrc2 = conv2(afbrc1)
    if '/' in afbrc2:
        afdiv=div1(afbrc2)
    else:
        afdiv = afbrc2
    latex_str = ' '.join(afdiv)
    print(latex_str)
