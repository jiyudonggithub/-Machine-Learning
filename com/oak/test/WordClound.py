# -*- coding: utf-8 -*-
# @Time : 2019/7/19 15:05
# @Author : Jiyudong
# @FileName: WordClound.py
# @Software: PyCharm
import jieba
import wordcloud
f = open("F:/Desktop/123.txt", "r")
line = f.read()
f.close()
word = jieba.lcut(line)
c = wordcloud.WordCloud(font_path="F:/Desktop/china.ttf", width=600, height=400)
ss = " ".join(word)
print(ss)
c.generate(ss)
c.to_file("F:/Desktop/123.png")
