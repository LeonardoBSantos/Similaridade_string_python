# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 17:28:23 2020

@author: Leonardo
"""


import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de plágio.")
    print("Informe a assinatura típica:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    
    a = 0
    b = 0
    grau_similaridade = []
    soma_tracos = 0
    
    while(a <= len(as_a) - 1):
        ass_a = as_a[a]
        for b in range(len(as_b)):
            soma_tracos = soma_tracos + abs(ass_a[b] - as_b[b])
        a = a + 1
        b = 0
        grau_similaridade.append(soma_tracos / 6)
        soma_tracos = 0
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    k = 0
    r = 0
    t = 0
    x = 0
    p = 0
    o = 0
    y = 0
    i = 0
    j = 0
    g = 0
    soma_tam_palavras = 0
    num_total_palavras = 0
    n_palavras_diff = 0
    n_frases = 0
    n_caracteres = 0
    lista_frases = []
    lista_palavras = []
    assinatura = []
    lista_aux_4 = []
    tam_medio_sentenca = 0
    
    '''transformações do texto '''
    
    lista_sentencas = separa_sentencas(texto)     # Separa as sentenças
    tam_lista_sentencas = len(lista_sentencas)
    
    while (r <= tam_lista_sentencas - 1):
        lista_frases.append(separa_frases(lista_sentencas[r])) # Separa as frases
        r = r + 1
        
    tam_lista_frases = len(lista_frases)
    while (t <= tam_lista_frases - 1):      # Separa Palavras 
        lista_aux = lista_frases[t]
        tam_lista_aux = len(lista_aux)
        while(x <= tam_lista_aux - 1):
            lista_palavras.append(separa_palavras(lista_aux[x]))
            x = x +1
        t = t +1
        x = 0
    
    '''Calculando o tamanho das palavras (nº de caracteres)'''
    
    tam_lista_palavras = len(lista_palavras)
    while (k <= tam_lista_palavras - 1):    # Soma os tamanhos das palavras
        lista_aux_2 = lista_palavras[k]
        tam_lista_aux_2 = len(lista_aux_2)
        while(p <= tam_lista_aux_2 - 1):
            soma_tam_palavras = soma_tam_palavras + len (lista_aux_2[p])
            num_total_palavras = num_total_palavras + 1 
            p = p + 1
        k = k + 1
        p = 0
    assinatura.append (soma_tam_palavras / num_total_palavras)
    
    '''Calculando relação type token'''
    
    while(o <= tam_lista_palavras - 1):
        lista_aux_3 = lista_palavras[o]
        tam_lista_aux_3 = len(lista_aux_3)
        while(y <= tam_lista_aux_3 - 1):
            lista_aux_4.append(lista_aux_3[y])
            y = y + 1
        o = o + 1
        y = 0
    n_palavras_diff = n_palavras_diferentes(lista_aux_4)
    rel_type_token = n_palavras_diff/num_total_palavras
    assinatura.append(rel_type_token)
    
    '''Calculando a razão hapax legomana'''
    
    n_palavras_unic = n_palavras_unicas(lista_aux_4)
    razao_hapax = n_palavras_unic / num_total_palavras
    assinatura.append(razao_hapax)
    
    '''Calculando o tamanho médio da sentença '''
    
    tam_medio_sentenca = (len(texto) - texto.count('.')) / tam_lista_sentencas
    assinatura.append(tam_medio_sentenca)
    
    '''Calculando a complexidade de sentenças'''
    
    while(i <= tam_lista_frases - 1):
        n_frases = n_frases + len(lista_frases[i])
        i = i + 1 
    complexidade_sentencas = n_frases / tam_lista_sentencas
    assinatura.append(complexidade_sentencas)
    
    '''Calculando o tamanho médio de frase'''
    
    while(j <= tam_lista_frases - 1):
        lista_aux_5 = lista_frases[j]
        tam_lista_aux_5 = len(lista_aux_5)
        while (g <= tam_lista_aux_5 - 1):
            n_caracteres = n_caracteres + len(lista_aux_5[g])
            g = g + 1
        j = j + 1
        g = 0
    tam_medio_frases = n_caracteres / n_frases
    assinatura.append(tam_medio_frases)
    return assinatura


   
   
    

def avalia_textos(texto, as_b):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    j = 0
    m = 0
    pos = 0
    menor_valor = 100
    as_a = []
    g_sim = []
    
    l = len(texto)
    while (i <= l-1):
        j = calcula_assinatura(texto[i])
        as_a.append(j)
        i = i + 1 
    g_sim = compara_assinatura(as_a, as_b)
    
    while (m <= (len(g_sim) - 1)):
        if (menor_valor - g_sim[m] > 0):
            menor_valor = g_sim[m]
            pos = m + 1
        m = m + 1
    
    return pos

def main ():
    as_b = le_assinatura()
    texto = le_textos()
    txt_similar = avalia_textos(texto,as_b)
    print("O Autor do texto", txt_similar, "está cometendo plágio")
    
main()