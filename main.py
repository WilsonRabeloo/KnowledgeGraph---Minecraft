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
    }
}

# funcoes.add_node(nodes)

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
        label=node_id,
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

