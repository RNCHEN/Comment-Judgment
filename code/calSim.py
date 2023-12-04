import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import spacy
import re
import community as community_louvain
nlp = spacy.load('en_core_web_sm')
def clean_text(text):
    # remove html
    text = re.sub(r'<[^>]+>', '', text)

    # remove special characters
    text = re.sub(r'[^\w\s]', '', text)

    return text

networkx_savepath = './anaNet/posALL.txt'
G = nx.read_adjlist(networkx_savepath) # read the networkx
partition = community_louvain.best_partition(G) # get the community

client_1 = r'./dataSet/aclImdb_v1/aclImdb/test/pos/9_7.txt'
client_2 = r'./dataSet/aclImdb_v1/aclImdb/test/pos/10_7.txt'

texts = []  # storage all text
texts_2 = []  # storage all text
text_1 = ''
text_2 = ''
with open(client_1, 'r', encoding='utf-8') as file:
    text_1 = file.read()
    texts.append(text_1)
with open(client_2, 'r', encoding='utf-8') as file:
    text_2 = file.read()
    texts.append(text_2)
# deal with customer1
clean_text(text_1)
doc = nlp(text_1)
lemmatized_words = [token.lemma_ for token in doc]
# each community score
score_1 = {community_id: 0 for community_id in set(partition.values())}
Total_1 = 0
for word in lemmatized_words:
    for node, community_id in partition.items():
        if word == node:
            score_1[community_id] += 1
            Total_1 += 1
print(score_1)
print(Total_1)
# deal with customer2
clean_text(text_2)
doc = nlp(text_2)
lemmatized_words = [token.lemma_ for token in doc]
# each community score
score_2 = {community_id: 0 for community_id in set(partition.values())}
Total_2 = 0
for word in lemmatized_words:
    for node, community_id in partition.items():
        if word == node:
            score_2[community_id] += 1
            Total_2 += 1
print(score_2)
print(Total_2)




values = list(score_2.values())
values_array = np.array(values)
mean = np.mean(values_array)
std = np.std(values_array)
normalized_values = (values_array - mean) / std
normalized_dict_1 = dict(zip(score_2.keys(), normalized_values))

print(normalized_dict_1)
values = list(score_1.values())
values_array = np.array(values)
mean = np.mean(values_array)
std = np.std(values_array)
normalized_values = (values_array - mean) / std
normalized_dict_2 = dict(zip(score_1.keys(), normalized_values))

print(normalized_dict_2)

# caculate the different similarity
values_1 = np.array(list(normalized_dict_1.values()))
values_2 = np.array(list(normalized_dict_2.values()))

cosine_similarity = np.dot(values_1, values_2) / (np.linalg.norm(values_1) * np.linalg.norm(values_2))

print("cosine similarity:", cosine_similarity)

manhattan_distance = np.sum(np.abs(values_1 - values_2))
print("manhattan distance:", manhattan_distance)
pearson_correlation = np.corrcoef(values_1, values_2)[0, 1]
print("pearson correlation:", pearson_correlation)


community_sizes = {}
for node, community_id in partition.items():
    if community_id in community_sizes:
        community_sizes[community_id] += 1
    else:
        community_sizes[community_id] = 1

# Num of communities
print("Num:", len(community_sizes))

# size of each community
print("Each size:", community_sizes)
# # 计算模块度
# modularity = community_louvain.modularity(partition, G)
# print("modularity:", modularity)
#
community_ids = list(set(partition.values()))
colors = [community_ids.index(partition[node]) for node in G.nodes()]

# # visualization
# all
nx.draw(G, node_color=colors, with_labels=False)
plt.show()
##
plt.bar(community_sizes.keys(), community_sizes.values())
plt.title("Size of Communities")
plt.xlabel("Community ID")
plt.ylabel("Number of Nodes")
plt.show()
# #     draw  / it is not necessary
# pos = nx.spring_layout(G)
# nx.draw_networkx(G, pos,
#                  with_labels=True,
#                  node_size=50,
#                  edge_color='gray',
#                  alpha=1,
#                  width=0.1)
#
# plt.figure(figsize=(20, 20), dpi=600)
# # plt.savefig('./photo/dataSetG.png', dpi=300)
# plt.show()
