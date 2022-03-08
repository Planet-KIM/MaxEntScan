import math
from maxentscan.mes3.utils import getrest, maxentscore, scoreconsensus, makemaxentscores

def score3(sequence):
    try:
        result_dic = {}
        metables = makemaxentscores()
        if type(sequence) == list:
            for seq in sequence:
                addscore = scoreconsensus(seq) * maxentscore(getrest(seq), metables)
                result = math.log(addscore, 2)
                result = f'{result:.2f}'
                result_dic[seq] = result
            return result_dic
        elif type(sequence) == str:
            addscore = scoreconsensus(sequence) * maxentscore(getrest(sequence), metables)
            result = math.log(addscore, 2)
            return f'{result:.2f}'
        else:
            raise TypeError

    except Exception as e:
        return e
