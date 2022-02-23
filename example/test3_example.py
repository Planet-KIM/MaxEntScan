import sys
import os
sys.path.append('../')
from maxentscan.mes3 import score3

# input: sequence list
test = score3(
    ['ctctactactatctatctagatc',
     'ctctactactatctatctacatc',
     'ctctactactctctatctacatc',
     'ctctactactttctatctacatc',
     'ctctactactgtctatctacatc',
     'ctctactaccatctatctacatc',
     'ctctactacaatctatctacatc' ])
print(test)

# input: one sequence
seq = 'ctctactactatctatctagatc'
test = score3(seq)
print(test)
