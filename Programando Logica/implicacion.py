def implicacion(p,q):
    if (p == False):
        z = True
    else:
        z = q
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
       print(p,q, implicacion(p,q))

