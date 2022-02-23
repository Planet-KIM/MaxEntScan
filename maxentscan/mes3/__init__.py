from maxentscan.mes3.util import *
import math

def score3(seq):
    metables = makemaxentscores()
    if type(seq) == list:
        result_dic = {}
        for item in seq:
            addscore = scoreconsensus(item) * maxentscore(getrest(item), metables)
            result = math.log(addscore, 2)
            result = f'{result:.2f}'
            result_dic[item] = result
        return result_dic
    else:
        addscore = scoreconsensus(seq) * maxentscore(getrest(seq), metables)
        result = math.log(addscore, 2)
        result = f'{result:.2f}'
        return result
        