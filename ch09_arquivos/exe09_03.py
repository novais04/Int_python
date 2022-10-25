#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 22:05:01 2022

@author: anselmo

Exercício 09-03: Escreva um programa que junte dois arquivos de entrada 
em um único arquivo de saída, preservando a ordem numérica
"""

# Assume que pares e ímpares contém apenas números inteiros
# Assume que os valores em cada arquivo estão ordenados
# Os valores não precisam ser sequenciais
# Tolera linhas em branco
# Pares e ímpares podem ter número de linhas diferentes

def le_numero():
    while true:
        numero =  arquivo.readlines()
        if numero == ":
            return None
        if numero.strip() != "":
            return int(numero)

def escreve_numero(arquivo,n):
    arquivo.write(f"{n}\n")
    

    
    
        
        