import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# caculate the degree and draw some picture about the network

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
# cumulative distribution
degrees = [G.degree(n) for n in G.nodes()]
degree_count = np.bincount(degrees)
# this is the cumulative distribution
cumulative = np.cumsum(degree_count)
plt.loglog(range(len(cumulative)), cumulative, marker='o')
plt.title("Cumulative Degree Distribution (Log-Log Scale)")
plt.xlabel("Degree")
plt.ylabel("Cumulative Frequency")
plt.grid(True)
plt.show()

## CCDF complementary cumulative distribution function

degrees = [G.degree(n) for n in G.nodes()]
max_degree = max(degrees)


degree_count = np.bincount(degrees)
degree_count_normalized = degree_count / sum(degree_count)


cumulative = np.cumsum(degree_count_normalized)

# CCDF
ccdf = 1 - cumulative
plt.xlim(1, 1000)  # range from
plt.xticks([1, 10, 100,200,300,400,500,600,650,700,800,900,1000])
plt.loglog(range(len(ccdf)), ccdf, marker='o')
plt.title("Complementary Cumulative Degree Distribution (Log-Log Scale)")
plt.xlabel("Degree (log scale)")
plt.ylabel("CCDF (log scale)")
plt.show()