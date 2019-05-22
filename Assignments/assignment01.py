##
## File: assignment01.py (STAT 3250)
## Topic: Assignment 1
## Name: John Dunne

## 1.  For the questions in this part, use the following
##     lists as needed:
list01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
list02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1,0,5]
list03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = list01 + list02 + list03
#%%
## (a) Find the product of the last four elements of list02.
productoflastfour = list02[-1]*list02[-2]*list02[-3]*list02[-4] #The product of the specified indices
print(productoflastfour)
"""
## 1a

0               #The product
"""
#%%
## (b) Extract the sublist of list01 that goes from
##     the 3rd to the 11th elements (inclusive).
sublist01 = list01[2:11] #Makes a new list from containing 3rd to (and including) 11th element of list01.
print(sublist01)
"""
## 1b

[4, 9, 10, -3, 5, 5, 3, -8, 0]
"""
#%%
## (c) Concatenate list01 and list03 (in that order), sort
##     the combined list, then extract the sublist that 
##     goes from the 5th to the 15th elements (inclusive).
list0103 = list01+list03 #Adds list 01 and 03 together
list0103.sort() #sorts the newly formed list
sortedlist0103 = list0103[4:15] #Makes new list containing 5th to 15th element from the previously sorted list.
print(sortedlist0103)
"""
## 1c

[-3, -2, -2, -2, 0, 0, 0, 0, 0, 2, 2]
"""

#%%
## (d) Generate "biglist", then extract the sublist of every 4th 
##     element starting with the 3rd element
list01 = [2,5,4,9,10,-3,5,5,3,-8,0,2,3,8,8,-2,-4,0,6]
list02 = [-7,-3,8,-5,-5,-2,4,6,7,5,9,10,2,13,-12,-4,1,0,5]
list03 = [2,-5,6,7,-2,-3,0,3,0,2,8,7,9,2,0,-2,5,5,6]
biglist = list01 + list02 + list03
biglistindex = 1 #Indices counter, I decided to start from 2nd element for the while loop so that when it iterates it adds 4 each time, this gives the fourth element after the 3rd element and every 4th element after that till it reaches the end of the list.
sublistofbiglist = []
while biglistindex<=56:
    biglistindex = biglistindex + 4 #Increments 4 indices
    if biglistindex<=56: #Checks to makes sure index isnt greater than the length of the biglist
        sublistofbiglist.append(biglist[biglistindex]) #appends number in given index to the new list
print(sublistofbiglist)
"""
##1d

[-3, -8, 8, 0, 8, 4, 9, -12, 5, 7, 3, 7, -2]
"""

#%%

## 2.  Use for loops to do each of the following with the lists
##     defined above.
#%%
## (a) Add up the squares of the entries of biglist.
squaredlist = []
index = 0
summation = 0
for index in biglist:
    squaredlist.append(biglist[index]**2) #Increments through biglist and adds the square of each index to a new list
for n in squaredlist:
    summation = summation + n #Increments through the list of squared values, summing them together under the summation variable
print(summation)
"""
##2a

1440
"""
#%%
## (b) Create "newlist01", which has 19 entries, each the 
##     sum of the corresponding entry from list01 added 
##     to the corresponding entry from list02.  That is,
##     
##         newlist01[i] = list01[i] + list02[i] 
##     for each 0 <= i <= 18.
newlist01 = []
for i in list01 and list02:
    newlist01.append(list01[i] + list02[i]) #Adds the values of the given index in both lists together then appends them to a new list
print(newlist01)
"""
## 2b

[5, -3, 10, -4, -4, 0, 5, 9, 11, -5, -3, 9, 12, 21, 11, -6, 2, -5, -5]
"""
#%%
## (c) Compute the mean of the entries of biglist.
##     (Hint: len(biglist) gives the number
##     of entries in biglist.  This is potentially useful.)
summed = 0
for i in biglist:
    summed = summed + i #sums the all the values in the biglist
biglistmean = summed/len(biglist) #divides the summed biglist value by the number of entries in biglist
print(biglistmean)
"""
##2c

2.3684210526315788
"""
#%%
## (d) Determine the number of entries in biglist that
##     are less than 6.
total = 0
for i in biglist: #increments through biglist
    if i < 6: #if index is less then six then the total counter variable is increased by one
       total += 1
