import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from wordEmbed import get_same_word

def vector_distance_cossim(v1, v2, signed = True):
    c = np.dot(v1, v2)/np.linalg.norm(v1)/np.linalg.norm(v2)
    if not signed:
        return abs(c)
    return c

def vectors_distance_norm(vec1, vec2):
    return np.linalg.norm(np.subtract(vec1, vec2))


def get_distance_matrix(model1, model2, words):
    # get distance matrix
    distance_matrix = np.zeros((len(words), len(words)))
    for i in range(len(words)):
        for j in range(len(words)):
            distance_matrix[i][j] = vector_distance_cossim(model1.wv[words[i]], model2.wv[words[j]])
    return distance_matrix

#calculate the average distance of every word in one model to another model
def get_average_distance(model1, model2, words):
    distance_matrix = get_distance_matrix(model1, model2, words)
    average_distance = np.sum(distance_matrix, axis=0)/len(words)
    return np.mean(average_distance)

def get_heatmap():
    heatmap = np.zeros((12, 12))
    for i in range(12):
        for j in range(i+1,12):
            model1 = Word2Vec.load('./models/w2v_b%02d.model'%(i+1))
            model2 = Word2Vec.load('./models/w2v_b%02d.model'%(j+1))
            words = get_same_word(i,j)
            average_distance = get_average_distance(model1, model2, words)
            print('The average distance between block_%02d and block_%02d is %f'%(i+1,j+1,average_distance))
            heatmap[i][j] = average_distance
            heatmap[j][i] = average_distance
    for i in range(12):
        heatmap[i][i] = 1
    return heatmap

if __name__ == '__main__':

    #提取相同的词，计算平均距离
    print("Calculating the average distance between blocks...")
    heatmap = get_heatmap()
    range_num = range(1,13)
    plt.figure(figsize=(6,6))
    sns.heatmap(heatmap, annot=True, fmt='.2f', cmap='YlGnBu', xticklabels=range_num, yticklabels=range_num)
    plt.show()
