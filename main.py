import pandas as pd
import networkx as nx
from pyvis.network import Network

triples = {
    ("item_001", "crafta", "item_002"),
    ("item_002", "crafta", "item_003"),
    ("item_003", "crafta", "item_004"),
    ("item_002", "crafta", "item_004"),
    ("item_004", "quebra", "item_005"),
    ("item_005", "e_quebrado_em", "item_006"),
    ("item_006", "crafta", "item_007"),
    ("item_003", "crafta", "item_007"),
    ("item_006", "crafta", "item_008"),
}

df = pd.DataFrame(
    triples,
    columns=["head", "relation", "tail"]
)

nodes = {
    "item_001": {
        "nome": "madeira",
        "tipo": "bloco",
        "imagem": "icons/madeira.png"
    },
    "item_002": {
        "nome": "tabua",
        "tipo": "bloco",
        "imagem": "icons/tabua.png"
    },
    "item_003": {
        "nome": "graveto",
        "tipo": "recurso",
        "imagem": "icons/graveto.png"
    },
    "item_004": {
        "nome": "picareta_de_madeira",
        "tipo": "ferramenta",
        "imagem": "icons/picareta_de_madeira.png"
    },
    "item_005": {
        "nome": "pedra",
        "tipo": "bloco",
        "imagem": "icons/pedra.png"
    },
    "item_006": {
        "nome": "pedregulho",
        "tipo": "bloco",
        "imagem": "icons/pedregulho.png"
    },
    "item_007": {
        "nome": "picareta_de_pedra",
        "tipo": "ferramenta",
        "imagem": "icons/picareta_de_pedra.png"
    },
    "item_008": {
        "nome": "fornalha",
        "tipo": "bloco",
        "imagem": "icons/fornalha.png"
    }
}

G = nx.DiGraph()

for node_id, attrs in nodes.items():
    G.add_node(node_id, **attrs)

for head, relation, tail, in triples:
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
        label=attrs["nome"],
        title=f"Tipo: {attrs["tipo"]}",
        shape="image",
        image=attrs["imagem"],
        size=30
    )

for source, target, attrs in G.edges(data=True):
    net.add_edge(
        source,
        target,
        label=attrs["relation"],
    )

net.write_html("minecraft_kg.html")

