from afinn import Afinn
import networkx as nx
import matplotlib.pyplot as plt
import spacy
import re
import numpy as np
import glob
networkx_savepath = 'neg1000.txt'
G = nx.read_adjlist(networkx_savepath)

pos = nx.spring_layout(G)
degrees = [G.degree(n) for n in G.nodes()]
# distribution of degrees
plt.hist(degrees, bins=50, edgecolor='black')
plt.title("Degree Distribution")
plt.xlabel("Degree")
plt.ylabel("Frequency")
plt.show()
degrees = [G.degree(n) for n in G.nodes()]
max_degree = max(degrees)

# log - binning
bins = np.logspace(np.log10(1), np.log10(max_degree), num=20)
hist, edges = np.histogram(degrees, bins=bins)
#
bin_centers = (edges[:-1] + edges[1:]) / 2
#
plt.loglog(bin_centers, hist, marker='o', linestyle='none')
#
plt.title("Degree Distribution with Log Binning")
plt.xlabel("Degree (log scale)")
plt.ylabel("Frequency (log scale)")
plt.show()