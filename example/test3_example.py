import sys
import os
sys.path.append('../')
from maxentscan.mes3 import score3
test = score3(
    ['ctctactactatctatctagatc',
     'ctctactactatctatctacatc',
     'ctctactactctctatctacatc',
     'ctctactactttctatctacatc',
     'ctctactactgtctatctacatc',
     'ctctactaccatctatctacatc',
     'ctctactacaatctatctacatc' ])
print(test)