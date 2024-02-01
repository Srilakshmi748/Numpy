#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


ary1 = np.random.rand(10,20,(5))


# In[3]:


ary1


# In[4]:


ary1.mean()


# ###  Round

# In[5]:


num = 35.3453456787


# In[6]:


np.round(num, 2)


# In[7]:


np.round(num,1)


# In[8]:


np.round(num)


# ###  Insert

# In[9]:


ary1


# In[10]:


np.insert(ary1,2, 55, axis = None )


# In[11]:


ary1


# In[12]:


# multiple values at single index

np.insert(ary1, 2, [55, 56], axis = None)


# In[13]:


ary1


# In[15]:


# Single value at multiple indexs 

np.insert(ary1,[2, 4], 55, axis = None)


# In[16]:


ary1


# In[17]:


np.insert(ary1, [1, 3], [100,200])


# ###  2D Array Insertion

# In[18]:


ary2 = np.random.randint(100,200,(4,6))


# In[19]:


ary2


# In[20]:


np.insert(ary2,2,[22,22,22,22,22,22] )


# In[21]:


np.insert(ary2, 2, [22,22,22,22,22,22], axis = 0)


# In[22]:


ary2


# In[23]:


np.insert(ary2, 3, [100,100,100,100], axis = 1)


# In[24]:


ary2


# In[27]:


np.insert(ary2,4, [100,100,100,100], axis = 1)


# In[30]:


np.insert(ary2,4, [100,100,100,100], axis = 1)


# In[31]:


ary2


# In[32]:


np.insert(ary2, 3, 55, axis = 1)


# In[33]:


ary2


# In[34]:


np.insert(ary2, 3, 55, axis = 0)


# ###  Append

# In[35]:


ary1


# In[36]:


np.append(ary1, 1000, axis = None)


# In[37]:


ary2


# In[39]:


np.append(ary2, [[5,5,5,5,5,5]], axis = 0)


# In[48]:


ary2


# In[50]:


np.append(ary2, [[5],[5],[5],[5]], axis = 1)


# In[ ]:





# In[42]:


a1 = np.array([5,5,5,5,5,5])


# In[43]:


a1


# In[44]:


a2 = np.array([[5,5,5,5,5,5]])


# In[45]:


a2


# In[46]:


a1.shape


# In[47]:


a2.shape


# ###  Delete

# In[52]:


ary1 = np.random.randint(10,20,(10,))


# In[53]:


ary1


# In[54]:


np.delete(ary1, 3, axis = None)


# In[55]:


ary1


# In[56]:


ary2


# In[58]:


a2 = np.insert(ary2, 2, 999, axis = 0)


# In[59]:


a2


# In[60]:


np.delete(a2,2, axis = 0)


# In[61]:


ary2


# In[62]:


np.delete(ary2, 3, axis = 1)


# ### Concatenate

# In[63]:


ary1


# In[64]:


a1


# In[66]:


ary2


# In[68]:


a2 = np.random.randint(10,50,(4,5))


# In[69]:


a2


# In[70]:


ary2


# In[77]:


np.concatenate((a2, ary2))  # default axis = 0


# In[76]:


np.concatenate((a2, ary2), axis = 0)


# In[75]:


np.concatenate((a2, ary2), axis = 1)


# In[78]:


a2.shape


# In[79]:


ary2.shape


# In[81]:


np1 = np.random.randint(10,20,(5,6))


# In[82]:


np2 = np.random.randint(20,40,(6,6))


# In[83]:


np3 = np.random.randint(40,60,(5,6))


# In[84]:


np1


# In[85]:


np2


# In[86]:


np3


# In[87]:


np1.shape


# In[88]:


np2.shape


# In[89]:


np.concatenate((np1, np2), axis = 0)


# In[90]:


np.concatenate((np1, np2), axis = 1)


# In[92]:


np.vstack((np1, np2))  #  concatenate with axis = 0


# In[94]:


np.hstack((np1, np2))  # concatenate with axis = 1


# In[95]:


np1.shape


# In[96]:


np3.shape


# In[97]:


np.concatenate((np1, np3), axis = 1)


# In[103]:


x = np.hstack((np1, np3))


# In[104]:


x


# ###  Split

# In[99]:


ary1


# In[100]:


ary1.size


# In[101]:


np.split(ary1, 2)


# In[102]:


np.split(ary1, 3)


# In[105]:


x


# In[108]:


np.split(x, 5, axis = 0)


# In[109]:


np.split(x,  6 ,axis = 1)


# In[110]:


np.split(x,  4 ,axis = 1)


# In[111]:


np.split(x,  3 ,axis = 1)


# In[113]:


