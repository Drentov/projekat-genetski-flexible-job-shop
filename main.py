import random

"""
Primer vremena:
vremena = [
    [[1,2], [3, -1]],
    [[2,1], [-1,1], [2,3]]
]
"""

# 0<p<1 - verovatnoća da će neka mašina podržavati neku operaciju
def generisiNizVremena(broj_poslova, min_op, max_op, broj_masina, p):
    vremena = []
    for i in range(broj_poslova):
        posao = []
        broj_op = random.randint(min_op, max_op)
        for j in range(broj_op):
            operacija = []
            for k in range(broj_masina):
                if random.random() > p:
                    operacija.append(-1)
                else:
                    operacija.append(random.randint(1, 10))
            if all(i==-1 for i in operacija):
                operacija[random.randint(0, broj_masina-1)] = random.randint(1, 10)
            posao.append(operacija)
        vremena.append(posao)
    return vremena

# vremena[posao][operacija][mašina]
vremena = generisiNizVremena(10, 2, 100, 100, 0.8)
broj_poslova = len(vremena)
broj_operacija_po_poslu = [len(posao) for posao in vremena]
broj_masina = len(vremena[0][0])

# Vraća listu u kojoj je prvi element OS (niz indeksa poslova), a drugi element MS (niz indeksa mašina)
def napraviJedinku():
    operacije = []
    for i in range(broj_poslova):
        operacije.extend(i for _ in range(broj_operacija_po_poslu[i]))

    random.shuffle(operacije)
    brojac_operacija = [0]*broj_poslova

    masine = []
    for posao in operacije:
        operacija = brojac_operacija[posao]
        brojac_operacija[posao] += 1

        sled_masina = random.randint(0, broj_masina-1)
        if vremena[posao][operacija][sled_masina] == -1:
            for i in range(broj_masina):
                if vremena[posao][operacija][(sled_masina + i)%broj_masina] != -1:
                    sled_masina = (sled_masina + i) % broj_masina

        masine.append(sled_masina)

    return operacije, masine
    

# Prima listu [OS, MS]
# U i-tom trenutku se dodaje naredna operacija posla OS[i] u mašinu MS[i] (tako da počinje u najraniji trenutak)
def trajanje(jedinka):
    masine = [0]*broj_masina
    poslovi = [0]*broj_poslova
    brojac_operacija = [0]*broj_poslova

    for op in range(len(jedinka[0])):
        posao = jedinka[0][op]
        masina = jedinka[1][op]
        operacija = brojac_operacija[posao]
        trajanje = vremena[posao][operacija][masina]

        start = max(masine[masina], poslovi[posao])
        finish = start+trajanje

        #print(f"O_{posao+1},{operacija+1} izvršena na mašini M_{masina+1} u trajanju od {trajanje} ({start}-{finish})")
        
        masine[masina] = finish
        poslovi[posao] = finish
        brojac_operacija[posao] += 1

    print(f"Ukupno je bilo potrebno {max(masine)} jedinica vremena")
    return max(masine)
        
def main():
    jedinke = []
    for i in range(10):
        jedinke.append(napraviJedinku())

    for jed in jedinke:
        trajanje(jed)

if __name__=="__main__":
    main()