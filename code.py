from collections import Counter

def monobitTest(s):
    numeroDe1 = 0
    
    for bit in s:
        if bit == '1':
            numeroDe1 += 1               
    if (numeroDe1 > 9654) and (numeroDe1 < 10346):
        return True
    else:
        return False

def monobitQuantityTest(s):
    numeroDe1 = 0
    
    for bit in s:
        if bit == '1':
            numeroDe1 += 1       
    return numeroDe1

def pokerTest(s):
    segmentos = [s[i:i+4] for i in range(0, len(s), 4)]
    count = Counter(segmentos)
    f_i = 0
    for string, quant in count.items():
        f_i += quant*quant
    x = ((16/5000) * f_i) - 5000

    if (x > 1.03) and (x < 57.4):
        return True
    else:
        return False

def pokerQuantityTest(s):
    segmentos = [s[i:i+4] for i in range(0, len(s), 4)]
    count = Counter(segmentos)
    return count

def runsTest(s):
    count = 1
    repeticoes = []
    contador0 = [0, 0, 0, 0, 0, 0]
    contador1 = [0, 0, 0, 0, 0, 0]
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                repeticoes.append([s[i - 1], count])
                count = 1
        repeticoes.append([s[i], count])


    for repet in repeticoes:
        if repet[0] == '0':
            if repet[1] >= 6:
                contador0[5] += 1
            else:
                contador0[repet[1]-1] += 1
        if repet[0] == '1':
            if repet[1] >= 6:
                contador1[5] += 1
            else:
                contador1[repet[1]-1] += 1

    is_0_true = False
    is_1_true = False
    if (contador0[0] > 2267) and (contador0[0] < 2733) and (contador0[1] > 1079) and (contador0[1] < 1421) and (contador0[2] > 502) and (contador0[2] < 748) and (contador0[3] > 223) and (contador0[3] < 402) and (contador0[4] > 90) and (contador0[4] < 223) and (contador0[5] > 90) and (contador0[5] < 223):
        is_0_true = True

    if (contador1[0] > 2267) and (contador1[0] < 2733) and (contador1[1] > 1079) and (contador1[1] < 1421) and (contador1[2] > 502) and (contador1[2] < 748) and (contador1[3] > 223) and (contador1[3] < 402) and (contador1[4] > 90) and (contador1[4] < 223) and (contador1[5] > 90) and (contador1[5] < 223):
        is_1_true = True

    if is_0_true and is_1_true:
        return True
    else:
        return False

def runsQuantityTest(s):
    count = 1
    repeticoes = []
    contador0 = [0, 0, 0, 0, 0, 0]
    contador1 = [0, 0, 0, 0, 0, 0]
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                repeticoes.append([s[i - 1], count])
                count = 1
        repeticoes.append([s[i], count])


    for repet in repeticoes:
        if repet[0] == '0':
            if repet[1] >= 6:
                contador0[5] += 1
            else:
                contador0[repet[1]-1] += 1
        if repet[0] == '1':
            if repet[1] >= 6:
                contador1[5] += 1
            else:
                contador1[repet[1]-1] += 1
    print('Quantidade de cada sequencia do Run test para zeros: ' + str(contador0))
    print('\nQuantidade de cada sequencia do Run test para uns: ' + str(contador1))

def longRun(s):
    count = 1
    
    if len(s) > 1:
        for i in range(1, len(s)):
            if s[i - 1] == s[i]:
                count += 1
            else:
                if count >= 34:
                    return False
                count = 1
    return True



def convertHexBinary(t):
    r = ''
    for char in t:
        r += "{0:04b}".format(int(char, 16))
    return r


def main():
    keys = open('Chaves de Criptografia 2021.S2.txt', 'r')
    keys_binarias = []
    keys_filtradas = []

    for key in keys:
        temp = key[1:]
        temp = temp[:-2]
        a = len(temp)
        keys_filtradas.append(temp)
        keys_binarias.append(convertHexBinary(temp))

    nBin = 1
    for binario in keys_binarias:
        monobit = monobitTest(binario)
        quantityMonobit = monobitQuantityTest(binario)
        quantityPoker = pokerQuantityTest(binario)
        poker = pokerTest(binario)
        runs = runsTest(binario)
        long = longRun(binario)
        print('\n ')
        print('binária: ' + str(nBin))
        
        if monobit and poker and runs and long:
            print("aprovado")
        else:
            print("reprovado! Monobit: " + str(monobit) + ". Poker: " + str(poker) + ". Runs: " + str(runs) + ". Long: " + str(long))
        nBin += 1
        print('quantidade Monobit: ' + str(quantityMonobit))    
        print('valor calculado no pokerTest e quantidade de cada nible ' + str(quantityPoker)) 
        runsQuantityTest(binario)

main()