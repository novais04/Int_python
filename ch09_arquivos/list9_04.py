#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:52:11 2022

@author: anselmo

Listagem 9.4 - Garvação de números pares impares em arqeuivos diferentes
"""

impares = open("impares.txt", "w")
pares = open("pares.txt", "w")
for n in range(0,1000):
    if n % 2 == 0:
        pares.write(f"{n}\n")
    else:
        impares.write(f"{n}\n")
impares.close()
pares.close()