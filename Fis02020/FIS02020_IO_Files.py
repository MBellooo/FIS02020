#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May  8 15:41:28 2025

@author: mar
"""

dir_dados = "/home/mar/Fis02020/dados/" # joga pra essa pasta

#%% 1. EScrevendo em arquivo (modo texto)

file1 = dir_dados + "exemplo.txt"

with open (file1, "w") as arquivo: #cria um texto, w é escrito
    # w cria um arquivo ou substitui oque ta escrito no arquivo anterior
    # a é de append que adciona no que já existe
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    arquivo.write("Terceira linha\n")

#%%2. Lendo Arquivo linha por linha


with open(file1,"r") as arquivo: #r de leitura
    for linha in arquivo:
        print(linha, end='') # esse end corta o espaço
        #outra maneira é print (linha.strip())

#%%3. Lendo todo o conteudo de uma vez


with open (file1,"r") as arquivo:
    conteudo =arquivo.read()
   
print (conteudo)
print (type(conteudo))

#%%4. Acrescentando dados no final do arquivo

with open (file1, "a") as arquivo:
    arquivo.write("Mais uma linha.\n")
    
#%%5. Lendo e escrevendo dados tabulares
# com CSV
import csv

file2 = dir_dados + "stars.csv"
with open (file2, "w", newline="") as arquivo: # ja coloca linhas extras aqui
    escritor = csv.writer(arquivo)
    
    #writer é um escritor usando ow pra escrver uma linha
    
    escritor.writerow(["Id", "DEC", "RA"])
    escritor.writerow(['star1', -30.001, 34.15])
    escritor.writerow(['star2', -29.232, 12.789])
    escritor.writerow(['star3', 40.123, 23.123])
    
#%%
with open (file2, "r") as arquivo:
    leitor =csv.reader(arquivo)
    for linha in leitor:
        print(linha)

#%%6. Lendo dados tabulares...

file3= dir_dados + "Dados2.csv"

with open(file3, "r") as fid:
    leitor =csv.reader(fid)
    matriz =[]
    for linha in leitor:
       # t = int(linha[0])
      # x = float (linha[1])
       # y = float (linha[2])
       row = [float (e) for e in linha]
      # matriz.append ([t,x,y])
       matriz.append (row)
       
print ()  
print(matriz)