#%%
readfile = lambda x:open(x).read().split("\n")
parse = lambda x:[int(y) for y in x.split('/')]
def knuts(x):
    sign = "-" if x[0] < 0 else ""
    k = (abs(x[0])*23 + x[1])*17+x[2]
    k = -k if sign else k 
    return k 
original_data = [parse(y) for y in readfile('lab2data')]
converted_data = list(map(lambda x: knuts(x), original_data))
# convert back 
def decify(num, d):
    a = int(num/d)
    b = abs(num) - abs(a)*d
    return a, b
def to_form(num):
    gal, rest = decify(num,23*17)
    sic, knu = decify(rest, 17)
    return [gal, sic, knu]

data_back = [to_form(n) for n in converted_data]

assert all(map(lambda x:all([x[0][i]==x[1][i] for i in range(len(x))]),list(zip(original_data, data_back))))
# %%
