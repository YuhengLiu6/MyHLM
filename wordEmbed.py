from gensim.models import Word2Vec
import os
# import w2v_b01.model
#load cocked words
def train_word2vec():
    folder_path = './cocked_words'
    model_path = './models'
    os.makedirs(model_path, exist_ok=True)
    abs_path = os.path.abspath(folder_path)
    for i in range(1,13):
        file_path = os.path.join(abs_path, 'block_words_%02d.txt'%i)
        with open(file_path, 'r', encoding='utf-8') as f:
            text = f.read()
        words = text.split(' ')

        #train word2vec model
        model = Word2Vec([words], vector_size=100, window=5, min_count=5, workers=4)
    
        model.save('./models/w2v_b%02d.model'%i)
        print('model_%02dsaved'%i)
        print(model.wv)


def blocks_word_list():
    all_words =[]
    model_path = os.path.abspath('./models')
    for i in range(1,13):
        block_word = []
        model_name = 'w2v_b%02d.model'%i
        model = Word2Vec.load(os.path.join(model_path, model_name))
        for word in model.wv.index_to_key:
            block_word.append(word)
        all_words.append(block_word)
    return all_words


def get_same_word(i,j):
    allwords = blocks_word_list()
    same_word =[word for word in (set(allwords[i])&set(allwords[j]))]
    # print("The number of same words between block_%02d and block_%02d is %d"%(i+1,j+1,len(same_word)))
    return same_word








# model.wv.key_to_index: 返回一个字典，其中键是单词，值是它们在词汇表中的索引。
# model.wv.index_to_key: 返回一个列表，其中包含所有单词，按照它们在词汇表中的索引顺序排列。
# model.wv.get_vecattr(word, attr): 返回给定单词的词向量属性。
# model.wv.set_vecattr(word, attr, new_val): 设置给定单词的词向量属性为新值。

if __name__ == '__main__':
    train_word2vec()
    # model_01 = Word2Vec.load('./models/w2v_b01.model')
    
    # for word in model_01.wv.index_to_key:
    #     vocab_obj = model_01.wv[word]
    #     print(word)
    # len = wvec.shape[0]
    
    for i in range(12):
        for j in range(i+1,12):
            get_same_word(i,j)

    # for k in range(12):
    #     for i in range(len(allwords[k])):
    #         for j in range(len(allwords[k+1])):
    #             if allwords[0][i] == allwords[1][j]:
    #                 samewords.append(allwords[0][i])
    # print(samewords)
    # print(len(samewords))
    # print(len(allwords))