# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 09:46:35 2021

@author: TQC
"""

score = []
while True :
    inscore = int(input("分數"))
    if inscore == "" :
        break
    else:
        score.append(inscore)
        score2 = sorted(score,reverse=True)
    print(score2)