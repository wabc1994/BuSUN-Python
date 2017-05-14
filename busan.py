#encoding:utf-8
import os,sys
import jieba,codecs,math
import jieba.posseg as pseg
names={}  #姓名字典]
relationships={} #关系字典
lineNames=[]  #每段人物关系
#设置字典,加载
jieba.load_userdict('dict.txt')
with codecs.open("busan.txt",'r','utf-8') as f:
    for line in f.readlines():
        poss=pseg.cut(line)  #分
        lineNames.append([])
        for w in poss:   #nr词频，
            if w.flag!="nr" or len(w.word) <2:
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word]=0
                relationships[w.word]={}
            names[w.word]+=1
    for name,times in names.items():
        print name,times

