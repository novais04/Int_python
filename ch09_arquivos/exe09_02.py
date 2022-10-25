#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:02:20 2022

@author: anselmo

Exercício 09-02: Imprimia as linhas de um arquivo. O nome do arquivo, 
a primeira e última linha a imprimir serão passadas na linha de comando

"""

import sys

if len(sys.argv) != 4:
    print("\nUso: exe09-02.py nome_do_arquivo início fim\n\n")
else:
    nome = sys.argv[1]
    inicio = int(sys.argv[2])
    fim = int(sys.argv[3])
    arquivo = open(nome, "r")
    for linha in arquivo.readlines()[inicio-1:fim]:
        # Como a linha termina com ENTER,
        # retiramos o último caractere antes de imprimir
        print(linha[:-1])
    arquivo.close()