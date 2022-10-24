#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:02:20 2022

@author: anselmo

Exercício 09-01: Imprima todas as linhas de um arquivo cujo nome é passado 
pela linha de comand

"""

import sys

if len(sys.argv) != 2:
    print("\nUso: exe09-01.py nome_do_arquivo\n\n")
else:
    nome = sys.argv[1]
    arquivo = open(nome, "r")
    for linha in arquivo.readlines():
        print(linha)

arquivo.close()