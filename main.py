#importing Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st
import numpy as np
from matplotlib.patches import Circle
import os
import sys

#Getting the sample data 100_samples.csv file
# data = pd.read_csv(os.getcwd()+"\\" + sys.argv[1]) 
data = pd.read_csv('100_samples.csv') 


# Part1 - Analysis 
#Calculating the range, mean, mode, Standard Deviation, Median of the attributes present in the dataset except for Country
analysis=data.drop('Country', axis=1)
columns= analysis.columns.tolist()
metrics={}
for i in columns[1:]:
   metrics[i]= [[analysis[i].max(), analysis[i].min()], analysis[i].mean(), st.mode(analysis[i].tolist()), analysis[i].std(), analysis[i].median()]

print(pd.DataFrame(metrics, index=["Range","Mean", "Mode", "Standard Deviation","Median"]))



#Part2 - Visualization

#a. Pie Chart
data0=data.loc[data['Severity_Mild'].isin([1])]
data1=data.loc[data['Severity_Moderate'].isin([1])]
data2=data.loc[data['Severity_Severe'].isin([1])]
c0=data0['Severity_Mild'].count()
c1=data1['Severity_Moderate'].count()
c2=data2['Severity_Severe'].count()
labels = 'Severity_Mild',  'Severity_Moderate', 'Severity_Severe'
sizes = [c0, c1, c2]
explode = (0.1, 0, 0)
plt.pie(sizes,  labels=labels, autopct='%1.1f%%', explode=explode )
plt.title("Pie Chart for visualizing the severity of the patients present in the dataset ")
plt.show()


# b. Polar Chart
polar = data
#Considering the following Columns used for Polar Chart
cols = ['Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+', 'Gender_Female', 'Gender_Male']
#Age Categories
ages = ['Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+']
polar=polar[cols]

#Declaration of 2 lists
men=[]
women=[]

for i in range(len(cols)- 2):
  #Counting the number of Men in the following age categories 'Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+'
  m =polar.loc[(polar[cols[i]] == 1) & (polar[cols[5]] == 1)] 
  #Counting the number of Women in the following age categories 'Age_0-9', 'Age_10-19', 'Age_20-24', 'Age_25-59', 'Age_60+'
  n =polar.loc[(polar[cols[i]] == 1) & (polar[cols[6]] == 1)] 
  men.append(m[cols[i]].count()) 
  women.append(n[cols[i]].count()) 
    
#Plotting Polar Chart
fig, ax = plt.subplots(figsize=(12, 7), subplot_kw=dict(polar=True))
ax.bar(ages, women, label='Women', alpha=0.8)
ax.bar(ages, men, label='Men', alpha=0.8)
ax.tick_params(labelleft='Off', left='Off')
l = ax.legend(loc='upper left')
l.set_bbox_to_anchor((0, 0))
l.set_title("Polar Chart of all Age Categories against Men and Women")


#c. Donut Chart
donut_chart = pd.DataFrame(
    {'Age': ages,
     'Men': men,
     'Women': women
    })

fig, ax = plt.subplots()
donut_chart.plot.pie(y='Women', labels=donut_chart.Age, autopct='%1.1f%%', ax=ax)
ax.legend_.set_visible(False)
ax.set_xlabel('Donut Chart to display number of Women under each Age Category')
circle = Circle((0,0), 0.75, facecolor='white')
ax.add_artist(circle)


#d. Heatmap
plt.figure(figsize=[30, 10])
sns.heatmap(data.corr(), annot=True, linewidths=1, vmin=-1, cmap="RdBu_r")
plt.title("Correlation Matrix")
plt.show()



#e. Bar Chart
fig, ax = plt.subplots(figsize=(15,5))
men = ax.bar(donut_chart.Age, 'Men', data=donut_chart, label='Men %')
women = ax.bar(donut_chart.Age, 'Women', data=donut_chart, label='Women %')
ax.legend()
ax.set_title("Bar Chart for Visualizing the data of Men and Women across all Age Categories")
plt.show()



#f. Count Plot

#f1 Count Plot for Country
fig, axes = plt.subplots(figsize=(12,12))
sns.countplot(y='Country', data=data)
plt.title("Count Plot for Country")
plt.show()

#f2 Count Plot for Country vs Fever Symptom
fig, axes = plt.subplots(figsize=(13, 13))
sns.countplot(x='Country', data=data, hue='Fever')
plt.title("Count Plot for Country vs Fever Symptom")
plt.show()

#f3 Count Plot for Country vs None Experiencing Symptom
fig, axes = plt.subplots(figsize=(13, 13))
sns.countplot(x='Country', data=data, hue='None_Experiencing')
plt.title("Count Plot for Country vs None Experiencing Symptom")
plt.show()