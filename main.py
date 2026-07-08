import pandas as pd
import networkx as nx
from pyvis.network import Network
import funcoes

triples = {
    ("madeira", "crafta", "tabua"),
    ("tabua", "crafta", "graveto"),
    ("graveto", "crafta", "picareta_de_madeira"),
    ("tabua", "crafta", "picareta_de_madeira"),
    ("picareta_de_madeira", "quebra", "pedra"),
    ("pedra", "e_quebrado_em", "pedregulho"),
    ("pedregulho", "crafta", "picareta_de_pedra"),
    ("graveto", "crafta", "picareta_de_pedra"),
    ("pedregulho", "crafta", "fornalha"),
    ("ovelha", "dropa", "la"),
    ("ovelha", "dropa", "carne_de_ovelha"),
    ("carne_de_ovelha", "cozinha_em", "carne_de_ovelha_cozida"),
    ("la", "crafta", "cama"),
    ("tabua", "crafta", "cama"),
    ("vaca", "dropa", "couro"),
    ("vaca", "dropa", "bife_cru"),
    ("bife_cru", "cozinha_em", "file"),
    ("couro", "crafta", "capacete_de_couro"),
    ("couro", "crafta", "peitoral_de_couro"),
    ("couro", "crafta", "calca_de_couro"),
    ("couro", "crafta", "bota_de_couro"),
    ("minerio_de_carvao", "e_quebrado_em", "carvao"),
    ("carvao", "crafta", "tocha"),
    ("graveto", "crafta", "tocha"),
    ("carvao", "e_usado_em", "fornalha"),
    ("picareta_de_pedra", "quebra", "minerio_de_ferro"),
    ("picareta_de_madeira", "quebra", "minerio_de_carvao"),
    ("picareta_de_pedra", "quebra", "minerio_de_carvao"),
    ("minerio_de_ferro", "e_quebrado_em", "ferro_bruto"),
    ("ferro_bruto", "e_derretido_em", "barra_de_ferro"),
    ("picareta_de_pedra", "quebra", "pedra"),
    ("zumbi", "dropa", "carne_podre"),
    ("aranha", "dropa", "olho_de_aranha"),
    ("aranha", "dropa", "linha"),
    ("linha", "crafta", "vara_de_pesca"),
    ("graveto", "crafta", "vara_de_pesca"),
    ("areia", "e_derretido_em", "vidro"),
    ("vidro", "crafta", "vidraca"),
    ("graveto", "crafta", "picareta_de_ferro"),
    ("barra_de_ferro", "crafta", "picareta_de_ferro"),
    ("barra_de_ferro", "crafta", "capacete_de_ferro"),
    ("barra_de_ferro", "crafta", "peitoral_de_ferro"),
    ("barra_de_ferro", "crafta", "calca_de_ferro"),
    ("barra_de_ferro", "crafta", "bota_de_ferro"),
    ("picareta_de_ferro", "quebra", "pedra"),
    ("picareta_de_ferro", "quebra", "minerio_de_carvao"),
    ("picareta_de_ferro", "quebra", "minerio_de_ferro"),
    ("picareta_de_ferro", "quebra", "minerio_de_diamante"),
    ("minerio_de_diamante", "e_quebrado_em", "diamante"),
    ("tabua", "crafta", "pa_de_madeira"),
    ("tabua", "crafta", "machado_de_madeira"),
    ("tabua", "crafta", "enxada_de_madeira"),
    ("graveto", "crafta", "pa_de_madeira"),
    ("graveto", "crafta", "enxada_de_madeira"),
    ("graveto", "crafta", "machado_de_madeira"),
    ("pedregulho", "crafta", "espada_de_pedra"),
    ("pedregulho", "crafta", "pa_de_pedra"),
    ("pedregulho", "crafta", "enxada_de_pedra"),
    ("pedregulho", "crafta", "machado_de_pedra"),
    ("graveto", "crafta", "espada_de_pedra"),
    ("graveto", "crafta", "pa_de_pedra"),
    ("graveto", "crafta", "enxada_de_pedra"),
    ("graveto", "crafta", "machado_de_pedra"),
    ("barra_de_ferro", "crafta", "espada_de_ferro"),
    ("barra_de_ferro", "crafta", "pa_de_ferro"),
    ("barra_de_ferro", "crafta", "enxada_de_ferro"),
    ("barra_de_ferro", "crafta", "machado_de_ferro"),
    ("graveto", "crafta", "espada_de_ferro"),
    ("graveto", "crafta", "pa_de_ferro"),
    ("graveto", "crafta", "enxada_de_ferro"),
    ("graveto", "crafta", "machado_de_ferro"),
    ("galinha", "dropa", "frango_cru"),
    ("frango_cru", "cozinha_em", "frango_assado"),
    ("galinha", "dropa", "pena"),
    ("pena", "crafta", "flecha"),
    ("graveto", "crafta", "flecha"),
    ("galinha", "dropa", "ovo"),
    ("flecha", "e_usado_em", "arco"),
    ("graveto", "crafta", "arco"),
    ("linha", "crafta", "arco"),
    ("esqueleto", "dropa", "arco"),
    ("esqueleto", "dropa", "osso"),
    ("osso", "domestica", "lobo"),
    ("creeper", "dropa", "polvora"),
    ("porco", "dropa", "costela_de_porco_crua"),
    ("costela_de_porco_crua", "cozinha_em", "costela_de_porco_assada")
}

