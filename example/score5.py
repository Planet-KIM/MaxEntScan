import math
from maxentscan.mes5 import score5

seq_list = ['caggtaagt',"acggtaagt", "caggtaagt"]
result = score5(seq_list)
print(result)

result = score5('caggtaagt')
print(result)
