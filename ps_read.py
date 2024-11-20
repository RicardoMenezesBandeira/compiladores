dicionario = {}
tolkenizada = []
def abre(caminho):    
       # Abrir o arquivo e ler o conteúdo
    try:
        with open(caminho, "r") as arq:
            conteudo = arq.read()  # Ler o conteúdo do arquivo como uma string
            return conteudo
    except:
        print("erro ao abrir o script")

