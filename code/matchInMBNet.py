from afinn import Afinn
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

networkx_savepath = 'neg.txt'
testPath = r'./dataSet/aclImdb_v1/aclImdb/test/pos/1_10.txt'

G = nx.read_adjlist(networkx_savepath)
partition = community_louvain.best_partition(G)

texts = []  # storage all text
with open(testPath, 'r', encoding='utf-8') as file:
    text = file.read()
    texts.append(text)
clean_text(text) # clean text
doc = nlp(text)
lemmatized_words = [token.lemma_ for token in doc]
# each community score
score = {community_id: 0 for community_id in set(partition.values())}
Total = 0
for word in lemmatized_words:
    for node, community_id in partition.items():
        if word == node:
            score[community_id] += 1
            Total += 1

print(score)
print(Total)
# # partition = community_louvain.best_partition(G)

# #     draw
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
