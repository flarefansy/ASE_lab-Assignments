# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 15:51:35 2017

@author: Spencersun
"""

import csv
import numpy as np
import matplotlib.pyplot as plt
import random

def csvfile():
    list_file = []
    with open('Customers.csv','r') as csv_file:  
        all_lines=csv.reader(csv_file)
        for one_line in all_lines:  
            list_file.append(one_line)
    x = [row[3] for row in list_file[1:]]
    y = [row[4] for row in list_file[1:]]
    return x,y

def cluster_content(X, mu):
    cluster = {}
    for x in X:
        value = min([(i[0],np.linalg.norm(x - mu[i[0]]))for i in enumerate(mu)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster

def new_center(mu, cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(newmu, oldmu):
    return (set([tuple(a)for a in newmu]) == set([tuple(a)for a in oldmu]))

def Apply_Kmeans(X, K, N):
    temp1 = np.random.randint(N, size = K)
    oldmu = np.array([X[i]for i in temp1])
    temp2 = np.random.randint(N, size=K)
    newmu = np.array([X[i] for i in temp2])
    cluster = cluster_content(X, oldmu)
    itr = 0
    plot_cluster(oldmu,cluster,itr)
    while not matched(newmu, oldmu):
        itr = itr + 1
        oldmu = newmu
        cluster = cluster_content(X,newmu)
        plot_cluster(newmu, cluster,itr)
        newmu = new_center(newmu, cluster)
    plot_cluster(newmu, cluster, itr)
    return

def plot_cluster(mu,cluster, itr):
    plt.ylabel ('Spending Score (1-100)')
    plt.xlabel ('Annual Income (k$)')
    plt.title('Clusters of customers')
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'o', c = 'y', s = 150, linewidths = 10, zorder = 10, label = 'Centroids')
    plt.show()

def Simulate_Clusters():
    K = 5
    list_file = []
    with open('Customers.csv','r') as csv_file:  
        all_lines=csv.reader(csv_file)
        for one_line in all_lines:  
            list_file.append(one_line)
    X = np.zeros((len(list_file[1:]),2))
    X[:, 0] = [row[3] for row in list_file[1:]]
    X[:, 1] = [row[4] for row in list_file[1:]]
    #X = np.array(x,y)
    plt.scatter(X[:, 0], X[:, 1])
    N=10
    plt.show()
    temp = Apply_Kmeans(X, K, N)

if __name__ == '__main__':
    Simulate_Clusters()
    

    

