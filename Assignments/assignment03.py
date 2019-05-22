##
## File: assignment03.py (STAT 3250)
## Topic: Assignment 3
## Name: John Dunne (jd5an)
##

##  The questions in this assignment refer to the data in the
##  file 'absent.csv'.  The data contains 740 records from an
##  employer, with 21 columns of data for each record.  (There
##  are a few missing values indicated by zeros where zeros 
##  are clearly not appropriate.)  The file 'absent.pdf' has
##  a summary of the meanings for the variables.

##  Questions 1 and 2 can be completed without loops.  You should
##  try to do them this way, grading will take this into account.
import pandas as pd
import numpy as np
import csv
import math
#%%
data = pd.read_csv("absent.csv")
#%%
## 1.  All questions refer to the data set 'absent.csv'.

## 1(a) Find the mean absent time among all records.
data['Absenteeism time in hours'].mean()
'''
#1a
6.924324324324324
'''
## 1(b) Determine the number of records corresponding to
##      being absent on a Thursday.

data['Day of the week'].value_counts() #Displays the counts of all the days, Thursday = 6
'''
#1b

144
'''
## 1(c) Find the number of different employees represented in 
##      this data.
data['ID'].nunique()
"""
#1c

36
"""
## 1(d) Find the transportation expense for the employee with
##      ID = 34.
ID34 = data[(data['ID'] == 34)]

ID34['Transportation expense'].sum()
'''
#1d

6490
'''

## 1(e) Find the mean number of hours absent for the records
##      for employee ID = 11.
ID11 = data[(data['ID'] == 11)]
ID11['Absenteeism time in hours'].mean()
'''
#1e

11.25
'''
## 1(f) Find the mean number of hours absent for the records of those who 
##      have no pets, then do the same for those who have more than one pet.
NoPets = data[(data['Pet'] == 0)]
NoPets['Absenteeism time in hours'].mean()
havePets = data[(data['Pet'] > 0)]
havePets['Absenteeism time in hours'].mean()
'''
#1f

6.8283 = No Pets mean absence (hrs)
7.082142857 = With Pets mean absence time (hrs)
'''

## 1(g) Find the percentage of smokers among the records for absences that
##      exceeded 8 hours, then do the same for absences of no more then 4 hours.
absencesOver8 = data[(data['Absenteeism time in hours'] > 8)]
abscenceSmokers = absencesOver8[(absencesOver8['Social smoker'] ==1)]
(abscenceSmokers['ID'].nunique()/absencesOver8['ID'].nunique())*100 #percentage of smokers compared to overall population
absencesUnder4 = data[(data['Absenteeism time in hours'] < 4)]
abscenceSmokersUnder4 = absencesUnder4[(absencesUnder4['Social smoker'] ==1)]
(abscenceSmokersUnder4['ID'].nunique()/absencesUnder4['ID'].nunique())*100 #percentage of smokers compared to overall population
'''
#1g

19.047619047619047% = Over 8 hours
17.647058823529413% = Under 4 hours
'''
## 1(h) Repeat 1(g), this time for social drinkers in place of smokers.
DrabsencesOver8 = data[(data['Absenteeism time in hours'] > 8)]
abscenceDrinkers = DrabsencesOver8[(absencesOver8['Social drinker'] ==1)]
print((abscenceDrinkers['ID'].nunique()/DrabsencesOver8['ID'].nunique())*100) #percentage of drinkers compared to overall population
DrabsencesUnder4 = data[(data['Absenteeism time in hours'] < 4)]
abscenceDrinkersUnder4 = DrabsencesUnder4[(DrabsencesUnder4['Social smoker'] ==1)]
print((abscenceDrinkersUnder4['ID'].nunique()/DrabsencesUnder4['ID'].nunique())*100) #percentage of drinkers compared to overall population
'''
#1h

61.904761904761905% =  Social drinkers over 8 hours late
17.647058823529413% =  social drinkers less than 4 hours late
'''
#%%

## 2.  All questions refer to the data set 'absent.csv'.

## 2(a) Find the top-5 employee IDs in terms of total hours absent.  List
##      the IDs and corresponding total hours absent.
print(data.groupby(['ID'])["Absenteeism time in hours"].sum().sort_values(ascending=False))
'''
#2a

Top 5 absent IDs = 3, 14, 11, 28, 34
'''
## 2(b) Find the average hours absent per record for each day of the week.
##      Print out the day number and average.
print(data.groupby(['Day of the week'])["Absenteeism time in hours"].mean())
'''
#2b

2    9.248447
3    7.980519
4    7.147436
5    4.424000
6    5.125000
'''
## 2(c) Repeat 2(b) replacing day of the week with month.
#print(data.groupby(['Month of absence'])["Absenteeism time in hours"].mean())
'''
#2c
0      0.000000
1      4.440000
2      4.083333
3      8.793103
4      9.094340
5      6.250000
6      7.611111
7     10.955224
8      5.333333
9      5.509434
10     4.915493
11     7.507937
12     8.448980
'''
## 2(d) Find the top 3 most common reasons for absence for the social smokers,  
##      then do the same for the non-smokers. (If there is a tie for 3rd place,
##      include all that tied for that position.
socialSmokers = data[(data['Social smoker'] == 1)] #Gives only smoker data
socialSmokers['Reason for absence'].value_counts(ascending=False) #Prints out the reason number and quantity of the reason given for smokers absences
NotsocialSmokers = data[(data['Social smoker'] == 0)] #Gives only nonsmoker data
NotsocialSmokers['Reason for absence'].value_counts(ascending=False) #Prints out the reason number and quantity of the reason given for Nonsmokers absences
'''
#2d
Smokers:
Reason|Number
    0     8
    25    7
    19    4
    18    4
    28    4
    22    4
    23    4
NonSmokers:
Reason|Number
23    145
28    108
27     69
'''
## 2(e) Suppose that we consider our data set as a sample from a much
##      larger population.  Find a 95% confidence interval for the 
##      proportion of the records that are from social drinkers.  Use
##      the formula 
##
##  [phat - 1.96*sqrt(phat*(1-phat)/n), phat + 1.96*sqrt(phat*(1-phat)/n)]
##
## where "phat" is the sample proportion and "n" is the sample size.

