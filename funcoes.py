
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

def excluir_no(tp,nd):
    elem = input("elemento a ser excluido: ")

    if elem not in nd:
        print("O elemento não consta na base de dados.")
        return
    else:
        del nd[elem]

    tp_excluindo = {
        (s,p,o) for s,p,o in tp
        if s!=elem and  o!=elem
    }
    tp.clear()
    tp.update(tp_excluindo)
    print("o elemento '{elem}' e suas relações foram excluidos da base de dados.".format(elem = elem))

def excluir_relacao(tp):
    elem = input("de que elemento você vai excluir uma relação?: ")
    other = input ("você vai excluir uma relção dele com quem?: ")

    tripla_encontrada = None
    for s,p,o in tp:
        if s == elem and o == other:
            tripla_encontrada = (s, p, o)
            break

    if tripla_encontrada is not None:
        tp.remove(tripla_encontrada)
        print("{Relação foi removida na base de dados}")
    else:
        print("{Nenhuma relação foi removida pois nenhuma relação com o critério estabelecido foi encontrada}")


def consultar(nd,tp):
    elem = input("elemento: ")
    if elem not in nd:
        print("elemento não encontardo na base de dados.")
        return
    else:
        print("> INFORMAÇÕES DO ELEMENTO: <")
        print("tipo: " + nd[elem].get("tipo", "Não informado"))
        print("endereco_de_imagem: " + nd[elem].get("imagem", "Não informado"))
        print("")
        print("> CONEXÕES: <")
        for s,p,o in tp:
            if s == elem or o == elem:
                print(f"  {s} --({p})--> {o}")


def exibir_menu():
    print("Digite 1: para adicionar um novo elemento")
    print("Digite 2: para remover um elemento")
    print("Digite 3: para adicionar uma nova relação")
    print("Digite 4: para remover uma relação")
    print("Digite 5: para encerrar o processo")







