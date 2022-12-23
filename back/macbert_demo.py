# -*- coding: utf-8 -*-
"""
@Time   :   2022-12-19
@File   :   macbert_demo.py
"""
import argparse
import sys
from pycorrector.macbert.macbert_corrector import MacBertCorrector
from pycorrector import config

sys.path.append('../..')


def correct(content):
    ini_content = content
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--macbert_model_dir", default=config.macbert_model_dir,
                        type=str,
                        help="MacBert pre-trained model dir")
    print("yes")
    args = parser.parse_args()
    print(args)
    print("no")

    nlp = MacBertCorrector(args.macbert_model_dir).macbert_correct

    # Preprocessing
    sentence_lst = []
    for k in range(len(content)):  # 切分语料
        if k < len(content) - 1 and content[k] in ["。", "；", "：", "？", "！", "……", "——", ","]:  # 使用标点符号
            sentence_lst.append(content[:k + 1])
            content = content[k + 1:]

    sentence_lst.append(content)  # 将最后的语料压入

    # Correcting
    result_lst = [nlp(s) for s in sentence_lst]  # 获得结果列表，形如(correct_text, [(wrong_word, right_word, id, id+1)]
    # Postprocessing
    correct_lst = []
    correct_ids = []
    offset = 0  # 初始化位移量
    for i, lst in result_lst:
        correct_lst.append(i)
        if len(lst) != 0:  # 如果有错误
            for k in range(len(lst)):
                idx = lst[k][2] + offset  # 位置= 在本句话中的位置 + 位移量（即之前的句子的长度）
                correct_ids.append(idx)  # 记录下错误发生的位置

        offset += len(i)  # 更新位移值

    correct_content = "".join(correct_lst)
    change = []
    for i in correct_ids:
        change_i = []
        change_i.append(ini_content[i])
        change_i.append(correct_content[i])
        change_i.append(i)
        change_i.append(i + 1)
        change.append(change_i)
    return correct_content, change  # 修改后的句子，变化的位置


if __name__ == "__main__":
    test1 = "经本院审理查明：2014年4月20日，被告以生意资金周转为由向原告借款9万园，"
    test_result1 = correct(test1)
    print(test_result1)
    correct_test1 = test_result1[0]
    test_ids1 = test_result1[1]
    for i in test_ids1:
        print(test1[i])
        print(correct_test1[i])

    test2 = "事实与理由：原、被告系朋系关友，2016年11月29日、2017年12月11日，被告分三次向原告借款共计125000元，约定利息月息1.5分。"
    test_result2 = correct(test2)
    print(test_result2)
    correct_test2 = test_result2[0]
    test_ids2 = test_result2[1]
    for i in test_ids2:
        print(test2[i])
        print(correct_test2[i])