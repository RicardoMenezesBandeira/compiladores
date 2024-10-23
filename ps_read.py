import sys, re
import ps_lex as ps
dicionario = {}
"""arquivo ={
    linha1 :[dajsldjlkas,dfssdafs,sdmfsad]
}"""
tolkenizada = []
def abre(caminho):    
       # Abrir o arquivo e ler o conteúdo
    with open(caminho, "r") as arq:
        conteudo = arq.read()  # Ler o conteúdo do arquivo como uma string
    ps.tolkenizando(conteudo)  # Passar o conteúdo lido para a função tolkenizando

abre("./exemplo1.sp")