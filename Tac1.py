seq = input("insira a sequencia :")
count = 1
lista = []
seq = seq.upper()

for x in range(1, len(seq)):
    if seq[x] == seq[x - 1]:
        count += 1
        if count == 3:
            posi = x - 1

    elif seq[x] != seq[x - 1]:
        if count >= 3:
            lista.append((seq[x - 1], count, posi))
            count = 1
        else:
            count = 1
print(lista)
