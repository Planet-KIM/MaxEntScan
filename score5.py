import os
import sys
import math

def makescorematrix(mefile='me2x5'):
    me_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), mefile)
    matrix = {}
    with open(me_path) as me_file:
        for index, item in enumerate(me_file.readlines()):
            matrix[index]=item.replace('\n', '').replace(' ', '')
    return matrix
  
def makesequencematrix(splice='splicemodels/splice5sequences'):
    splice_path = os.path.join(os.path.dirname(os.path.realpath(__name__)), splice)
    matrix = {}
    with open(splice_path) as splice_file:
        for index, item in enumerate(splice_file.readlines()):
            matrix[item.replace('\n','')] = index
    return matrix


def getrest(seq):
    seq = list(seq.upper()[:9])
    seq = ''.join(seq)
    seq = seq[:3] + seq[5:9]
    return seq


def scoreconsensus(seq):
    seqa = list(seq.upper())
    bgd = {'A':0.27,'C':0.23, 'G':0.23, 'T': 0.27}
    cons1 = {'A' : 0.004, 'C':0.0032,'G':0.9896,'T':0.0032 }
    cons2 = {'A' : 0.0034,'C':0.0039,'G':0.0042,'T':0.9884 }
    addscore = cons1[seqa[3]]*cons2[seqa[4]]/(bgd[seqa[3]]*bgd[seqa[4]]); 
    return addscore



def score5(seq_list):
    me2x5 = makescorematrix();
    seq_matrix = makesequencematrix()
    bgd = {'A':0.27,'C':0.23, 'G':0.23, 'T': 0.27}
    result_dic = {}
    for seq in seq_list:
         print(me2x5[seq_matrix[getrest(seq)]])
         print(scoreconsensus(seq))
         result = math.log(scoreconsensus(seq) * float(me2x5[seq_matrix[getrest(seq)]]),2)
         result_dic[seq] = f'{result:.2f}'
    return result_dic


seq_list = ['caggtaagt',"acggtaagt", "caggtaagt"]
result = score5(seq_list)
print(result)





