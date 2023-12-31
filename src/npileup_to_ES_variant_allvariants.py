# -*- coding: utf-8 -*-
# File Name: npileup_to_ES_variant_allvariants.py
# 1Author: QinYang
# Mail: yyqin90@gmail.com
# Created time: 2016-05-01 21:10:50
# Last modified: 2019-10-09 08:20:30
#!/usr/bin/env python
#****************************************

import os, sys, time
#args: input, ES, variants
#input : chr10:95096     A       2       Gg      Gg^///^<@^///^62,11     0       0       0       0   2  1       0       0       0       0       2       2       0.404931033733664
#output: chr10:95096     a       2       0       0       0       0       2       1       0       0   0  0       2       2       0.404931033733664       g   1

dic = {'a':[5,11],'c':[7,11],'g':[9,11],'t':[13,11]}
dui = {5:'a',7:'c',9:'g',13:'t'}
with open(sys.argv[1],'r') as f1:
    for l1 in f1:
        l1 = l1.strip().split('\t')
        l1[1] = l1[1].lower()
        for i in range(5,15,2):
            if l1[1] in dic and i not in dic[l1[1]]:
                if int(l1[-3])>=int(sys.argv[3]):
                    if float(l1[i])/int(l1[-3]) >float(sys.argv[2]):
                        print(('\t').join(l1[:3]+l1[5:]),'\t',dui[i],l1[i+1])
