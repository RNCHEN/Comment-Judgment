import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize

G = nx.Graph()

# add nodes and edges
nodes_with_weights = {
    "happy": 3, "sad": -2, "exciting": 4, "tragic": -3, "funny": 2,
    "angry": -2, "joyful": 3, "scary": -4, "romantic": 3, "thrilling": 4,
    "movie": 5, "love": 2, "action": 4, "drama": -2, "comedy": 3,
    "fantasy": 1, "mystery": -1, "thriller": 2, "horror": -3, "animation": 1,
    "family": 2, "musical": 3, "war": -2, "western": -1, "crime": -3, "romcom": 3,"tragedy": -3,
    "movie": 5  # "movie" node
}
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

# draw
pos = nx.spring_layout(G)

node_weights = [G.nodes[node]['weight'] for node in G.nodes]
### has color
# #
# cmap = plt.cm.viridis  # choose a color
#
# #
# nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_weights, cmap=cmap,
#         vmin=min(node_weights), vmax=max(node_weights), font_size=8, arrows=False)
#
# #
# sm = plt.cm.ScalarMappable(cmap=cmap, norm=plt.Normalize(vmin=min(node_weights), vmax=max(node_weights)))
# sm.set_array([])  #
# plt.colorbar(sm, label='Node Weight')

# 显示图形

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrows=False)
plt.show()

####------- own wordNetwork

comment = "tragedy movie happy"
words = comment.split()
words_to_remove = ["I", "a", "an", "I'm",","]
filtered_words = [word for word in words if word not in words_to_remove]
connections = [(filtered_words[i], filtered_words[i + 1]) for i in range(len(filtered_words) - 1)]
print(connections)
print(filtered_words)
#
H = nx.Graph()
H.edge = connections
# node & edge
for word in filtered_words:
    H.add_node(word)

H.add_edges_from(connections)
print("edges of comments:",connections)
nodes_G = set(G.nodes)
filtered_words_set = set(filtered_words)

common_nodes = filtered_words_set.intersection(nodes_G)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos, with_labels=True, font_weight='bold', node_size=200, node_color='skyblue', font_size=8, arrows=False)

# The second graph should be drawn on the first Graph
nx.draw_networkx_nodes(H, pos, nodelist=common_nodes, node_color='salmon', node_size=200)
nx.draw_networkx_edges(H, pos, edgelist=H.edge, edge_color='red', width=2)

# save
plt.savefig('matchNet.png', dpi=300)
# show
plt.show()