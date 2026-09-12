from numpy import round as rnd
import matplotlib.pyplot as plt
import pandas as pd
from math import sqrt as sq

#محسابه ی واریانس و انحراف معیار
def scale(lst, vrnc=False):
    lst2=[]
    for tmp in lst:
        lst2.append(((sum(lst)/len(lst))-tmp)**2)
    variance=sum(lst2)/len(lst2)
    if vrnc:
        return variance
    return(sq(variance))

#بالاترین دما
def maxim(lst):
    return max(lst)

#پایین ترین دما
def minim(lst):
    return min(lst)

#میانگین دما
def loc(lst):
    return sum(lst)/len(lst)

#تولید نمودار و هیستوگرام
def vector(x,y):
    plt.figure(figsize=(25,6))
    plt.plot(x,y,linewidth=1, color='blue')
    plt.show()
def histogram(tmps):
    bins = (rnd(sq(len(tmps)))).astype(int)
    plt.hist(tmps, bins, edgecolor='black', alpha=0.7)
    plt.show()


#دیسکرایب کردن فایل سی اس وی
def describe(name):
    tmp_lis = ((pd.read_csv(name, index_col=0))['Tmps'].tolist())
    x = (((pd.read_csv(name)).index)+1).tolist()
    print("scale: ", scale(tmp_lis), end='\n -------------------- \n')
    print("variance: ", scale(tmp_lis,True), end='\n -------------------- \n')
    print("max tmp: ", maxim(tmp_lis), end='\n -------------------- \n')
    print("min tmp: ",minim(tmp_lis), end='\n -------------------- \n')
    print("loc tmps: ", loc(tmp_lis), end='\n -------------------- \n')
    input("press enter to show vector...")
    vector(x, tmp_lis)
    print('-'*20)
    input("press enter to show histogram...")
    histogram(tmp_lis)