socialDrinker = data[(data['Social drinker'] == 1)] #isolates social drinker records
n = data['ID'].count() #finds  total records sample size
phat = socialDrinker['ID'].count()/data['ID'].count() #finds ratio of social drinker records to total records
lowerInterval = phat - 1.96*math.sqrt(phat*(1-phat)/n)
upperInterval = phat + 1.96*math.sqrt(phat*(1-phat)/n)

'''
#2e
[0.5318725067607831, 0.603262628374352]
(0.5675675675675675-0.5318725067607831) = Lower interval
(0.5675675675675675+0.603262628374352) = Upper interval
'''
#%%
## 3.  For this problem we return to simulations one more time.  Our
##     topic is "bias" of estimators, more specifically the "percentage
##     relative bias" (PRB) which we take to be
##
##        100*((mean of estimated values) - (exact value))/(exact value)
##
##     For instance, to approximate the bias of the sample mean in 
##     estimating the population mean, we would computer
##
##        100*((mean of sample means) - (population mean))/(population mean)
##
##     For estimators that are "unbiased" we expect that the average
##     value of all the estimates will be close to the value of the
##     quantity being estimated.  In these problems we will approximate
##     the degree of bias (or lack of) by simulating.  In all parts we
##     will be sampling from a population of 10,000,000 values randomly
##     generated from an exponential distribution with scale = 10 using
##     the code below.

pop = np.random.exponential(scale = 10, size = 10000000)

## 3(a) Compute and report the mean for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample mean for each of the samples,
##      compute the mean of the sample means, and then compute the PRB.
pop.mean()
samparray = np.zeros(100000)
for sim in range(100000): #loops 100,000 times, randomly taking samples of size 10 from pop, finding their mean,then adding that mean to an arra
    sample = np.random.choice(pop, size=10)
    sampleMean = sample.mean() #computes sample mean
    samparray[sim] = sampleMean
meanofsamplemeans = samparray.mean() #finds the mean of the sample means
PRB = 100*((meanofsamplemeans) - pop.mean())/(pop.mean()) #PRB formula
#print(PRB, 'mean PRB')
'''
#3a
mean for pop = 9.997205556302264
0.0028396626303007276
'''
## 3(b) Compute and report the variance for all of "pop" using "np.var(pop)".  
##      Simulate 100,000 samples of size 10, then compute the sample variance 
##      for each sample using "np.var(samp)" (where "samp" = sample).  Compute 
##      the mean of the sample variances, and then compute the PRB.
##      Note: Here we are using the population variance formula on the samples
##      in order to estimate the population variance.  This should produce
##      bias, so expect something nonzero for the PRB.
np.var(pop)
samparray = np.zeros(100000)
for sim in range(100000): 
    samp = np.random.choice(pop, size=10)
    sampleVariance= np.var(samp)
    samparray[sim] = sampleVariance
meanofsampleVariances= samparray.mean() #finds the mean of the sample means
PRB = 100*((meanofsampleVariances) - np.var(pop))/(np.var(pop))
#print(PRB, 'First variance PRB')
'''
#3b
np.var(pop) = 99.92172310117115
-10.520631491196692 = PRB
'''
## 3(c) Repeat 3(b), but this time use "np.var(samp, ddof=1)" to compute the
##      sample variances.  (Don't change "np.var(pop)" when computing the
##      population variance.)
np.var(pop)
samparray = np.zeros(100000)
for sim in range(100000): 
    samp = np.random.choice(pop, size=10)
    sampleVariance= np.var(samp, ddof=1)
    samparray[sim] = sampleVariance
meanofsampleVariances= samparray.mean() #finds the mean of the sample means
PRB = 100*((meanofsampleVariances) - np.var(pop))/(np.var(pop))
#print(PRB, 'Second variance PRB')
'''
#3c
-0.31160670085339365 = PRB
'''
## 3(d) Compute and report the median for all of "pop".  Simulate 100,000
##      samples of size 10, compute the sample median for each of the samples,
##      compute the mean of the sample medians, and then compute the PRB.
##      Note: For nonsymmetric distributions (such as the exponential) the
##      sample median is a biased estimator for the population median.  The
##      bias gets decreases with larger samples, but should be evident with 
##      samples of size 10.
print(np.median(pop))
samparray = np.zeros(100000)
for sim in range(100000): 
    samp = np.random.choice(pop, size=10)
    sampleMedian= np.median(samp) #finds median of the sample
    samparray[sim] = sampleMedian #adds median to array
meanofsamplemedian= samparray.mean() #finds mean of the median array
PRB = 100*((meanofsamplemedian) - np.median(pop))/(np.median(pop))
print(PRB, "PRB median")
'''
#3d
6.934521077938933 = median of pop
7.605631028566901 = PRB
'''

