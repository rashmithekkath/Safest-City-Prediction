# -*- coding: utf-8 -*-
"""
Created on Tue May 19 21:35:20 2020

@author: Rashmi Dinesh Thekkath
"""

#TO FIND NEARBY AREAS [ALGO STEP 1- CLUSTERING BASED ON LATITUDE AND LONGITUDE]

import pandas as pd
df=pd.read_csv('ind_cities_loc.csv')

df=df.sample(frac=1)
df.head(15)
df.dropna(axis=0,how='any',subset=['Latitude','Longitude'],inplace=True)
X=df.loc[:,['City_num','Latitude','Longitude']]
X.head(10)

from sklearn.cluster import KMeans
K_clusters = range(1,10)
kmeans = [KMeans(n_clusters=i) for i in K_clusters]
Y_axis = df[['Latitude']]
X_axis = df[['Longitude']]
score = [kmeans[i].fit(Y_axis).score(Y_axis) for i in range(len(kmeans))]
score


import matplotlib.pyplot as plt


kmeans = KMeans(n_clusters = 20, init ='k-means++')
kmeans.fit(X[X.columns[1:3]]) # Compute k-means clustering.
X['cluster_label'] = kmeans.fit_predict(X[X.columns[1:3]])
centers = kmeans.cluster_centers_ # Coordinates of cluster centers.
labels = kmeans.predict(X[X.columns[1:3]]) # Labels of each point
X.head(10)
X.plot.scatter(x ='Latitude', y = 'Longitude', c=labels, s=50, cmap='viridis')
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)
X = X[['City_num','cluster_label']]
X.head(5)

clustered_data = df.merge(X, left_on='City_num', right_on='City_num')
clustered_data['cluster'] = kmeans.labels_
clustered_data[clustered_data.cluster==3]
centers = kmeans.cluster_centers_
print(centers)
  
#my_location=str(input())
#for i in range(0,20,1):
 #   if (clustered_data['City']==my_location):
    #if my_location in clustered_data['City'][clustered_data.cluster==i]:
  #      print(clustered_data[clustered_data.cluster==i])
        
        
#ALGORITHM PART2-ML MODEL ON CLUSTERED DATA TO FIND BEST SUITED PLACE

import pandas as pd
filename='update_list.csv'
pdf=pd.read_csv(filename)
pdf=pdf.sample(frac=1)
pdf.head()

from sklearn.datasets import make_blobs
from sklearn import preprocessing 
def createDataPoints(centroidLocation, numSamples, clusterDeviation):
    # Create random data and store in feature matrix X and response vector y.
    X, y = make_blobs(n_samples=numSamples, centers=centroidLocation, 
                                cluster_std=clusterDeviation)
    # Standardize features by removing the mean and scaling to unit variance
    X = preprocessing.StandardScaler().fit_transform(X)
    return X, y
X, y = createDataPoints(pdf[['Value.active','Value.confirmed','Value.deaths','Value.recovered']], 1500, 0.5)

#DBSCAN
our_df=pdf[['Value.active','Value.confirmed','Value.deaths','Value.recovered']]
our_df.head()
#our_df=StandardScaler().fit_transform(our_df)

loc_for_merge=clustered_data[['City','State','cluster_label']]
loc_for_merge.head(5)

my_population=pd.read_csv('cities_r2.csv')
population_merge=pd.merge(loc_for_merge,my_population,on='City')

stats_for_merge=pdf[['State','Value.active','Value.confirmed','Value.deaths','Value.recovered']]
stats_for_merge.head(5)

for_model=pd.merge(population_merge,stats_for_merge,on='State')
for_model

mylist=[]
for ind in for_model.index: 
    if(for_model['City'][ind].strip()==input('Your City Name: ').strip()):
                factor_one=((for_model['Value.deaths'][ind])/(for_model['Value.confirmed'][ind]))
                factor_two=((for_model['Value.deaths'][ind])/(for_model['Population'][ind]))**2
                factor=float(1/(factor_one*factor_two))
                mylist.append(factor)
                print(factor)
                break
    else:
        print('Try submitting another nearby city name.')
        continue
