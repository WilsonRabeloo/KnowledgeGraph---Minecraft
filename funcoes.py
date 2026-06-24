
def add_node(nd):
    nome = input("nome: ")
    tipo = input("tipo: ")
    imagem = input("endereço da imagem: ")
    nd[nome] = {"tipo": tipo, "imagem": imagem}


def add_relacao(tp):
    elem = input("elemento: ")
    elem2 = input("segundo elemento: ")
    rel = input("relacao entre eles: ")
    tp.add((elem,rel,elem2))
