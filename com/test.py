import time
import os, sys

N = 1000


s_time = time.time()
fp = open('test.txt', 'w')
fp.truncate()

for n in xrange(N):
    fp.write('Num:'+str(n))
    fp.flush()
fp.close()

print time.time() - s_time
