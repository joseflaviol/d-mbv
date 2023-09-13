import random

from npe.npe_class import NPE

def sprn(npe: NPE):
    n = npe.n 
    d = npe.d 

    ip = random.randint(0, len(n) - 1)
    fp = ip + 1

    while (fp < len(n)) and (d[fp] > d[ip]):
        fp = fp + 1
    
    rp = range(ip, fp)

    ia    = None 
    tries = 0

    while ia is None and tries < 10:
        try:
            ia = n.index( random.choice( list( npe.graph.adj(n[ip]) )) )

            if ia in rp:
                ia = None
        except ValueError:
            ia = None 

        tries = tries + 1

    if ia is None:
        return npe

    new_n = [n[x] for x in range(0, ia + 1) if x not in rp]
    new_d = [d[y] for y in range(0, ia + 1) if y not in rp]

    for i in rp:
        new_n.append(n[i])
        new_d.append(d[i] - d[ip] + d[ia] + 1)

    new_n += [n[x] for x in range(ia + 1, len(n)) if x not in rp]
    new_d += [d[y] for y in range(ia + 1, len(n)) if y not in rp]

    new_npe = NPE(npe.graph, autostart = False)
    new_npe.n = new_n
    new_npe.d = new_d

    return new_npe

def tbrn(npe: NPE):
    pass