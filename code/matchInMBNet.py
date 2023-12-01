from afinn import Afinn
import networkx as nx
import matplotlib.pyplot as plt
import spacy
import re

import glob
networkx_savepath = 'neg.txt'
G = nx.read_adjlist(networkx_savepath)

pos = nx.spring_layout(G)
nx.draw_networkx(G, pos,
                 with_labels=False,
                 node_size=50,
                 edge_color='gray',
                 alpha=1,
                 width=0.1)

plt.figure(figsize=(20, 20), dpi=600)
# plt.savefig('./photo/dataSetG.png', dpi=300)
plt.show()
print("Nodes:", G.nodes())
print("Edges:", G.edges())