import networkx as nx
import matplotlib.pyplot as plt

comment = "I watched a tragedy movie last week, I'm happy"
words = comment.split()
words_to_remove = ["I", "a", "an", "I'm",","]
filtered_words = [word for word in words if word not in words_to_remove]
connections = [(filtered_words[i], filtered_words[i + 1]) for i in range(len(filtered_words) - 1)]
print(connections)
print(filtered_words)
# directed graph
G = nx.Graph()

# node & edge
for word in filtered_words:
    G.add_node(word)

G.add_edges_from(connections)

# draw
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_size=8, arrowsize=10)

# show
plt.savefig('./photo/commentNet.png', dpi=300)
plt.show()