import sys
import os
sys.path.append('../')
from maxentscan.mes5 import score5
test = score5(
    [ 'acggtaagt',
      'caggtaagt'
     ])
print(test)