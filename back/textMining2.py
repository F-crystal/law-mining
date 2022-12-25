#计算idf
import jieba
from jieba import analyse
import jieba.analyse as jbany
jbany.set_stop_words('hgdstopwords') # 输入停用词
jbany.set_idf_path('word_tf.txt')#加载自定义词典
word_result = jbany.extract_tags(newstring,topK=2000,withWeight=True)#这里的数量可能需要改


def split_words(words):
    word_list = jieba.cut_for_search(words.lower().strip(),HMM=True)
    word_list = [i for i in word_list if i not in stopwords and i!=' ']
    return word_list

# 统计词频，并返回字典
def make_word_freq(word_list):
    freword = {}
    for i in word_list:
        if str(i) in freword:
            freword[str(i)] += 1
        else:
            freword[str(i)] = 1
    return freword

# 计算tfidf,组成tfidf矩阵
import numpy as np
def make_tfidf(word_list,all_dick,idf_dict):
    length = len(word_list)
    word_list = [word for word in word_list if word in all_dick]
    word_freq = make_word_freq(word_list)
    w_dic = np.zeros(len(all_dick))
    for word in word_list:
        ind = all_dick[word]
        idf = idf_dict[word]
        w_dic[ind] = float(word_freq[word]/length)*float(idf)
    return w_dic

# 按每行读取，每一行按空格切分为一个list，组成2维列表。
def read_file2matrix():
    tf=[]
    for i in range(5102):
        word_list = split_words(data1["A"].iloc[i])
        vec = make_tfidf(word_list,items,word_result)
        tf.append(vec)
    return tf

# 基于numpy的余弦相似性计算
def Cos_Distance(vector1, vector2):
    vec1 = np.array(vector1)
    vec2 = np.array(vector2)
    return float(np.sum(vec1 * vec2)) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

# 计算相似度
def similarity_words(vec, vecs_list):
    Similarity_list = []
    for vec_i in vecs_list:
        Similarity = Cos_Distance(vec, vec_i)
        Similarity_list.append(Similarity)
    return Similarity_list

def read_file(data_jianmo):
    data_al=[]
    for i in range(5102):
        data_al.append(" ".join(jieba.cut(data_jianmo.iloc[i], cut_all=False)))
    return data_al

def main(words, file_path):
    words_list = read_file(file_path)
    vecs_list = read_file2matrix()
    word_list = split_words(words)
    vec = make_tfidf(word_list,items,word_result)
    similarity_lists = similarity_words(vec, vecs_list)
    sorted_res = sorted(enumerate(similarity_lists), key=lambda x: x[1])
    outputs = [[words_list[i[0]],i[1]] for i in sorted_res[-10:]]
    return outputs

words=f"委托代理人蒋水光，湘阴县南湖法律服务所法律工作者。被告夏某1。\n\n原告李某1诉称，2015年3月6日，被告夏某1因欠缺资金，向丰辉借款70000元。因丰辉又欠他70000元，2015年3月23日，他向丰辉追收欠款时，丰辉将被告夏某1所欠其70000元债权转让予他，被告夏某1同意转让并向他出具欠条一张。后被告夏某1经他多次催要，至今尚未归还本金及利息。为维护他的合法权益，特起诉至法院，请求法院依法判决：1、被告夏某1偿还其本金70000元及利息"

file_path = data1["A"]
#readed_path = r"MobilePhoneTitle_tfidf.txt"
outputs = main(words, file_path)
# print(outputs)
for i in outputs[::-1]:
    print(i[0] + '     ' + str(i[1]))