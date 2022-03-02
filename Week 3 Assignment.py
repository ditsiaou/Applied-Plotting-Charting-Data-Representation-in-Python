#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats


# In[41]:


df = pd.DataFrame([np.random.normal(32000,10000,5000), 
                   np.random.normal(43000,10000,5000), 
                   np.random.normal(39000,10000,5000), 
                   np.random.normal(48000,10000,5000)], 
                  index=[1992,1993,1994,1995])


# In[42]:


year_avg=df.mean(axis=1)
yerr=df.std(axis=1)
#print(year_avg,yerr)


# In[43]:


bars = plt.bar(df.index, year_avg, yerr= yerr,color='brbr')
# blue under the threshold and red above it
plt.xticks([1992,1993,1994,1995])
plt.plot([0,2000],[39541,39541],'k')
plt.xlim(1991.3,1995.7)
plt.title('Ferreira 2014 Diagrams')
plt.xlabel('Year()')
plt.ylabel('Number of cases')
plt.show() ; plt.close()


# In[ ]:





# In[ ]:





# In[ ]:




