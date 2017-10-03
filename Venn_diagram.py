
# coding: utf-8

# In[2]:

import numpy as np
from numpy import nan
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import statistics
get_ipython().magic('matplotlib inline')


# In[3]:

All_Asso_ori = pd.read_csv('Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/Fired_origins.txt', sep="\t")

A364a_WT_1 = All_Asso_ori['A364a_WT_1']
A364a_WT_1 = A364a_WT_1.dropna()

A364a_rad53_1 = All_Asso_ori['A364a_rad53_1']
A364a_rad53_1 = A364a_rad53_1.dropna()

A364a_WT_2 = All_Asso_ori['A364a_WT_2']
A364a_WT_2 = A364a_WT_2.dropna()

A364a_rad53_2 = All_Asso_ori['A364a_rad53_2']
A364a_rad53_2 = A364a_rad53_2.dropna()

W303_WT_1 = All_Asso_ori['W303_WT_1']
W303_WT_1 = W303_WT_1.dropna()

W303_rad53_1 = All_Asso_ori['W303_rad53_1']
W303_rad53_1 = W303_rad53_1.dropna()
#pd.options.display.max_rows = 999
#print(W303_rad53_1)

W303_WT_2 = All_Asso_ori['W303_WT_2']
W303_WT_2 = W303_WT_2.dropna()

W303_rad53_2 = All_Asso_ori['W303_rad53_2']
W303_rad53_2 = W303_rad53_2.dropna()




# In[5]:

A364a_WT = list(set(A364a_WT_1).intersection(A364a_WT_2))
A364a_WT = pd.DataFrame(A364a_WT)
A364a_WT.columns = ['A364a_WT']
A364a_WT.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/A364a_WT_common.txt",index=None, sep='\t')

A364a_rad53 = list(set(A364a_rad53_1).intersection(A364a_rad53_2))
A364a_rad53 = pd.DataFrame(A364a_rad53)
A364a_rad53.columns = ['A364a_rad53']
A364a_rad53.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/A364a_rad53_common.txt",index=None, sep='\t')

W303_WT = list(set(W303_WT_1).intersection(W303_WT_2))
W303_WT = pd.DataFrame(W303_WT)
W303_WT.columns = ['W303_WT']
W303_WT.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/W303_WT_common.txt",index=None, sep='\t')

W303_rad53 = list(set(W303_rad53_1).intersection(W303_rad53_2))
W303_rad53 = pd.DataFrame(W303_rad53)
W303_rad53.columns = ['W303_rad53']
W303_rad53.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/W303_rad53_common.txt", index=None, sep='\t')


# In[6]:

from matplotlib_venn import venn2
venn2([set(A364a_WT_1), set(A364a_WT_2)], ('Exp1', 'Exp2'))
plt.title("A364a WT")
plt.show()


# In[7]:

venn2([set(A364a_rad53_1), set(A364a_rad53_2)], ('Exp1', 'Exp2'))
plt.title("A364a rad53")
plt.show()


# In[8]:

venn2([set(W303_WT_1), set(W303_WT_2)], ('Exp1', 'Exp2'))
plt.title("W303 WT")
plt.show()


# In[9]:

venn2([set(W303_rad53_1), set(W303_rad53_2)], ('Exp1', 'Exp2'))
plt.title("W303 rad53")
plt.show()


# In[10]:

merge1 = pd.merge(A364a_WT, A364a_rad53, how = 'outer', left_on = 'A364a_WT', right_on = 'A364a_rad53')
merge1.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/A364A_origins.txt",index=None, sep='\t')
merge2 = pd.merge(W303_WT, W303_rad53, how = 'outer', left_on = 'W303_WT', right_on = 'W303_rad53')
merge2.to_csv("Identified_ssDNA_Peaks/Peak_bed/Asso/OriANA_ori2000/W303_origins.txt",index=None, sep='\t')


# In[ ]:



