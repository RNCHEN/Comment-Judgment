# Similarity based on Networks
Similarity based on Networks for courses18755 
Everything is on the master branch
PPT: https://docs.google.com/presentation/d/1yi-1jC7W8r98PnyQqsRT5xmNQ_1piDoHpBDCMjAw8Lk/edit#slide=id.g2899d455ea1_5_49

Dataset https://www.kaggle.com/datasets

Teammates: 

Jeffrey Chen 2448297223@qq.com

Yudi Chen yudichen@andrew.cmu.edu

Zhonghui Cui zhonghuc@andrew.cmu.edu

# Usage about the folder&file

1. import dataset in folder `dataSet `
2. Build our analysis network and export it to folder `anaNet`
3. `processCode` includes the previous code
4. `proAna.py` draw some pictures about our analysis network 
5. `withModel` creates the analysis network 
6. `calSim` calculates the similarity(results from 0 -1 )of two customer who comment the same movie

# Lib requirement

```
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import spacy
import re
import community as community_louvain
import glob
```

