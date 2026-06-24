
def add_node(nd):
    nome = input("nome: ")
    tipo = input("tipo: ")
    imagem = input("endereço da imagem: ")
    nd[nome] = {"tipo": [tipo], "imagem": [imagem]}
