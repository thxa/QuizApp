import os

l,r=1,10000
for i in range(50):
    os.system("rm output/quiz_{%d..%d}.json" %(l, r))
    l=r 
    r+=10000