df = pd.DataFrame(
    triples,
    columns=["head", "relation", "tail"]
)

nodes = {
    "madeira": {
        "tipo": "bloco",
        "imagem": "icons/madeira.png"
    },
    "tabua": {
        "tipo": "bloco",
        "imagem": "icons/tabua.png"
    },
    "graveto": {
        "tipo": "recurso",
        "imagem": "icons/graveto.png"
    },
    "picareta_de_madeira": {
        "tipo": "ferramenta",
        "imagem": "icons/picareta_de_madeira.png"
    },
    "pedra": {
        "tipo": "bloco",
        "imagem": "icons/pedra.png"
    },
    "pedregulho": {
        "tipo": "bloco",
        "imagem": "icons/pedregulho.png"
    },
    "picareta_de_pedra": {
        "tipo": "ferramenta",
        "imagem": "icons/picareta_de_pedra.png"
    },
    "fornalha": {
        "tipo": "bloco",
        "imagem": "icons/fornalha.png"
    },
    "ovelha": {
       "tipo": "criatura",
       "imagem": "icons/ovelha.png"
    },
    "la": {
       "tipo": "bloco",
       "imagem": "icons/la.png"
    },
    "cama": {
       "tipo": "utilidade",
       "imagem": "icons/cama.png"
    },
    "carne_de_ovelha": {
       "tipo": "comida",
       "imagem": "icons/carne_de_ovelha.png"
    },
    "carne_de_ovelha_cozida": {
       "tipo": "comida",
       "imagem": "icons/carne_de_ovelha_cozida.png"
    },
    "vaca": {
        "tipo": "criatura",
        "imagem": "icons/vaca.png"
    },
    "bife_cru": {
        "tipo": "comida",
        "imagem": "icons/bife_cru.png"
    },
    "file": {
        "tipo": "comida",
        "imagem": "icons/file.png"
    },
    "couro": {
        "tipo": "recurso",
        "imagem": "icons/couro.png"
    },
    "capacete_de_couro": {
        "tipo": "armadura",
        "imagem": "icons/capacete_de_couro.png"
    },
    "peitoral_de_couro": {
        "tipo": "armadura",
        "imagem": "icons/peitoral_de_couro.png"
    },
    "calca_de_couro": {
        "tipo": "armadura",
        "imagem": "icons/calca_de_couro.png"
    },
    "bota_de_couro": {
        "tipo": "armadura",
        "imagem": "icons/bota_de_couro.png"
    },
    "minerio_de_carvao":{
        "tipo": "bloco",
        "imagem": "icons/minerio_de_carvao.png"
    },
    "carvao": {
        "tipo": "recurso",
        "imagem": "icons/carvao.png"
    },
    "tocha": {
        "tipo": "utilidade",
        "imagem": "icons/tocha.png"
    },
    "minerio_de_ferro": {
        "tipo": "bloco",
        "imagem": "icons/minerio_de_ferro.png",
    },
    "ferro_bruto": {
        "tipo": "recurso",
        "imagem": "icons/ferro_bruto.png"
    },
    "barra_de_ferro": {
        "tipo": "recurso",
        "imagem": "icons/barra_de_ferro.png"
    },
    "areia": {
        "tipo": "bloco",
        "imagem": "icons/areia.png"
    },
    "vidro": {
        "tipo": "bloco",
        "imagem": "icons/vidro.png"
    },
    "vidraca": {
        "tipo": "bloco",
        "imagem": "icons/vidraca.png"
    },
    "zumbi": {
        "tipo": "criatura",
        "imagem": "icons/zumbi.png"
    },
    "carne_podre": {
        "tipo": "comida",
        "imagem": "icons/carne_podre.png"
    },
    "aranha": {
        "tipo": "criatura",
        "imagem": "icons/aranha.png"
    },
    "linha": {
        "tipo": "recurso",
        "imagem": "icons/linha.png"
    },
    "olho_de_aranha": {
        "tipo": "recurso",
        "imagem": "icons/olho_de_aranha.png"
    },
    "vara_de_pesca": {
        "tipo": "ferramenta",
        "imagem": "icons/vara_de_pesca.png"
    },
    "picareta_de_ferro": {
        "tipo": "ferramenta",
        "imagem": "icons/picareta_de_ferro.png"
    },
    "capacete_de_ferro": {
        "tipo": "armadura",
        "imagem": "icons/capacete_de_ferro.png"
    },
    "peitoral_de_ferro": {
        "tipo": "armadura",
        "imagem": "icons/peitoral_de_ferro.png"
    },
    "calca_de_ferro": {
        "tipo": "armadura",
        "imagem": "icons/calca_de_ferro.png",
    },
    "bota_de_ferro": {
        "tipo": "armadura",
        "imagem": "icons/bota_de_ferro.png"
    },
    "diamante": {
        "tipo": "recurso",
        "imagem": "icons/diamante.png"
    },
    "minerio_de_diamante": {
        "tipo": "bloco",
        "imagem": "icons/minerio_de_diamante.png"
    },
    "espada_de_pedra": {
        "tipo": "ferramenta",
        "imagem": "icons/espada_de_pedra.png"
    },
    "espada_de_ferro": {
        "tipo": "ferramenta",
        "imagem": "icons/espada_de_ferro.png",
    },
    "machado_de_madeira": {
        "tipo": "ferramenta",
        "imagem": "icons/machado_de_madeira.png"
    },
    "machado_de_pedra": {
        "tipo": "ferramenta",
        "imagem": "icons/machado_de_pedra.png"
    },
    "machado_de_ferro": {
        "tipo": "ferramenta",
        "imagem": "icons/machado_de_ferro.png"
    },
    "pa_de_madeira": {
        "tipo": "ferramenta",
        "imagem": "icons/pa_de_madeira.png"
    },
    "pa_de_pedra": {
        "tipo": "ferramenta",
        "imagem": "icons/pa_de_pedra.png"
    },
    "pa_de_ferro": {
        "tipo": "ferramenta",
        "imagem": "icons/pa_de_ferro.png"
    },
    "enxada_de_madeira": {
        "tipo": "ferramenta",
        "imagem": "icons/enxada_de_madeira.png"
    },
    "enxada_de_pedra": {
        "tipo": "ferramenta",
        "imagem": "icons/enxada_de_pedra.png"
    },
    "enxada_de_ferro": {
        "tipo": "ferramenta",
        "imagem": "icons/enxada_de_ferro.png"
    },
    "galinha": {
        "tipo": "criatura",
        "imagem": "icons/galinha.png"
    },
    "frango_cru": {
        "tipo": "comida",
        "imagem": "icons/frango_cru.png"
    },
    "frango_assado": {
        "tipo": "comida",
        "imagem": "icons/frango_assado.png"
    },
    "ovo": {
        "tipo": "recurso",
        "imagem": "icons/ovo.png"
    },
    "pena": {
        "tipo": "recurso",
        "imagem": "icons/pena.png"
    },
    "flecha": {
        "tipo": "recurso",
        "imagem": "icons/flecha.png"
    },
    "arco": {
        "tipo": "ferramenta",
        "imagem": "icons/arco.png"
    },
    "esqueleto": {
        "tipo": "criatura",
        "imagem": "icons/esqueleto.png"
    },
    "osso": {
        "tipo": "recurso",
        "imagem": "icons/osso.png"
    },
    "lobo": {
        "tipo": "criatura",
        "imagem": "icons/lobo.png"
    },
    "creeper": {
        "tipo": "criatura",
        "imagem": "icons/creeper.png"
    },
    "polvora": {
        "tipo": "recurso",
        "imagem": "icons/polvora.png"
    },
    "porco": {
        "tipo": "criatura",
        "imagem": "icons/porco.png"
    },
    "costela_de_porco_crua": {
        "tipo": "comida",
        "imagem": "icons/costela_de_porco_crua.png"
    },
    "costela_de_porco_assada": {
        "tipo": "comida",
        "imagem": "icons/costela_de_porco_assada.png"
    }
}


