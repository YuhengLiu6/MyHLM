from bs4 import BeautifulSoup
import os
import regularize_split as rs

def combine_block(block_num):
    print('Combining block', block_num, '...')
    dir = 'data/block%02d'%block_num
    block_words =[]
    for i in range(10):
        # name_fix = str(block_num-1)
        html_file_path = os.path.abspath(os.path.join(dir, 'chap%02d%d.html'%(block_num-1, i)))
        # print('chap%02d%d.html'%(block_num-1, i))
        chap_words = rs.split_data(rs.regularize_data(html_file_path))
        block_words.extend(chap_words)
    rs.write_output(block_words, block_num)
    

    

if __name__ == '__main__':
    for i in range(1, 13):
        combine_block(i)