print(total)
"""
## 2d

40
"""
#%%
## (e) Determine the number of entries in biglist that
##     are between -2 and 4 (inclusive).
totale = 0
for i in biglist:#increments through biglist
    if i > -3 and i < 5: #checks to see if index value is between the proper values
        totale += 1 #increments totale counter variable
print(totale)
"""
##2e

22
"""
#%%
## (f) Create a new list called "newlist02" that contains 
##     the elements of biglist that are greater than 0.
newlist02 = []
for i in biglist:
    if i > 0: #Checks to see if value in index i in biglist is greater than 0
        newlist02.append(i) #appends index value i to newlist02
print(newlist02)
"""
## 2f

[2, 5, 4, 9, 10, 5, 5, 3, 2, 3, 8, 8, 6, 8, 4, 6, 7, 5, 9, 10, 2, 13, 1, 5, 2, 6, 7, 3, 2, 8, 7, 9, 2, 5, 5, 6]
"""
#%%

## 3.  In this problem you will be simulating confidence intervals
##     for samples drawn from a uniform distribution on [0,24], 
##     which has a mean of 12.
##     For instance, a sample of size 10 can be drawn with the 
##     commands
import numpy as np # "as np" lets us use "np"; only run once
samp = np.random.uniform(low=0,high=24,size=10)
print(samp, "line 116")
#%%
## (a) Use random samples of size 20 and simulation to generate 
##     500,000 confidence intervals of the form
##     
##                           xbar +- 2
## 
##     Use your confidence intervals to estimate the confidence
#      level. (Give the level as a percentage.)
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0 #counter variable
for i in range(500000): #increments through array
    samp = np.random.uniform(low=0,high=24,size=20) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 10 and n <= 14: #checks to see if mean in array is in proper range
        ct += 1#increments counter
ConfidenceLevel = (ct/500000)*100 #determines confidence level

print(ct, "count of means within interval, line 136")
print(ConfidenceLevel, "= ConfidenceLevel")
"""
## 3a

80.1494
"""
#%%
## (b) Repeat (a) with confidence intervals xbar +- 3
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0 #counter variable
for i in range(500000): #increments through array
    samp = np.random.uniform(low=0,high=24,size=20) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 9 and n <= 15: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 149")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
## 3b

94.8102
"""
#%%
## (c) Repeat (a) with samples of size 30.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0 #counter variable
for i in range(500000): #increments through array
    samp = np.random.uniform(low=0,high=24,size=30) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 10 and n <= 14: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 163")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
3ca

88.602
"""
#%%
## (d) Repeat (b) with samples of size 30.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0#counter variable
for i in range(500000): #increments through array
    samp = np.random.uniform(low=0,high=24,size=30) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 9 and n <= 15: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 178")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
##3db

98.3028
"""
#%%

## 4.  Here we repeat parts (a)-(d) of #3, but this time using
##     samples from an exponential distribution with mean 12.
##     The code below will produce a sample of size 10 with 
##     mean = 12:
samp = np.random.exponential(scale=12,size=10)
#%%
# 4a.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0#counter variable
for i in range(500000): #increments through array
    samp = np.random.exponential(scale=12,size=10) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 10 and n <= 14: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 199")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
##4a

40.1148
"""
#%% 4b.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0#counter variable
for i in range(500000): #increments through array
    samp = np.random.exponential(scale=12,size=10) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray:  #increments through sample means in array
    if n >= 9 and n <= 15: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 212")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
##4b

57.5634
"""
#%% 4c.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0#counter variable
for i in range(500000): #increments through array
    samp = np.random.exponential(scale=12,size=30) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 10 and n <= 14: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 225")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
##4c

64.11240000000001
"""
#%% 4d.
samparray = np.zeros(500000) #creates empty array of 500000 indices
ct = 0#counter variable
for i in range(500000): #increments through array
    samp = np.random.exponential(scale=12,size=30) #makes a sample interval
    mean = np.mean(samp) #finds the mean of the sample interval
    samparray[i] = mean #places this mean value into
for n in samparray: #increments through sample means in array
    if n >= 9 and n <= 15: #checks to see if mean in array is in proper range
        ct += 1 #increments counter
print(ct, "count of means within interval, line 238")
ConfidenceLevel = (ct/500000)*100 #determines confidence level
print(ConfidenceLevel, "= ConfidenceLevel")
"""
## 4d

83.39959999999999
"""
