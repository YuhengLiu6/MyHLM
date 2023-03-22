from combine import combine_block
from wordEmbed import train_word2vec
from calculation import get_heatmap
import matplotlib.pyplot as plt
import seaborn as sns



for i in range(1, 13):
        combine_block(i)
#train the model for each block
train_word2vec()
#calculate the average distance between each block
print("Calculating the average distance between blocks...")
heatmap = get_heatmap()
range_num = range(1,13)
plt.figure(figsize=(6,6))
sns.heatmap(heatmap, annot=True, fmt='.2f', cmap='YlGnBu', xticklabels=range_num, yticklabels=range_num)
plt.show()