def salvar_grafo_html(nodes, triples):
    G = nx.DiGraph()

    for node_id, attrs in nodes.items():
        G.add_node(node_id, **attrs)

    for head, relation, tail in triples:
        G.add_edge(
            head,
            tail,
            relation=relation
        )

    net = Network(
        height="750px",
        width="100%",
        directed=True
    )
    net.barnes_hut()

    for node_id, attrs in G.nodes(data=True):
        net.add_node(
            node_id,
            label=node_id,
            title=f"Tipo: {attrs.get('tipo', 'Desconhecido')}",
            shape="image",
            image=attrs.get('imagem', ''),
            size=30
        )

    for source, target, attrs in G.edges(data=True):
        net.add_edge(
            source,
            target,
            label=attrs["relation"],
        )

    net.write_html("minecraft_kg.html")
    print("🔄 Grafo visual atualizado com sucesso em 'minecraft_kg.html'!")


while True:
    funcoes.exibir_menu()
    opcao = input("Escolha o que deseja fazer: ")

    if opcao == "1":
        funcoes.add_node(nodes)
        salvar_grafo_html(nodes, triples)

    elif opcao == "2":
        funcoes.excluir_no(nodes, triples)
        salvar_grafo_html(nodes, triples)

    elif opcao == "3":
        funcoes.add_relacao(triples)
        salvar_grafo_html(nodes, triples)

    elif opcao == "4":
        funcoes.excluir_relacao(triples)
        salvar_grafo_html(nodes, triples)

    elif opcao == "5":
        print("encerrar processo")
        salvar_grafo_html(nodes, triples)
        break

