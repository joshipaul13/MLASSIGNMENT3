#!/usr/bin/env python
# coding: utf-8

# In[1]:


#1. Numpy:
# Using NumPy create random vector of size 15 having only Integers in the range 1-20.
import numpy as np
x = np.random.randint(1,20, size = 15)
print (x)


# In[2]:


# 1. Reshape the array to 3 by 5
y=x.reshape(3,5)
print(y)


# In[3]:


# 2. Print array shape.
print("array is :",y)
print ("array shape is:",y.shape)


# In[4]:


# 3. Replace the max in each row by 0
new_a = np.where(y == [
    [i]
    for i in np.amax(y, axis = 1)
], 0, y)

print(new_a)


# In[5]:


# Create a 2-dimensional array of size 4 x 3 (composed of 4-byte integer elements), also print the shape, type and data type
#of the array.
import numpy as np

# create a 2-dimensional array of size 4x3
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], dtype=np.int32)

# print the array shape
print("Array shape:", arr.shape)

# print the array type
print("Array type:", type(arr))

# print the array data type
print("Array data type:", arr.dtype)


# In[6]:


#1(b) Write a program to compute the eigenvalues and right eigenvectors
import numpy as np

# define the square array
A = np.array([[3, -2], [1, 0]])

# compute the eigenvalues and right eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# print the eigenvalues and right eigenvectors
print("Eigenvalues:", eigenvalues)
print("Right eigenvectors:")
print(eigenvectors)


# In[7]:


#1(c)Compute the sum of the diagonal element of a given array.
import numpy as np

# define the array
A = np.array([[0, 1, 2], [3, 4, 5]])

# compute the sum of the diagonal elements
diagonal_sum = np.trace(A)

# print the sum of the diagonal elements
print("Sum of diagonal elements:", diagonal_sum)


# In[8]:


#1(d)Write a NumPy program to create a new shape to an array without changing its data. 
import numpy as np

# define the original array
arr = np.array([[1, 2], [3, 4], [5, 6]])

# reshape to 3x2
arr_3x2 = arr.reshape(3, 2)

# reshape to 2x3
arr_2x3 = arr.reshape(2, 3)

print("Reshaped to 3x2:\n", arr_3x2)
print("Reshaped to 2x3:\n", arr_2x3)


# In[9]:


#Question2 Write a Python programming to create a below chart of the popularity of programming Languages.
import matplotlib.pyplot as plt
# Data to plot
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popuratity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
# explode 1st slice
explode = (0.1, 0, 0, 0,0,0)  
# Plot
plt.pie(popuratity, explode=explode, labels=languages, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.show()


# In[ ]:




