# 하나 뽑기
from random import choice

def pick_one(*ones):
     one_list = list(ones)
     print(choice(one_list))

pick_one(1,2,3,4,5)