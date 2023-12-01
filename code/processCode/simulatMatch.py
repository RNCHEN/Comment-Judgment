import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

# create an undirected G
G = nx.Graph()

# nodes and edges
nodes_with_weights = {
    "happy": 3, "sad": -2, "exciting": 4, "tragic": -3, "funny": 2,
    "angry": -2, "joyful": 3, "scary": -4, "romantic": 3, "thrilling": 4,
    "movie": 5, "love": 2, "action": 4, "drama": -2, "comedy": 3,
    "fantasy": 1, "mystery": -1, "thriller": 2, "horror": -3, "animation": 1,
    "family": 2, "musical": 3, "war": -2, "western": -1, "crime": -3, "romcom": 3,"tragedy": -3,
    "movie": 5
}
# 添加边
edges = [
    ("happy", "exciting"), ("sad", "tragic"), ("funny", "exciting"),
    ("angry", "scary"), ("joyful", "romantic"), ("romantic", "thrilling"),
    ("thrilling", "exciting"), ("scary", "thrilling"), ("angry", "sad"),
    ("sad", "funny"), ("funny", "happy"), ("joyful", "happy"), ("angry", "sad"),
    ("happy", "movie"), ("sad", "movie"), ("exciting", "movie"),("tragedy", "movie"),
    ("funny", "movie"), ("thrilling", "movie"), ("romantic", "movie"),
    ("love", "romantic"), ("action", "thrilling"), ("drama", "sad"),
    ("comedy", "funny"), ("fantasy", "romantic"), ("mystery", "thriller"),
    ("thriller", "horror"), ("horror", "thrilling"), ("animation", "fantasy"),
    ("family", "happy"), ("musical", "romantic"), ("war", "drama"),
    ("western", "thrilling"), ("crime", "thriller"), ("romcom", "romantic")
]
for node, weight in nodes_with_weights.items():
    G.add_node(node, weight=weight)
G.add_edges_from(edges)

#
pos = nx.spring_layout(G)  #
## set movie node
pos["movie"] = [0, 0]

node_weights = [G.nodes[node]['weight'] for node in G.nodes]
## has color

cmap = plt.cm.viridis

# 绘制节点时使用权重和颜色映射
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=500, node_color=node_weights, cmap=cmap,
        vmin=min(node_weights), vmax=max(node_weights), font_size=8, arrows=False)
## set Movie node
nx.draw_networkx_nodes(G, pos, nodelist=["movie"], node_size=700, node_color='red')
# add color slide
sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(node_weights), vmax=max(node_weights)))
sm.set_array([])
plt.colorbar(sm, label='Node Weight')

# draw
## with no color
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrows=False)
plt.savefig('wordNet.png', dpi=300)
plt.show()
