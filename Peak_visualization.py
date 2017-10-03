
# coding: utf-8

# In[1]:

import numpy as np
from numpy import nan
import pandas as pd
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot
import seaborn as sns
get_ipython().magic('matplotlib inline')


# In[2]:

df1 = pd.read_csv('dat/A364a_WT_exp1_new.csv', sep=",")
df1.head()


# In[3]:

cols = ['Coord', 'ssDNA']
chr1 = df1[['Coordinates (kb)', 'Chr1_ssDNA_new']]
chr1 = chr1.dropna()
#chr1[chr1 < 0] = nan
chr1.columns = cols
chr1['chromosome'] = 1

chr2 = df1[['Coordinates (kb)', 'Chr2_ssDNA_new']]
chr2 = chr2.dropna()
#chr2[chr2 < 0] = nan
chr2.columns = cols
chr2['chromosome'] = 2

chr3 = df1[['Coordinates (kb)', 'Chr3_ssDNA_new']]
chr3 = chr3.dropna()
#chr3[chr3 < 0] = nan
chr3.columns = cols
chr3['chromosome'] = 3

chr4 = df1[['Coordinates (kb)', 'Chr4_ssDNA_new']]
chr4 = chr4.dropna()
#chr4[chr4 < 0] = nan
chr4.columns = cols
chr4['chromosome'] = 4

chr5 = df1[['Coordinates (kb)', 'Chr5_ssDNA_new']]
chr5 = chr5.dropna()
#chr5[chr5 < 0] = nan
chr5.columns = cols
chr5['chromosome'] = 5

chr6 = df1[['Coordinates (kb)', 'Chr6_ssDNA_new']]
chr6 = chr6.dropna()
#chr6[chr6 < 0] = nan
chr6.columns = cols
chr6['chromosome'] = 6

chr7 = df1[['Coordinates (kb)', 'Chr7_ssDNA_new']]
chr7 = chr7.dropna()
#chr7[chr7 < 0] = nan
chr7.columns = cols
chr7['chromosome'] = 7

chr8 = df1[['Coordinates (kb)', 'Chr8_ssDNA_new']]
chr8 = chr8.dropna()
#chr8[chr8 < 0] = nan
chr8.columns = cols
chr8['chromosome'] = 8

chr9 = df1[['Coordinates (kb)', 'Chr9_ssDNA_new']]
chr9 = chr9.dropna()
#chr9[chr9 < 0] = nan
chr9.columns = cols
chr9['chromosome'] = 9

chr10 = df1[['Coordinates (kb)', 'Chr10_ssDNA_new']]
chr10 = chr10.dropna()
#chr10[chr10 < 0] = nan
chr10.columns = cols
chr10['chromosome'] = 10

chr11 = df1[['Coordinates (kb)', 'Chr11_ssDNA_new']]
chr11 = chr11.dropna()
#chr11[chr11 < 0] = nan
chr11.columns = cols
chr11['chromosome'] = 11

chr12 = df1[['Coordinates (kb)', 'Chr12_ssDNA_new']]
chr12 = chr12.dropna()
#chr12[chr12 < 0] = nan
chr12.columns = cols
chr12['chromosome'] = 12

chr13 = df1[['Coordinates (kb)', 'Chr13_ssDNA_new']]
chr13 = chr13.dropna()
#chr13[chr13 < 0] = nan
chr13.columns = cols
chr13['chromosome'] = 13

chr14 = df1[['Coordinates (kb)', 'Chr14_ssDNA_new']]
chr14 = chr14.dropna()
#chr14[chr14 < 0] = nan
chr14.columns = cols
chr14['chromosome'] = 14

chr15 = df1[['Coordinates (kb)', 'Chr15_ssDNA_new']]
chr15 = chr15.dropna()
#chr15[chr15 < 0] = nan
chr15.columns = cols
chr15['chromosome'] = 15

chr16 = df1[['Coordinates (kb)', 'Chr16_ssDNA_new']]
chr16 = chr16.dropna()
#chr16[chr16 < 0] = nan
chr16.columns = cols
chr16['chromosome'] = 16


# In[4]:

All_chro = pd.concat([chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10])
All_chro = pd.concat([All_chro, chr11, chr12, chr13, chr14, chr15, chr16])
All_chro = All_chro.reset_index(drop=True)
All_chro


# In[5]:

import statistics

Med = statistics.median(All_chro['ssDNA'])
print('Median is ' + str(Med))


# In[6]:

mylist = []
for ss in All_chro['ssDNA']:
    if ss < Med:
        mylist.append(ss)
subdata = np.array(mylist)

mylist_std = statistics.stdev(mylist)
print("std: " + str(mylist_std))


# In[7]:

Cutoff = Med + mylist_std*3
print("Significance Cutoff: " + str(Cutoff))


# In[8]:

thres_percentage = (Cutoff - All_chro['ssDNA'].min())/(All_chro['ssDNA'].max() - All_chro['ssDNA'].min())
## The reason for this transformation is that the 'thres' is a nomalized value from 0 and 1 in the peak detection function indexes(y, thres, min_dist). 
## In the function, the 'thres' is then transfromed for real calculation by this equation: thres = thres * (np.max(y) - np.min(y)) + np.min(y)

print("Maximun: " + str(All_chro['ssDNA'].max()))
print("Minimun: " + str(All_chro['ssDNA'].min()))
print("Threshold for Peak detection: " + str(thres_percentage))


# In[9]:

indexes = peakutils.indexes(All_chro['ssDNA'], thres=thres_percentage, min_dist=1)


# In[10]:

Peak_list = ["Index", "Chromosome", "Coord_kb", "ssDNA"]
j = 0
while j < len(indexes):
    arr = np.array([indexes[j], All_chro['chromosome'][indexes[j]], All_chro['Coord'][indexes[j]], All_chro['ssDNA'][indexes[j]]])
    Peak_list = np.vstack((Peak_list, arr))
    j += 1
#print(Peak_list)

df = pd.DataFrame(Peak_list)
df.to_csv("A364a_rad53_exp1_new_peaks_1.csv", header=None,index=False)


# In[11]:

df2 = pd.read_csv('A364a_rad53_exp1_new_peaks_1.csv', sep=",")
df2['Index'] = df2['Index'].astype(int)
df2.head()


# In[12]:

size = [2.30218, 8.13184, 3.1662, 15.31933, 5.76874, 2.70161, 10.9094, 5.62643, 4.39888, 7.45751, 6.66816, 10.78177, 9.24431, 7.84333, 10.91291, 9.48066]
Figures = []
i = 1
while i <= 16:
    Chr = All_chro.loc[All_chro['chromosome'] == i]
    peaks = df2.loc[df2['Chromosome'] == i]
    #idx = Chr[df2['Index']].index.tolist()
    globals()['Figure{}'.format(i)] = pyplot.figure(figsize=(size[i-1], 3))
    #pyplot.plot(Chr['Coord_kb_x'], Chr['ssDNA_loess'], )
    pplot(Chr['Coord'], Chr['ssDNA'], peaks['Index'])
    pyplot.title("Chr" + str(i))
    pyplot.legend(loc='upper right', fontsize = 'x-small')
    axes = pyplot.gca()
    axes.set_ylim([0,35])
    Figures.append(globals()['Figure{}'.format(i)])
    i += 1


# In[ ]:



