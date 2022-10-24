#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 17:50:30 2022

@author: anselmo

Listagem 9.3 - Impress'ão de paramêtros passados na linha de comando
"""

import sys

print("Número de parâmetros: %d" % len(sys.argv))
for n,p in enumerate(sys.argv):
    print(f"Parâmetro {n} = {p}")
    
