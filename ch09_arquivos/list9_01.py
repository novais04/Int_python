#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:45:39 2022

@author: anselmo

Liatagem 9.1 - Abrindo, escrevendoe fechando um arquivo

"""

arquivo = open('numeros.txt', "w") #abrindo o arquivo
for linha in range(1,10):
    arquivo.write(f'{linha}\n')  # ecrevendo os números de 0 à 9
    
arquivo.close() # fechando o arquivo



