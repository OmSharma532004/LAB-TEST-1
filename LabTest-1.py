#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import scipy as sci
from scipy import signal


# In[89]:


# vehdata=np.random()
mins=1440
noise=20+10*np.sin(2* np.pi / mins*2)

AQI_data=np.random.random(mins)

noisyData=AQI_data+noise
noisyData




# In[90]:


a,b= sci.signal.butter(4,0.5)
smoothdata=sci.signal.filtfilt(a,b,noisyData,axis=-1, padtype='odd', padlen=None, method='pad', irlen=None)

print("Smooth data :- " , smoothdata)



help(sci.signal.butter)


# In[86]:


def calculateAvg(smooth):
   hourly=smoothdata.reshape(24,60)
   average_data=np.mean(hourly,axis=-1)
   return average_data

hourlyAvg=calculateAvg(smoothdata)
hourlyAvg


# In[22]:


import matplotlib.pyplot as plt


# In[77]:


x= np.arange(0,1440,1)
noisyData.reshape(1440,1)
plt.plot(x,noisyData,'r')
plt.xlabel("Minutes")
plt.ylabel("AQI")
plt.title("NoisyData")
plt.show()


# In[75]:


x= np.arange(0,1440,1)
noisyData.reshape(1440,1)
plt.plot(x,smoothdata,'r')
plt.xlabel("Minutes")
plt.ylabel("AQI")
plt.title("SmoothData")
plt.show()


# In[88]:


x= np.arange(0,24,1)
noisyData.reshape(1440,1)
plt.plot(x,hourlyAvg,'r')
plt.xlabel("Minutes")
plt.ylabel("AQI")
plt.title("HourlyAvg")
plt.show()


# In[ ]:




