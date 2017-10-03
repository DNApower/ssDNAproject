
# coding: utf-8

# XML file

# In[1]:

from xml.dom import minidom
import numpy as np
import pandas as pd
import statistics
from matplotlib import pyplot as plt
get_ipython().magic('matplotlib inline')


# In[22]:

xmldoc = minidom.parse("output/To_A364a/strain_specific_ori_cl_A364a.xml")


# In[23]:

blast_iterations = xmldoc.getElementsByTagName("BlastOutput_iterations")[0]
iterations = blast_iterations.getElementsByTagName("Iteration")
data = []
for interation in iterations:
    query = str(interation.getElementsByTagName("Iteration_query-def")[0].firstChild.data)
    query_len = int(interation.getElementsByTagName("Iteration_query-len")[0].firstChild.data)
    #print(query, query_len)
    iteration_hits = interation.getElementsByTagName("Iteration_hits")[0]
    hits = iteration_hits.getElementsByTagName("Hit")
    for hit in hits:
        hit_num = int(hit.getElementsByTagName("Hit_num")[0].firstChild.data)
        hit_desc = str(hit.getElementsByTagName("Hit_def")[0].firstChild.data)
        hit_len = int(hit.getElementsByTagName("Hit_len")[0].firstChild.data)
        hit_hsps = hit.getElementsByTagName("Hit_hsps")
        #print(hit_num, hit_desc)
        for hit_hsp in hit_hsps:
            hsps = hit_hsp.getElementsByTagName("Hsp")
            for hsp in hsps:
                hsp_num = int(hit.getElementsByTagName("Hsp_num")[0].firstChild.data)
                query_from = int(hit.getElementsByTagName("Hsp_query-from")[0].firstChild.data)
                query_to = int(hit.getElementsByTagName("Hsp_query-to")[0].firstChild.data)
                hit_from = int(hit.getElementsByTagName("Hsp_hit-from")[0].firstChild.data)
                hit_to = int(hit.getElementsByTagName("Hsp_hit-to")[0].firstChild.data)
                align_len = int(hit.getElementsByTagName("Hsp_align-len")[0].firstChild.data)
                Hsp_qseq = str(hit.getElementsByTagName("Hsp_qseq")[0].firstChild.data)
                Hsp_hseq = str(hit.getElementsByTagName("Hsp_hseq")[0].firstChild.data)
                Hsp_midline = str(hit.getElementsByTagName("Hsp_midline")[0].firstChild.data)
                dt = []
                dt.extend((query, query_len, hit_num, hit_desc, hsp_num, query_from, query_to, hit_from, hit_to, align_len, Hsp_qseq, Hsp_hseq, Hsp_midline))
                data.append(dt)
col = ['Query', 'Query_length', 'Hit_num', 'Hit_description','Hsp_num', 'Query_from', 'Query_to', 'Hit_from', 'Hit_to', 'Alignment_length', 'Query_seq', 'Hit_seq', 'Midline']

data = pd.DataFrame(data)
data.columns = col
print(data.shape)
data.drop_duplicates(keep='first')
print(data.shape)
data.to_csv("output/To_A364a/strain_specific_ori_cl_A364a.txt", index=False, sep='\t')


# blast_iterations = xmldoc.getElementsByTagName("BlastOutput_iterations")[0]
# iterations = blast_iterations.getElementsByTagName("Iteration")
# data = []
# for interation in iterations:
#     query = str(interation.getElementsByTagName("Iteration_query-def")[0].firstChild.data)
#     query_len = int(interation.getElementsByTagName("Iteration_query-len")[0].firstChild.data)
#     #print(query, query_len)
#     iteration_hits = interation.getElementsByTagName("Iteration_hits")[0]
#     hits = iteration_hits.getElementsByTagName("Hit")
#     for hit in hits:
#         hit_num = int(hit.getElementsByTagName("Hit_num")[0].firstChild.data)
#         hit_desc = str(hit.getElementsByTagName("Hit_def")[0].firstChild.data)
#         hit_len = int(hit.getElementsByTagName("Hit_len")[0].firstChild.data)
#         hit_hsps = hit.getElementsByTagName("Hit_hsps")
#         #print(hit_num, hit_desc)
#         for hit_hsp in hit_hsps:
#             hsps = hit_hsp.getElementsByTagName("Hsp")
#             for hsp in hsps:
#                 hsp_num = int(hit.getElementsByTagName("Hsp_num")[0].firstChild.data)
#                 query_from = int(hit.getElementsByTagName("Hsp_query-from")[0].firstChild.data)
#                 query_to = int(hit.getElementsByTagName("Hsp_query-to")[0].firstChild.data)
#                 hit_from = int(hit.getElementsByTagName("Hsp_hit-from")[0].firstChild.data)
#                 hit_to = int(hit.getElementsByTagName("Hsp_hit-to")[0].firstChild.data)
#                 align_len = int(hit.getElementsByTagName("Hsp_align-len")[0].firstChild.data)
#                 #Hsp_qseq = str(hit.getElementsByTagName("Hsp_qseq")[0].firstChild.data)
#                 #Hsp_hseq = str(hit.getElementsByTagName("Hsp_hseq")[0].firstChild.data)
#                 #Hsp_midline = str(hit.getElementsByTagName("Hsp_midline")[0].firstChild.data)
#                 dt = []
#                 dt.extend((query, query_len, hit_num, hit_desc, hsp_num, query_from, query_to, hit_from, hit_to, align_len))
#                 data.append(dt)
# col = ['Query', 'Query_length', 'Hit_num', 'Hit_description','Hsp_num', 'Query_from', 'Query_to', 'Hit_from', 'Hit_to', 'Alignment_length']
# 
# data = pd.DataFrame(data)
# data.columns = col
# print(data.shape)
# data.drop_duplicates(keep='first')
# print(data.shape)
# data.to_csv("A364a/A364a_to_ref.txt", index=False, sep='\t')

# In[24]:

data1 = pd.read_csv('output/To_A364a/strain_specific_ori_cl_A364a.txt', sep="\t")
data2=data1.drop_duplicates(keep='first')
data2.to_csv("output/To_A364a/strain_specific_ori_cl_A364a_clean.txt", index=False, sep='\t')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



