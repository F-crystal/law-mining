# law-mining

小组作业，基于现有模型开发的法律文书辅助系统，包括文本纠错、相似案例判别 <br>
语言环境：python3<br>
使用的库：罗列在[requirements.txt](https://github.com/F-crystal/law-mining/blob/7237902458d335e5e0fa2f9a9f00b41ace8cf856/requirements.txt)中，需要可以自行下载<br>
```
pip install -r requirements.txt
```

## 文本纠错
### 基准模型
基于[macbert](https://github.com/shibing624/pycorrector/blob/master/pycorrector/macbert)进行数据训练和微调<br>

### 数据集
所使用的数据集来源如下：<br>

| 数据集 | 语料 | 下载链接 | 数据所占存储空间 | 格式 |
| :------- | :--------- | :---------: | :---------: | :---------: |
| **`原始ECSpell领域数据集`** | ECSpell law| [github](https://github.com/Aopolin-Lv/ECSpell)| 455k | txt |
| **`原始CAIL2019-SCM数据集`** | CAIL2019-SCM | [下载链接](https://cail.oss-cn-qingdao.aliyuncs.com/cail2019/CAIL2019-SCM.zip)| 44.7k | json |
| **`原始cail2022文书校对第一阶段数据集`** | cail2022| 目前未提供官方链接 | 992k | json |
| **`中文纠错比赛数据汇总`** | Chinese Text Correction（CTC） | [中文纠错汇总数据集（天池）](https://tianchi.aliyun.com/dataset/138195) | - | - |

### 数据增强
使用了[jionlp](https://github.com/dongrixinyu/JioNLP)和[eda](https://github.com/zhanlaoban/EDA_NLP_for_Chinese)两种方式

## 参考
> Xu, M. Pycorrector: Text error correction tool (Version 0.4.2) [Computer software]. https://github.com/shibing624/pycorrector
> Chengyu Cui, JioNLP, (2020), GitHub repository, https://github.com/dongrixinyu/JioNLP
```
@inproceedings{zhang-etal-2022-mucgec,
    title = "{M}u{CGEC}: a Multi-Reference Multi-Source Evaluation Dataset for {C}hinese Grammatical Error Correction",
    author = "Zhang, Yue  and
      Li, Zhenghua  and
      Bao, Zuyi  and
      Li, Jiacheng  and
      Zhang, Bo  and
      Li, Chen  and
      Huang, Fei  and
      Zhang, Min",
    booktitle = "Proceedings of the 2022 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies",
    month = jul,
    year = "2022",
    address = "Seattle, United States",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2022.naacl-main.227",
    pages = "3118--3130",
    }
  ```
