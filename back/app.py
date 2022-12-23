# -*- coding: utf-8 -*-
"""
@Time   :   2022-12-19
@File   :   macbert_demo.py
"""
import argparse
import sys
from pycorrector.macbert.macbert_corrector import MacBertCorrector
from pycorrector import config
from flask import Flask, jsonify, request
from flask_cors import CORS
from macbert_demo import correct
sys.path.append('../..')


app = Flask(__name__)    #  通过Flask方法注册app，以后所有的route都是app开头
#CORS(app)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})  #  跨域访问时使用，不跨域可将本行代码去掉
'''
def correct(content):
    
    ini_content=content
    parser = argparse.ArgumentParser()

    # Required parameters
    parser.add_argument("--macbert_model_dir", default=config.macbert_model_dir,
                        type=str,
                        help="MacBert pre-trained model dir")
    print("yes")
    args = parser.parse_known_args()
    print(args)
    print("no")

    nlp = MacBertCorrector(args.macbert_model_dir).macbert_correct

    # Preprocessing
    sentence_lst = []
    for k in range(len(content)):  # 切分语料
        if k < len(content)-1 and content[k] in ["。", "；", "：", "？", "！", "……", "——", ","]:  # 使用标点符号
            sentence_lst.append(content[:k+1])
            content = content[k+1:]

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
    change=[]
    for i in correct_ids:
        change_i=[]
        change_i.append(ini_content[i])
        change_i.append(correct_content[i])
        change_i.append(i)
        change_i.append(i+1)
        change.append(change_i)
    return correct_content, change  #修改后的句子，变化的位置
'''

@app.route('/', methods=['GET', 'POST']) # 提供接口，获取前端页面的提交的表单参数，获得结果，并以Json格式返回给前端页面
def submit():
    response_object = {'status': 'success'}

    if request.method == 'POST':#以POST方式发送
        post_data = request.get_json()
        print(post_data)
        sentence = post_data.get('sentence')#获取的段落（一共10个字）
        print(sentence)
        correct_content, change=correct(sentence)
        print(correct_content)
        print(change)
        #context=sentence[:-3]+"结"+sentence[-2:-1]+"果"        #返回的结果，将最后1位替换为“果”
        #change=[(sentence[-3],"结",7,8),(sentence[-1],"果",9,10)]#有修改的列表
        response_object['context']=correct_content
        response_object['change']=change
    else:#未以POST方式发送则返回错误
        response_object['message'] = 'method is error'

    return jsonify(response_object)





if __name__ == '__main__':

    app.run()
    print(correct("经本院审理查明：2014年4月20日，被告以生意资金周转为由向原告借款9万园"))