np.vsplit(x, 2)  #  split with axis = 0


# In[114]:


np.vsplit(x, 5)  #  split with axis = 0


# In[116]:


np.hsplit(x, 4) # split with axis = 1


# ###  reshape

# In[118]:


ary1


# In[120]:


ary1.ndim


# In[122]:


ary1.size


# In[123]:


ary1.reshape(2,5)


# In[124]:


r1 = ary1.reshape(1,-1)


# In[125]:


r1


# In[126]:


ary1


# In[127]:


ary1.shape


# In[128]:


r1.shape


# In[129]:


ary1.ndim


# In[130]:


r1.ndim


# In[131]:


ary1.reshape(-1,1)


# In[132]:


ary1


# In[133]:


ary1.ndim


# In[135]:


ary1.reshape(1,-1)


# In[138]:


ary1.reshape(1,-1).ndim


# In[137]:


ary1.reshape(-1,1)


# In[139]:


ary1.reshape(-1,1).ndim


# ###  min, max, mean, std, unique

# In[140]:


ary1


# In[141]:


ary1.max()


# In[142]:


ary1.min()


# In[143]:


np.unique(ary1)


# In[145]:


np.unique(ary1, return_counts = True)


# In[146]:


x


# In[147]:


np.unique(x)


# In[148]:


np.unique(x, return_counts=True)


# In[149]:


import pandas as pd


# In[150]:


dfiris = pd.read_csv(r"C:\Users\hp\Desktop\DATASETS\Classification Dataset\Iris.csv")


# In[151]:


dfiris


# In[152]:


dfiris["Species"]


# In[153]:


dfiris["Species"].unique()


# In[154]:


dfiris["Species"].nunique()


# In[155]:


dfiris["Species"].value_counts()


# In[156]:


dfiris["Species"].value_counts().plot(kind ="bar")


# In[157]:


ary1


# In[158]:


ary1.mean()


# In[159]:


ary1.std()


# ###  expand dimension

# In[160]:


ary1


# In[162]:


np.expand_dims(ary1, axis = 0)


# In[163]:


np.expand_dims(ary1, axis = 1)


# In[164]:


ary2


# In[166]:


ary2.shape


# In[167]:


ary_expand = np.expand_dims(ary2, axis = 0)


# In[168]:


ary_expand


# In[169]:


ary_expand.shape


# In[170]:


ary_expand1 = np.expand_dims(ary2, axis = 1)


# In[171]:


ary_expand1.shape


# In[173]:


ary_seq1 = np.squeeze(ary_expand1)


# In[174]:


ary_seq1.shape


# In[175]:


a1


# In[180]:


a2 = np.array( [0,5,4,0,6,0,2,0,9] )


# In[181]:


a2


# In[182]:


np.count_nonzero(a2)


# In[184]:


a2.size


# In[183]:


np.argwhere(a2)


# In[185]:


ary2


# In[186]:


a2


# In[187]:


np.argmax(a2)


# In[190]:


a2[6] = 34


# In[191]:


a2


# In[192]:


np.argmax(a2)


# In[ ]:





# In[193]:


ary2


# In[194]:


np.argmax(ary2)


# In[196]:


ary2[2,2] = 455


# In[197]:


ary2


# In[198]:


np.argmax(ary2)


# In[199]:


np.argmin(ary2)


# In[200]:


ary2


# In[201]:


np.flip(ary2)


# In[205]:


ary2


# In[206]:


np.flip(ary2, axis = 0)


# In[207]:


ary2


# In[208]:


np.flip(ary2, axis = 1)


# In[210]:


ary2


# In[211]:


np.fliplr(ary2)


# In[213]:


ary2


# In[212]:


np.flipud(ary2)


# In[215]:


ary1


# In[216]:


s1 = np.random.randint(1,15,(10))


# In[217]:


s2 = np.random.randint(5, 20, (10))


# In[218]:


s1


# In[219]:


s2


# In[220]:


np.setdiff1d(s1, s2)


# In[221]:


np.setdiff1d(s2, s1)


# In[222]:


np.setxor1d(s1, s2)


# In[223]:


ary2


# In[225]:


np.savetxt("npary.txt", ary2)


# In[226]:


np.loadtxt("npary.txt")


# In[227]:


np.repeat(9, 5)


# In[228]:


np.repeat([11,22],5)


# In[229]:


np.equal(s1, s2)


# In[230]:


s1


# In[231]:


s2


# In[232]:


np.equal(s1,s1)


# In[233]:


dfiris


# In[234]:


dfiris.shape


# In[235]:


dfiris.ndim


# In[236]:


dfiris.size


# In[ ]:




