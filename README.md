# law-mining

小组作业，基于现有模型开发的法律文书辅助系统，包括文本纠错、相似案例判别 <br>
语言环境：python3<br>
使用的库：罗列在[requirements.txt](https://github.com/F-crystal/law-mining/blob/7237902458d335e5e0fa2f9a9f00b41ace8cf856/requirements.txt)中，需要可以自行下载<br>
```
pip install -r requirements.txt
```

## 文本纠错
示例：[macbert_demo](https://github.com/F-crystal/law-mining/blob/b57a81c8814dc3efe410b4dc3216f3f679500406/back/macbert_demo.py)
### 基准模型
基于[macbert](https://github.com/shibing624/pycorrector/blob/master/pycorrector/macbert)进行数据训练和微调，主要支持中文音似、形似、语法错误纠正<br>

### 数据集
所使用的数据集来源如下：<br>

| 数据集 | 语料 | 下载链接 | 数据所占存储空间 | 格式 |
| :------- | :---------: | :---------: | :---------: | :---------: |
| **`原始ECSpell领域数据集`** | ECSpell law| [github](https://github.com/Aopolin-Lv/ECSpell)| 455k | txt |
| **`原始CAIL2019-SCM数据集`** | CAIL2019-SCM | [下载链接](https://cail.oss-cn-qingdao.aliyuncs.com/cail2019/CAIL2019-SCM.zip)| 44.7k | json |
| **`原始cail2022文书校对第一阶段数据集`** | cail2022| 目前未提供官方链接 | 992k | json |
| **`中文纠错比赛数据汇总`** | Chinese Text Correction（CTC） | [中文纠错汇总数据集（天池）](https://tianchi.aliyun.com/dataset/138195) | - | - |

### 数据增强
使用了[jionlp](https://github.com/dongrixinyu/JioNLP)中同音词替换和语序置换两种方式

### 模型配置
已有的配置文件存放在[百度网盘(密码：g8rg)](https://pan.baidu.com/s/1S8MFMfRFeIGyFdT32l1YeQ)中，共有两个配置，可根据需要自行下载：<br>

| 名字 | 语料来源 | 语料大小 |
| :------- | :---------: | :---------: | 
| **fine-tuning1** | ECSpell-law+cail2022| 6k+ |
| **fine-tuning2** | CAIL2019-SCM+ECSpell-law+cail2022 | 290k+ |

每个配置文件组成：
```
fine-tuning
    ├── config.json
    ├── added_tokens.json
    ├── pytorch_model.bin
    ├── special_tokens_map.json
    ├── tokenizer_config.json
    └── vocab.txt
```
下载后，将文件夹中的6个配置文件放入`~/.pycorrector/datasets/macbert_models/chinese_finetuned_correction`目录下，即可快速调用

## 参考
> Xu, M. Pycorrector: Text error correction tool (Version 0.4.2) [Computer software]. https://github.com/shibing624/pycorrector<br>
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
