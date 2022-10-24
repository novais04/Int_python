#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:50:30 2022

@author: anselmo

Listagem 9.2 - Abrindo, Lendo e Fechando um arquivo
"""

arquivo = open("numeros.txt", "r")
for linha in arquivo.readlines():
    print(linha)
arquivo.close()
