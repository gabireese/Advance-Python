#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd, numpy as np, matplotlib.pyplot as plt, seaborn as sns


# In[ ]:


##Task 1##


# In[10]:


##Creating a fibonacci sequence
def gen_Fibonacci(X):
    fib_seq = [0, 1]
    while len(fib_seq) < X:
        next_fib = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_fib)
    return np.array(fib_seq[:X])

##Creating a numpy array w/ the 20 fib. numbers

X = 20

fib_num = gen_Fibonacci(X)

##Recreating the arrays from second assignment using the fib. array

second_list = np.concatenate((np.array([1]), fib_num[1:] / fib_num[:-1]))
third_list = np.concatenate((np.array([0, 0]), np.diff(second_list)))

##Plotting all series into a graph

plt.figure(figsize= (15,15))

plt.plot(fib_num, label = "Fibonacci Sequence")

plt.plot(second_list, label = "Fibonacci Sequence 2")

plt.plot(third_list, label = "Fibonacci Sequence 3")

plt.xlabel("Position of the the values from the Sequence")

plt.ylabel("Values in the Sequence")

plt.legend()

plt.title("Visualization of Fibonacci Sequences")

plt.show()


# In[80]:


##Task 2


# In[25]:


##Loading and concatinating data

training_data = pd.read_csv("/Users/gabi_reese/Downloads/archive(1)/tit_train.csv")

test_data = pd.read_csv("/Users/gabi_reese/Downloads/archive(1)/tit_test.csv")

merged_data = pd.concat([training_data, test_data])

##Getting statistical summary of the data

merged_data.describe()

##Creating a histogram of age distribution 

plt.hist(merged_data['Age'], bins = 10)

plt.xlabel("Age")

plt.ylabel("Frequency")

plt.title("Age Distribution of Passengers on Titanic")


plt.show()


# In[40]:


## Histogram of the Age of Passengers Segregated from Titanic

sns.histplot(merged_data[merged_data['Survived']==1]['Age'], bins = 20, label = 'Survived', color ='blue')

sns.histplot(merged_data[merged_data['Survived']==0]['Age'], bins = 20, label = 'Not Survived', color = 'red')

plt.xlabel('Age')
plt.ylabel('Frequency')

plt.title('Age Distribution of Passengers that Survived vs. Did not Survive on Titanic')

plt.tight_layout()
plt.show()


# In[ ]:





# In[55]:


##Calculating survival percentages

total_passengers = merged_data.shape[0]

survival_rate = (merged_data['Survived'].sum()/total_passengers)*100

print('The survival rate:', survival_rate)

##Creating a bar chart of the survival rate

plt.bar(['Survived', 'Not Survived'], [survival_rate, 100 - survival_rate], color=['blue', 'red'])
plt.ylabel('Percentage')
plt.title('Survival rate on the Titanic')
plt.show()


# In[59]:


##Creating a bar chart of survival rate grouped by gender
survival_gender = merged_data.groupby('Sex')['Survived'].mean()*100

plt.figure(figsize=(8, 6))
sns.barplot(x=survival_gender.index, y=survival_gender)

plt.title('Survival Percentage by Gender')
plt.show()


# In[75]:


##Creating boxplot
fig, axes = plt.subplots(1, 2, figsize=(12, 6))

# Boxplot of survival vs passenger class
sns.boxplot(x='Pclass', y='Age', data=merged_data, hue='Survived', palette= 'flare', ax=axes[0])
axes[0].set_ylabel('Age')
axes[0].set_title('Age Distribution by Passenger Class and Survival')

# Boxplot for survival vs passenger class segregated by sex
sns.boxplot(x='Pclass', y='Age', data=merged_data, hue='Sex', palette = 'rocket', ax=axes[1])
axes[1].set_ylabel('Age')
axes[1].set_title('Age Distribution by Passenger Class and Sex')

plt.tight_layout()
plt.show()


# # Part G
# 
# 
#  Based on the visualizations created in prevoius parts of my code, I will be discussing the bar graph and the histogram.
#  Looking at the histogram, my first histogram shows the age distribution of passengers on the titanic, and I discovered that the majority of passergers on the titanic were around the age of 18-30. Also based on the histogram is right skewed an not normally distributed.
#  Looking at the bar graph grouped by gender, I found that women had a higher survival rate then men did during the events of the titanic. 
# 
# 
# 
# 
# 

# In[ ]:




