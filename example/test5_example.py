import sys
import os
sys.path.append('../')
from maxentscan.mes5 import score5

# input: sequence list
test = score5(
    [
      'acggtaagt',
      'caggtaagt'
     ])
print(test)

# input: one sequence
test = score5('acggtaagt')
print(test)
