from afinn import Afinn
import networkx as nx
import matplotlib.pyplot as plt
import spacy
import re

import glob

folder_path = r'./dataSet/aclImdb_v1/aclImdb/train/7'
file_paths = glob.glob(folder_path + '/*.txt')
save_path = r'MOST3'
texts = []  # storage all text

for file_path in file_paths:
    # print(file_path)
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        texts.append(text)

# Create a graph
G = nx.Graph()
afinn = Afinn()
nlp = spacy.load('en_core_web_sm')
emotionWords = []
node_weights = {}
node_colors = []
# set the MIN and MAX weight
min_weight = -7
max_weight = 7

# 定义颜色映射范围
cmap = plt.cm.get_cmap("Blues")
nmap = plt.cm.get_cmap("Reds")


def clean_text(text):
    # 移除HTML标签
    text = re.sub(r'<[^>]+>', '', text)

    # 移除特殊字符
    text = re.sub(r'[^\w\s]', '', text)

    return text


# ini the vocabulary network
def iniVocaularyNet(text):
    clean_text(text)
    doc = nlp(text)
    lemmatized_words = [token.lemma_ for token in doc]
    emotionWords = []
    prev_word = None
    for word in lemmatized_words:
        score = afinn.score(word)
        if score != 0:
            emotionWords.append(word)

            if word not in node_weights:
                node_weights[word] = score
            weight = score
            if prev_word:
                weight1 = node_weights.get(prev_word, 0)
                weight2 = node_weights.get(word, 0)
                G.add_edge(prev_word, word, weight=weight1 + weight2)
                # remove self loops
                self_loops = list(nx.selfloop_edges(G))
                G.remove_edges_from(self_loops)
            prev_word = word


def setColor():
    for node in G.nodes:
        # get the weight of node
        weight = node_weights.get(node, 0)
        # set the color
        if weight > 0:
            color = cmap((max_weight - weight) / (max_weight - min_weight))
        else:
            color = nmap((weight - min_weight) / (max_weight - min_weight))
        node_colors.append(color)


def getAttribute(G):
    # print("nodes:", G.nodes)
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    density = nx.density(G)
    avg_clustering_coefficient = nx.average_clustering(G)
    num_connected_components = nx.number_connected_components(G)
    giant_component = max(nx.connected_components(G), key=len)
    G_giant = G.subgraph(giant_component).copy()
    average_degree = sum(dict(G_giant.degree()).values()) / num_nodes
    diameter = nx.diameter(G_giant)
    avg_shortest_path_length = nx.average_shortest_path_length(G_giant)
    print(f"Number of nodes: {num_nodes}")
    print(f"Number of edges: {num_edges}")
    print(f"Average degree: {average_degree}")
    print(f"Density: {density}")
    print(f"Number of connected components: {num_connected_components}")
    print(f"Diameter of Giant Component: {diameter}")
    print(f"Average Shortest Path Length of Giant Component: {avg_shortest_path_length}")
    print(f"Average Clustering Coefficient: {avg_clustering_coefficient}")


for text in texts:
    iniVocaularyNet(text)

setColor()
getAttribute(G)
###  plot
pos = nx.spring_layout(G)
file_path = 'neg.txt'  # Replace with your desired file path
nx.write_adjlist(G, file_path)
nx.draw_networkx(G, pos, node_color=node_colors,
                 with_labels=False,
                 node_size=50,
                 edge_color='gray',
                 alpha=1,
                 width=0.1)

plt.figure(figsize=(80, 80), dpi=500)
# plt.savefig('./photo/dataSetG.png', dpi=300)
plt.show()
