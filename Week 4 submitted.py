# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 12:09:11 2022

@author: ditsi
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 00:03:25 2022

@author: ditsi
"""
import pandas as pd
import datetime as dt
import numpy as np
import sys
import matplotlib.pyplot as plt

#Introduction
# The data have been downloaded from the Greek Ministry of Environmental. To be more specific 
# they are the data of concentration of PM10 of Thessaloniki,Greece, the station of Kordelio, a urban and 
#industrial area, and the station of Panorama where is outside the metropolitan area so the measured
#PM10 derive mainly from the background. Thus, in Kordelio are expected higher concentrations.
# Also, Kordelio measurements are for 2001-2005 period and Panorama for 2001-2004 period.
# Link of data
#https://ypen.gov.gr/perivallon/poiotita-tis-atmosfairas/dedomena-metriseon-atmosfairikis-rypansis/
#KORDELIO
# https://drive.google.com/file/d/1efLhsZdg1ZinyutIBssq82CgGjbuAf95/view?usp=sharing
#PANORAMA
#https://drive.google.com/file/d/1OrNhMe2m4TAkIDLgW2GEyMkoOkscvZq5/view?usp=sharing
# Question
# Where higher concentration are measured? 
#Diagrams
# In the same diagram we have two plots each for station, while the mean monthly means are compared, so
# 12 
file=open('C:/Users/ditsi/Downloads/PM10#KODEEC2001-2005.dat', 'r')
file_2=open('C:/Users/ditsi/Downloads/PM10#PAOEEC2001-2004.dat', 'r')

data=np.loadtxt(file,dtype=object,skiprows=2,delimiter=',')
pm10_KOR=data[:,1].astype(float)
data_2=np.loadtxt(file_2,dtype=object,skiprows=2,delimiter=',')
pm10_PAO=data_2[:,1].astype(float)

date=data[:,0]
aer_time=np.zeros(date.shape[0],dtype=object)

for i in range(len(data)):
    day=int(date[i][6:8])
    month=int(date[i][4:6])
    year=int(date[i][0:4])
    hour=int(date[i][9:11])
    minute=int(date[i][12:14])
    # second=int(time[i][6:])
    aer_time[i]=dt.datetime(year,month,day,hour,minute)
#sys.exit()
date_2=data_2[:,0]
aer_time_2=np.zeros(date_2.shape[0],dtype=object)

for i in range(len(data_2)):
    day=int(date_2[i][6:8])
    month=int(date_2[i][4:6])
    year=int(date_2[i][0:4])
    hour=int(date_2[i][9:11])
    minute=int(date_2[i][12:14])
    aer_time_2[i]=dt.datetime(year,month,day,hour,minute)


pm10_KOR=pd.DataFrame(pm10_KOR, index=aer_time,columns=['PM10_KOR'])
pm10_KOR=pm10_KOR.where(pm10_KOR>0).dropna()
pm10_PAO=pd.DataFrame(pm10_PAO, index=aer_time_2,columns=['PM10_PAO'])
pm10_PAO=pm10_PAO.where(pm10_PAO>0).dropna()

fig, ax = plt.subplots() 
ax.plot(range(1,13), pm10_KOR.groupby([lambda x: x.month]).mean(),'b-o',label='Annual Circle for Kordelio')
ax.plot(range(1,13), pm10_PAO.groupby([lambda x: x.month]).mean(),'r-o',label='Annual Circle for Panorama')
plt.legend()
plt.ylim(0,100)
ax.set_ylabel('Concentration μg/m^(-3)',color='k')
ax.set_xlabel('Months of a year', color='k')
ax.set_title('Annual Circle of PM10')
plt.show() ; plt.close()



