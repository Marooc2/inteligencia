def xor(p,q):
    z= (p and not q) or (not p and q)
    return z
def bicondiciona2(p,q):
    z = not xor(p,q)
    return z

if __name__ == '__main__':
    Datos = []
    p = [False,True]
    q = [False, True]
    for pval in p:
        for qval in q:
            Lista = []
            Lista.append(pval)
            Lista.append(qval)
            Datos.append(Lista)
    for (p,q) in Datos:
       print(p,q,bicondiciona2(p,q))

