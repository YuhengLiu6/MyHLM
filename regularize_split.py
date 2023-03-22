import re
import numpy as np
import jieba
import os
from bs4 import BeautifulSoup


def regularize_data(file_path):
    # print('Reading raw data', chap_id, '...')
    # read raw text
    # file_path = './data/chap%03d.html'%chap_id
    with open(file_path, 'r', encoding='utf-8') as f:
        raw_text = f.read()
    soup = BeautifulSoup(raw_text, 'html.parser')
    text = soup.get_text()
    pattern = re.compile(r'[\u4e00-\u9fa5]+')
    result = ''.join(re.findall(pattern, text))

    return result

def split_data(text):
    print('Splitting data...')
    # split text into words
    words = jieba.cut(text, cut_all=False)
    # words = jieba.lcut((line.strip()) for line in text)
    words = [word for word in words if word != ' ']
    return words

def is_all_chinese_chars(s):
    return all('\u4e00' <= c <= '\u9fa5' for c in s)

def write_output(text_list, num):
    print('Writing output...')
    word_num = len(text_list)

    target_folder = './cocked_words'
    os.makedirs(target_folder, exist_ok=True)
    file_path = os.path.join(target_folder, 'block_words_%02d.txt'%num)

    with open(file_path, 'w', encoding='utf-8') as f:
        for word in text_list:
            f.write(word)
            f.write(' ')
        # f.write(str(word_num))






# #测试拆分方法的正确性
# if __name__ == '__main__':
#     # print(regularize_data(0))
#     # print(split_data(regularize_data(0)))
#     write_output(split_data(regularize_data(0)), 0)
#     with open('./data/chap000.html', 'r', encoding='utf-8') as f:
#         raw_text = f.read()
#     raw_text2 = split_data(raw_text)
#     text = [word for word in raw_text2 if is_all_chinese_chars(word)]
#     write_output(text, 1)
