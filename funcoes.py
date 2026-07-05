
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







