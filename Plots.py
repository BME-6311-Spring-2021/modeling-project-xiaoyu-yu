# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:00:04 2021

@author: Xiaoyu Yu
"""
import numpy as np
from matplotlib import pyplot as plt
import pandas
from scipy import stats
address1 = r'D:\UVA Phd\BME6311\Project\M1-10 M2-100.csv'
address2 = r'D:\UVA Phd\BME6311\Project\M1-100 M2-10.csv'
address3 = r'D:\UVA Phd\BME6311\Project\M1-100 M2-100.csv'
data1 = pandas.read_csv(address1)
data2 = pandas.read_csv(address2)
data3 = pandas.read_csv(address3)
data1 = data1.values
data2 = data2.values
data3 = data3.values
plt.close('all')
M1_10 = [144, 125, 124, 119, 164, 142, 123]
M1_30 = [104, 100, 106, 109, 113, 111, 107]
M2_10 = [69, 72, 69, 74, 76, 77, 67]
M2_30 = [73, 75, 75, 78, 76, 82, 73]
control = [81, 76, 83, 81, 83, 80, 84]

M1 = [np.mean(M1_10), np.mean(M1_30)]
M1error = [np.std(M1_10), np.std(M1_30)]
M2 = [np.mean(M2_30), np.mean(M2_10)]
M2error = [np.std(M2_30), np.std(M2_10)]
controlMean = np.mean(control)
controlerror = np.std(control)

fig, ax = plt.subplots()
wid = 0.3
ax.bar(np.asarray([0.8, 1.2]), M1, yerr = M1error, align='center', alpha=0.8, ecolor='black', capsize=5, width = wid, color = 'red')
ax.bar(np.asarray([2.8, 3.2]), M2, yerr = M2error, align='center', alpha=0.8, ecolor='black', capsize=5, width = wid, color = 'green')
ax.bar(2, controlMean, yerr = controlerror, align='center', alpha=0.8, ecolor='black', capsize=5, width = wid)
plt.xticks(np.asarray([0.8, 1.2,2, 2.8, 3.2]), ('90%', '70%','control', '90%', '70%', ))
plt.xlabel('Inhibition rate(%)')
plt.ylabel('Bacteria clearnce time(h)')
plt.ylim([0, 180])
plt.legend(['M1-macrophage','M2-macrophage', 'Control'])

plt.figure(figsize=(8, 4), dpi=80)
plt.plot(data1[:, 0], color = 'black')
plt.plot(data1[:, 1], color = 'orange')
plt.plot(data1[:, 2], color = 'red')
plt.plot(data1[:, 3], color = 'green')
plt.ylabel('number of cells')
plt.xlabel('Time(h)')
plt.legend(['Bacteria', 'Neutrophil', 'M1-macrophage', 'M2-macrophage'])
plt.title('M1-macrophage inibit 90%')

plt.figure(figsize=(8, 4), dpi=80)
plt.plot(data2[:, 0], color = 'black')
plt.plot(data2[:, 1], color = 'orange')
plt.plot(data2[:, 2], color = 'red')
plt.plot(data2[:, 3], color = 'green')
plt.ylabel('number of cells')
plt.xlabel('Time(h)')
plt.legend(['Bacteria', 'Neutrophil', 'M1-macrophage', 'M2-macrophage'])
plt.title('M2-macrophage inibit 90%')

plt.figure(figsize=(8, 4), dpi=80)
plt.plot(data3[:, 0], color = 'black')
plt.plot(data3[:, 1], color = 'orange')
plt.plot(data3[:, 2], color = 'red')
plt.plot(data3[:, 3], color = 'green')
plt.ylabel('number of cells')
plt.xlabel('Time(h)')
plt.legend(['Bacteria', 'Neutrophil', 'M1-macrophage', 'M2-macrophage'])
plt.title('Control(No inhibition)')

stats1, pValue1 = stats.ttest_ind(np.asarray(M1_10), np.asarray(M1_30))
stats2, pValue2 = stats.ttest_ind(np.asarray(M2_10), np.asarray(M2_30))
stats3, pValue3 = stats.ttest_ind(np.asarray(M1_30), np.asarray(control))
stats4, pValue4 = stats.ttest_ind(np.asarray(M2_30), np.asarray(control))