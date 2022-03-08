import math
from maxentscan.mes5.utils import makescorematrix, makesequencematrix, getrest, scoreconsensus

def score5(sequence):
    try:
        me2x5 = makescorematrix();
        seq_matrix = makesequencematrix()
        bgd = {'A':0.27,'C':0.23, 'G':0.23, 'T': 0.27}
        if type(sequence) == list:
            result_dic = {}
            for seq in sequence:
                 result = math.log(scoreconsensus(seq) * float(me2x5[seq_matrix[getrest(seq)]]),2)
                 result_dic[seq] = f'{result:.2f}'
            return result_dic
        elif type(sequence) == str:
            result = math.log(scoreconsensus(sequence) * float(me2x5[seq_matrix[getrest(sequence)]]),2)
            return f'{result:.2f}'
        else:
            raise TypeError
    except Exception as e:
        return e
