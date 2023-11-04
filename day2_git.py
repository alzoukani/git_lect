#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Hello World")


# In[2]:


print(Hello World)


# ### integers

# In[3]:


1


# In[4]:


343


# In[5]:


6756756


# In[6]:


print(78)


# ## FLOATS: decimal value

# In[7]:


7.0


# In[8]:


7


# In[9]:


print(7.6)


# In[10]:


type(7)


# In[11]:


type(7.0)


# ## strings:
# 
#  " ", ''

# In[13]:


"porosity"


# In[14]:


'porosity'


# In[15]:


type("porosity")


# In[16]:


"@##$(@#$()@*&*(@#(043nxmknx,mcn,mnsknds)))"


# In[17]:


"7"


# In[18]:


type(7)


# In[19]:


type(7.0)


# In[20]:


type("7")


# In[21]:


"97897+93493"


# ## Booleans

# In[22]:


8>2


# In[23]:


True


# In[24]:


False


# In[25]:


type(True)


# ## Mathematical Operations

# In[26]:


55+44


# In[27]:


55*2


# In[28]:


23-12


# In[29]:


55/2


# In[30]:


10/2


# In[31]:


10.0+5


# In[32]:


10+5


# In[33]:


5**3


# In[34]:


# * for multiplication, ** for exponential power

print(5*2)
print(5**2)


# In[35]:


31/5


# In[36]:


31//5


# In[37]:


31%5


# In[38]:


# string


# In[39]:


"55+22"


# In[40]:


"55"+"33"


# In[42]:


"Hello"+" All"


# In[43]:


"5"*3


# In[44]:


"5"+"5"+"5"


# In[45]:


"petroleum "*3


# In[46]:


## booleans


# In[47]:


78>56


# In[48]:


78<56


# In[49]:


55==55


# In[50]:


55==65


# In[51]:


56>23 


# In[52]:


25<45


# In[56]:


56>23 and 25<45


# In[55]:


56>23 and 25<20


# In[57]:


43>23


# In[58]:


45<21


# In[60]:


43<23 or 45<21


# ## Variables:
# 
# - Containers for storing informations
# 
# - variables are created "="
# 
# - for a given runtime

# In[61]:


porosity = 20


# In[62]:


porosity


# In[64]:


"hello"


# In[65]:


porosity==45


# In[67]:


b = "Petroleum"


# In[68]:


b


# In[69]:


type(b)


# In[4]:


#reintialise
b = "porosity"


# In[5]:


b


# In[6]:


b


# ### Variable names cannot start with a number or special character, ie 2,3,4,@#
# 
# 
# ### Variable name doesnot have any space in between two characters, but underscore can be used

# In[7]:


1a = 45


# In[8]:


a1 = 45


# In[9]:


a1 


# In[10]:


@a = 43


# In[11]:


_a = 45


# In[12]:


_a


# In[13]:


porosity 1 = 45


# In[14]:


poosity_1 = 45


# In[15]:


poosity_1


# In[16]:


poro_1 = 20
poro_2 = 10 


# In[17]:


poro_1+poro_2


# In[18]:


poro_1-poro_2


# In[19]:


poro_1/poro_2


# In[26]:


a = "Hello "
b = 3


# In[23]:


a*3


# In[27]:


a,b = "Hello",3


# In[28]:


a


# In[29]:


b


# ## input = taking input from user
# 
# - takes input in for of strings

# In[30]:


input()


# In[31]:


perm = input()


# In[32]:


perm


# In[33]:


type(perm)


# In[34]:


perm = input("Enter the formation's permeability: ")


# In[35]:


perm


# In[36]:


perm/2


# ## type conversions

# In[37]:


perm


# In[38]:


type(perm)


# In[39]:


float(perm)


# In[40]:


type(perm)


# In[41]:


perm


# In[42]:


perm = float(perm)


# In[43]:


type(perm)


# In[44]:


perm


# In[45]:


a = 3


# In[46]:


type(a)


# In[47]:


str(a)


# In[48]:


a = str(a)


# In[49]:


a


# In[50]:


float(a)


# In[51]:


a = 'petroleum'


# In[52]:


a


# In[53]:


float(a)


# In[54]:


a= 6.5


# In[55]:


int(a)


# In[56]:


int(6.7)


# In[57]:


permeability = float(input("Enter the formation's permeability: "))


# In[58]:


permeability


# In[60]:


type(permeability)


# ## String Formatting

# In[71]:


permeability = float(input("Enter the formation's permeability: "))
porosity = float(input("Enter the formation's porosity: "))
print(f"Formation Porosity is {porosity*100}, and permeability is {permeability} md, and product of both is {porosity*permeability}")


# In[67]:


print("Formation Porosity is {}, and permeability is {} md".format(porosity,permeability))


# In[68]:


print("Formation porosity is ", porosity, "and permeability is ", permeability)


# In[1]:


weather = "rainy"
weather2="very cloudy"

f"today is a very sunny day"


# In[2]:


f"today is a {weather} day"


# In[3]:


f"today is a {weather} and {weather2} day"


# In[4]:


perm=[2,5,77,[44,66,81,10], 43,33]


# In[5]:


perm


# In[6]:


perm[3]


# In[7]:


perm[3][2]


# In[8]:


len[perm]


# In[9]:


len(perm)


# In[10]:


perm[-1]


# In[11]:


perm


# In[12]:


perm[2]="Ahmad"


# In[13]:


perm


# In[14]:


# append to add element to the list
perm.append(99)


# In[15]:


perm


# # Slicing : accessing more than one data
# list[start, stop, step]
# stopping index is always EXECLUDED, meaning: in any slicing process, always increase 1 more, because python will excelude it and hence you get exactly the last value you want in slicing. In negative slicing, do vise versa. 
# (I noticed that when we use step size, the last index is included?!

# In[16]:


# if we want to slice perm between Ahmad (which is index 2), and 33 (which is index 5), increase 1 to the last index:
perm[2:6]


# In[17]:


perm[1:300]


# In[18]:


perm[1:]


# In[25]:


perm
perm[:3]


# In[20]:


perm[:100]


# In[24]:


perm


# In[26]:


perm[:]


# In[27]:


perm[::]


# In[28]:


perm[::2]


# In[30]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']


# In[31]:


li


# In[42]:


li[6][3][ -4: :-2]


# In[5]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']


# In[6]:


li


# In[7]:


li[6]


# In[32]:


li[6][3][-4::-2]


# In[33]:


li = [34,34,23,'saturation',True,6.7,[34,565,74,[98695,545,'ghery',["getme"],345,34],3,'str'],'jfdj']
# Get ghery, 98695

li[6]


# In[34]:


li[6][3]


# In[55]:


li[6][3][2::-2]
# we don't put (0) as stop point because stop point will be excluded then you end up having only 'ghery'. so keep 
#the stop point open. 


# In[39]:


li[6][3][-4::-2]


# In[53]:


li[6][3][-4::-2]


# # Tuples: 
# # Class#4, Sunday 9-Sep. 2023

# In[ ]:




