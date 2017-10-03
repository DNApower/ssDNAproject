
# coding: utf-8

# # Identify #peak with various Min_dist

# In[1]:

import numpy as np
from numpy import nan
import pandas as pd
import peakutils
from peakutils.plot import plot as pplot
from matplotlib import pyplot
import seaborn as sns
import statistics
get_ipython().magic('matplotlib inline')


# In[2]:

file_list = ['Normalized_data/A364a_WT_exp1_new.csv',
             'Normalized_data/A364a_WT_exp2_new.csv',
             'Normalized_data/A364a_rad53_exp1_new.csv',
             'Normalized_data/A364a_rad53_exp2_new.csv',
             'Normalized_data/W303_WT_exp1_new.csv',
             'Normalized_data/W303_WT_exp2_new.csv',
             'Normalized_data/W303_rad53_exp1_new.csv',
             'Normalized_data/W303_rad53_exp2_new.csv']


# def ssDNA_peaks(a):  
#     import numpy as np
#     from numpy import nan
#     import pandas as pd
#     import peakutils
#     from peakutils.plot import plot as pplot
#     import statistics
#     
# 
#     df1 = pd.read_csv(a, sep=",")
# 
#     cols = ['Coord', 'ssDNA']
#     chr1 = df1[['Coordinates (kb)', 'Chr1_ssDNA_new']]
#     chr1 = chr1.dropna()
#     #chr1[chr1 < 0] = nan
#     chr1.columns = cols
#     chr1['chromosome'] = 1
# 
#     chr2 = df1[['Coordinates (kb)', 'Chr2_ssDNA_new']]
#     chr2 = chr2.dropna()
#     #chr2[chr2 < 0] = nan
#     chr2.columns = cols
#     chr2['chromosome'] = 2
# 
#     chr3 = df1[['Coordinates (kb)', 'Chr3_ssDNA_new']]
#     chr3 = chr3.dropna()
#     #chr3[chr3 < 0] = nan
#     chr3.columns = cols
#     chr3['chromosome'] = 3
# 
#     chr4 = df1[['Coordinates (kb)', 'Chr4_ssDNA_new']]
#     chr4 = chr4.dropna()
#     #chr4[chr4 < 0] = nan
#     chr4.columns = cols
#     chr4['chromosome'] = 4
# 
#     chr5 = df1[['Coordinates (kb)', 'Chr5_ssDNA_new']]
#     chr5 = chr5.dropna()
#     #chr5[chr5 < 0] = nan
#     chr5.columns = cols
#     chr5['chromosome'] = 5
# 
#     chr6 = df1[['Coordinates (kb)', 'Chr6_ssDNA_new']]
#     chr6 = chr6.dropna()
#     #chr6[chr6 < 0] = nan
#     chr6.columns = cols
#     chr6['chromosome'] = 6
# 
#     chr7 = df1[['Coordinates (kb)', 'Chr7_ssDNA_new']]
#     chr7 = chr7.dropna()
#     #chr7[chr7 < 0] = nan
#     chr7.columns = cols
#     chr7['chromosome'] = 7
# 
#     chr8 = df1[['Coordinates (kb)', 'Chr8_ssDNA_new']]
#     chr8 = chr8.dropna()
#     #chr8[chr8 < 0] = nan
#     chr8.columns = cols
#     chr8['chromosome'] = 8
# 
#     chr9 = df1[['Coordinates (kb)', 'Chr9_ssDNA_new']]
#     chr9 = chr9.dropna()
#     #chr9[chr9 < 0] = nan
#     chr9.columns = cols
#     chr9['chromosome'] = 9
# 
#     chr10 = df1[['Coordinates (kb)', 'Chr10_ssDNA_new']]
#     chr10 = chr10.dropna()
#     #chr10[chr10 < 0] = nan
#     chr10.columns = cols
#     chr10['chromosome'] = 10
# 
#     chr11 = df1[['Coordinates (kb)', 'Chr11_ssDNA_new']]
#     chr11 = chr11.dropna()
#     #chr11[chr11 < 0] = nan
#     chr11.columns = cols
#     chr11['chromosome'] = 11
# 
#     chr12 = df1[['Coordinates (kb)', 'Chr12_ssDNA_new']]
#     chr12 = chr12.dropna()
#     #chr12[chr12 < 0] = nan
#     chr12.columns = cols
#     chr12['chromosome'] = 12
# 
#     chr13 = df1[['Coordinates (kb)', 'Chr13_ssDNA_new']]
#     chr13 = chr13.dropna()
#     #chr13[chr13 < 0] = nan
#     chr13.columns = cols
#     chr13['chromosome'] = 13
# 
#     chr14 = df1[['Coordinates (kb)', 'Chr14_ssDNA_new']]
#     chr14 = chr14.dropna()
#     #chr14[chr14 < 0] = nan
#     chr14.columns = cols
#     chr14['chromosome'] = 14
# 
#     chr15 = df1[['Coordinates (kb)', 'Chr15_ssDNA_new']]
#     chr15 = chr15.dropna()
#     #chr15[chr15 < 0] = nan
#     chr15.columns = cols
#     chr15['chromosome'] = 15
# 
#     chr16 = df1[['Coordinates (kb)', 'Chr16_ssDNA_new']]
#     chr16 = chr16.dropna()
#     #chr16[chr16 < 0] = nan
#     chr16.columns = cols
#     chr16['chromosome'] = 16
# 
#     All_chro = pd.concat([chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10])
#     All_chro = pd.concat([All_chro, chr11, chr12, chr13, chr14, chr15, chr16])
#     All_chro = All_chro.reset_index(drop=True)
# 
# 
# 
#     Med = statistics.median(All_chro['ssDNA'])
# 
#     mylist = []
#     for ss in All_chro['ssDNA']:
#         if ss < Med:
#             mylist.append(ss)
#     subdata = np.array(mylist)
# 
#     mylist_std = statistics.stdev(mylist)
# 
#     Cutoff = Med + mylist_std*3
#     print(Cutoff)
# 
#     thres_percentage = (Cutoff - All_chro['ssDNA'].min())/(All_chro['ssDNA'].max() - All_chro['ssDNA'].min())
# 
#     Min_dist_testing_list = [1, 2, 4, 6, 8, 10]
# 
#     for y in Min_dist_testing_list:
# 
#         indexes = peakutils.indexes(All_chro['ssDNA'], thres=thres_percentage, min_dist=y)
# 
#         print("name: {}".format(a), " ", y, " ", len(indexes))
# 
#         #Peak_list = ["Index", "Chromosome", "Coord_kb", "ssDNA"]
#         #j = 0
#         #while j < len(indexes):
#             #arr = np.array([indexes[j], All_chro['chromosome'][indexes[j]], All_chro['Coord'][indexes[j]], All_chro['ssDNA'][indexes[j]]])
#             #Peak_list = np.vstack((Peak_list, arr))
#             #j += 1
# 
#         #df2 = pd.DataFrame(Peak_list)
#         #df2.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/{}_{}.csv".format(a,y), header=None,index=False)

# In[4]:

for x in file_list:
    ssDNA_peaks(x)


# In[3]:

def ssDNA_peaks1(a):  
    import numpy as np
    from numpy import nan
    import pandas as pd
    import peakutils
    from peakutils.plot import plot as pplot
    import statistics
    

    df1 = pd.read_csv(a, sep=",")

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

    All_chro = pd.concat([chr1, chr2, chr3, chr4, chr5, chr6, chr7, chr8, chr9, chr10])
    All_chro = pd.concat([All_chro, chr11, chr12, chr13, chr14, chr15, chr16])
    All_chro = All_chro.reset_index(drop=True)



    Med = statistics.median(All_chro['ssDNA'])

    mylist = []
    for ss in All_chro['ssDNA']:
        if ss < Med:
            mylist.append(ss)
    subdata = np.array(mylist)

    mylist_std = statistics.stdev(mylist)

    Cutoff = Med + mylist_std*3

    thres_percentage = (Cutoff - All_chro['ssDNA'].min())/(All_chro['ssDNA'].max() - All_chro['ssDNA'].min())

    Min_dist_testing_list = [1, 2, 4, 6, 8, 10]

    for y in Min_dist_testing_list:

        indexes = peakutils.indexes(All_chro['ssDNA'], thres=thres_percentage, min_dist=y)

        print("name: {}".format(a), " ", y, " ", len(indexes))

        Peak_list = ["Index", "Chromosome", "Coord_kb", "ssDNA"]
        j = 0
        while j < len(indexes):
            arr = np.array([indexes[j], All_chro['chromosome'][indexes[j]], All_chro['Coord'][indexes[j]], All_chro['ssDNA'][indexes[j]]])
            Peak_list = np.vstack((Peak_list, arr))
            j += 1

        df2 = pd.DataFrame(Peak_list)
        #df2.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/data/Min_dist_{}_{}.csv".format(y, a[16:]), header=None,index=False)


# In[ ]:

for x in file_list:
    ssDNA_peaks1(x)


# In[4]:

Mid_Dist = [1, 2, 4, 6, 8, 10]
file_name = []
for x in Mid_Dist:
    for y in file_list:
        file_name.append("Min_dist_"+ str(x) +"_"+y[16:]+".csv")


# In[5]:

def PeakBed(x):
    df3 = pd.read_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/data/{}".format(x), sep=",")
    df3['Chromosome'] = df3['Chromosome'].astype(int)
    df3['Index'] = df3['Index'].astype(int)

    df4= df3[['Index','Chromosome', 'Coord_kb', 'ssDNA']]

    df4['Start'] = (df4['Coord_kb'] - 0.25)*1000
    df4['end'] = (df4['Coord_kb'] + 0.25)*1000

    df4['Chromosome'] = df4['Chromosome'].astype(str)
    df4['Coord_kb'] = df4['Coord_kb'].astype(str)
    df4['Start'] = df4['Start'].astype(int)
    df4['end'] = df4['end'].astype(int)
    df4['Chr'] = "chr" + df4['Chromosome']
    df4['Description'] = "PeakIndex" + df4['Coord_kb'] + ":" + df4['ssDNA'].astype(str)

    df5 = df4[['Chr', 'Start', 'end', 'Description']]

    df5.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/data/Peak_bed/{}.bed".format(x), header=None,index=None, sep='\t', mode = 'a')


# In[7]:

for x in file_name:
    PeakBed(x)


# ### Origin Bed files

# In[ ]:

df6 = pd.read_csv('origins_oridb.txt', sep="\t")

expansion = [100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]

for y in expansion:
    df6['start'] = df6['Mid_point'] - y
    df6['end'] = df6['Mid_point'] + y
    num = df6._get_numeric_data()
    num[num < 0] = 0
    df6['chro'] = "chr" + df6['chr'].astype(str)
    df6['start'] = df6['start'].astype(int)
    df6['end'] = df6['end'].astype(int)
    origins = df6[['chro', 'start', 'end', 'name']]
    origins.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/Origins/ori{}.bed".format(y), header=None,index=None, sep='\t', mode = 'a')


# In[8]:

get_ipython().run_cell_magic('bash', '', 'pwd\ncd Identified_ssDNA_Peaks/Peak_finder_parameters/data/Peak_bed\npwd\nfor ori in ori*.bed\ndo\n    for peak in Min_dist_*.csv.csv.bed\n    do\n        bedtools intersect -a ${ori} -b ${peak} -wa -wb> Ori_Peak_Asso/${ori}_${peak}.txt\n    done\ndone\n       ')


# In[7]:

file_name


# In[14]:

dfop = pd.read_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/data/Peak_bed/Ori_Peak_Asso/ori100.bed_Min_dist_1_A364a_rad53_exp1_new.csv.csv.bed.txt", header = None, sep="\t")
col_op = ['Ori_chr', 'Ori_start', 'Ori_end', 'Ori_name', 'Peak_chr', 'Peak_start', 'Peak_end', 'Peak_name']
dfop.columns = col_op
dfop['Peak'] =dfop['Peak_chr'] + ':' + dfop['Peak_start'].astype(str) + '-' + dfop['Peak_end'].astype(str) + ':' + dfop['Peak_name']
ap = pd.DataFrame(dfop['Peak'].value_counts())
bp= pd.DataFrame(ap['Peak'].value_counts())
bp['expation'] = 100
bp['strain'] = "A364a_rad53_exp1"

ao = pd.DataFrame(dfop['Ori_name'].value_counts())
bo= pd.DataFrame(ao['Ori_name'].value_counts())
print(bo)
print("********")
print(bp)
bp.to_csv("dist_test.txt", sep='\t')


# In[22]:

expansion = [100, 250, 500, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 5500, 6000]
Origin_dist = pd.DataFrame()
Peak_dist =pd.DataFrame()
for expa in expansion:
    for file in file_name:
        dfop = pd.read_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/data/Peak_bed/Ori_Peak_Asso/ori{}.bed_{}.bed.txt".format(expa, file), header = None, sep="\t")
        col_op = ['Ori_chr', 'Ori_start', 'Ori_end', 'Ori_name', 'Peak_chr', 'Peak_start', 'Peak_end', 'Peak_name']
        dfop.columns = col_op
        dfop['Peak'] =dfop['Peak_chr'] + ':' + dfop['Peak_start'].astype(str) + '-' + dfop['Peak_end'].astype(str) + ':' + dfop['Peak_name']
        ap = pd.DataFrame(dfop['Peak'].value_counts())
        bp= pd.DataFrame(ap['Peak'].value_counts())
        bp['expation'] = expa
        bp['strain'] = file
        Peak_dist = Peak_dist.append(bp)
        ao = pd.DataFrame(dfop['Ori_name'].value_counts())
        bo= pd.DataFrame(ao['Ori_name'].value_counts())
        bo['expation'] = expa
        bo['strain'] = file
        Origin_dist = Origin_dist.append(bo)
        #print(bo)
        #print("********")
        #print(bp)
Origin_dist.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/Origin_dist.txt", sep='\t')
Peak_dist.to_csv("Identified_ssDNA_Peaks/Peak_finder_parameters/Peak_dist.txt", sep='\t')


# In[3]:

get_ipython().run_cell_magic('bash', '', 'pwd\ncd Identified_ssDNA_Peaks/Peak_finder_parameters/data/Peak_bed\npwd\nfor ori in ori*.bed\ndo\n    for peak in Min_dist_*.csv.csv.bed\n    do\n        bedtools intersect -a ${ori} -b ${peak} -c> Orphan/Orphan_ori/Orphan_ori_${ori}_${peak}.txt\n        bedtools intersect -a ${peak} -b ${ori} -c> Orphan/Orphan_peak/Orphan_peak_${ori}_${peak}.txt\n    done\ndone')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



