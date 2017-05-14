[项目来源（实验楼）](https://www.shiyanlou.com/courses/677/labs/2202/document)
# Busan-python Python基于共现提取《釜山行》任务关系
##

一、课程简介



《釜山行》是一部丧尸灾难片，其人物少、关系简单，非常适合我们学习文本处理。这个项目将介绍共现在关系中的提取，使用python编写代码实现对《釜山行》文本的人物关系提取，最终利用Gephi软件对提取的人物关系绘制人物关系图。

######

1.内容简介

###### 2.课程知识点
本课程项目完成过程中将学习：

> 共现网络的基本原理

> Python代码对《釜山行》中人物关系提取的具体实现

> jieba库的基本使用

> Gephi软件的基本使用
```
$ mkdir work && cd work
$ mkdir gephi && cd gephi
$ wget http://labfile.oss.aliyuncs.com/courses/677/gephi-0.9.1-linux.tar.gz                 #下载
$ tar -zxvf gephi-0.9.1-linux.tar.gz
```

-1.*liu*

-2.xiongcheng

-3.cheng






	

######

3.课程来源

##

二、实验原理

##

三、开发准备

###

1.文本就结构

###

2.确定需要的变量
在work文件下创建代码文件busan.py,开始进行python代码的编写。在代码中，我使用字典类型names保存人物，该字典的键为人物名称，值为该人物在全文中出现的次数。我使用字典类型relationships保存人物关系的有向边，该字典的键为有向边的起点，值为一个字典edge，edge的键是有向边的终点，值是有向边的权值，代表两个人物之间联系的紧密程度。lineNames是一个缓存变量，保存对每一段分词得到当前段中出现的人物名称，lineName[i]是一个列表，列表中存储第i段中出现过的人物。
```
# -*-  coding: utf-8 -*- python
import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {}            # 姓名字典
relationships = {}    # 关系字典
lineNames = []        # 每段内人物关系
```


###

3.文本中实体识别
在具体实现过程中，读入《釜山行》剧本的每一行，对其做分词（判断该词的词性是不是“人名”[词性编码：nr]，如果该词的词性不为nr，则认为该词不是人名），提取该行（段）中出现的人物集，存入lineName中。之后对出现的人物，更新他们在names中的出现次数。

```
jieba.load_userdict("dict.txt")        # 加载字典
with codecs.open("busan.txt", "r", "utf8") as f:
    for line in f.readlines():
        poss = pseg.cut(line)        # 分词并返回该词词性
        lineNames.append([])        # 为新读入的一段添加人物名称列表
        for w in poss:
            if w.flag != "nr" or len(w.word) < 2:
                continue            # 当分词长度小于2或该词词性不为nr时认为该词不为人名
            lineNames[-1].append(w.word)        # 为当前段的环境增加一个人物
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1                    # 该人物出现次数加 1
```

###

4.根据识别结果构建网络
对于 lineNames 中每一行，我们为该行中出现的所有人物两两相连。如果两个人物之间尚未有边建立，则将新建的边权值设为 1，否则将已存在的边的权值加 1。这种方法将产生很多的冗余边，这些冗余边将在最后处理。
```
for line in lineNames:                    # 对于每一段
    for name1 in line:                    
        for name2 in line:                # 每段中的任意两个人
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:        # 若两人尚未同时出现则新建项
                relationships[name1][name2]= 1
            else:
                relationships[name1][name2] = relationships[name1][name2]+ 1        # 两人共同出现次数加 1
 ```               

###

5.过滤冗余边并输出结果

###

6.可视化网络
![实验结果：利用可视化工具gephi]({{site.baseurl}}/https://github.com/wabc1994/BuSUN-Python/blob/master/DeepinScreenshot20170514223103.png)
