#%%
import random
from sys import argv
sign = lambda: '-' if random.random() < 0.4 else ''
number = lambda e: str(random.randint(0,e))
row = lambda: '/'.join([sign()+number(15), number(22), number(16)])
if __name__ == '__main__':
    n = int(argv[1])
    fpath = argv[2]
    f = open(fpath, 'w')
    f.write(row())
    for _ in range(1,n):
        f.write("\n"+row())
    f.close()
