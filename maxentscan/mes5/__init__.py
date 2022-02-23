import math
from maxentscan.mes5.utils import makescorematrix, makesequencematrix, scoreconsensus, getrest

def score5(seq):
     me2x5 = makescorematrix();
     seq_matrix = makesequencematrix()
     #bgd = {'A':0.27,'C':0.23, 'G':0.23, 'T': 0.27}
     if type(seq) == list:
          result_dic = {}
          for item in seq:
               #print(me2x5[seq_matrix[getrest(item)]])
               #print(scoreconsensus(item))
               result = math.log(scoreconsensus(item) * float(me2x5[seq_matrix[getrest(item)]]),2)
               result_dic[item] = float(f'{result:.2f}')
          return result_dic
     else:
          result = math.log(scoreconsensus(seq) * float(me2x5[seq_matrix[getrest(seq)]]),2)
          result = f'{result:.2f}'
          return float(result)
         