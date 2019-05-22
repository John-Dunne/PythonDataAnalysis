##
## File: assignment02.py (STAT 3250)
## Topic: Assignment 2
## Name: John Dunne (jd5an)
##
import numpy as np 
import math
#%%
## 1.
##

## 1(a) Generate an array x of 10000 random values from 
##      a uniform distribution on the interval [0,50],
##      then use a for loop to determine the percentage     
##      of values that are in the interval [8,27].

ct = 0 #counter variable
oneAarray = np.random.uniform(low=0,high=50,size=10000) #Creates an single array of 10000 different elements in uniform distribution between 0 and 50. 
for i in oneAarray:
    if i>=8 and i<=27: #Line 18 to 20 increment through the array, and count how many elements are between 8 and 27 (inclusive)
        ct+= 1;
percentageinArray = (ct/10000)*100 #Finds the percentage in the loop

## Note: 1(a) asks for a percentage, not a count and not
##       a proportion.
"""
#1a
38.019999999999996%
"""
#%%
## 1(b) Repeat 1(a) 1000 times, then compute the average
##      of the 1000 percentages found.
samparray = np.zeros(1000)
countsum = 0
for x in range(1000):
    ct = 0 #counter variable
    oneAarray = np.random.uniform(low=0,high=50,size=10000) #Creates an single array of 10000 different elements in uniform distribution between 0 and 50. 
    for i in oneAarray:
        if i>=8 and i<=27: #Line 18 to 20 increment through the array, and count how many elements are between 8 and 27 (inclusive)
            ct+= 1;
    percentageinArray = (ct/10000)*100 #Finds the percentage in the loop
    samparray[x] = percentageinArray
for i in samparray:
    countsum = i + countsum #counts up indexes in the array

totalpercentage = countsum/1000 #finds the average from the array by dividing by the number of its indices
print(totalpercentage)
"""
#1b

38.00434999999995%
"""

 #%%           
## 1(c) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      first that is less than 3.
oneCarray = np.random.uniform(low=0,high=50,size=10000)
x = 0
while(oneCarray[x] >= 3 and x < 10000):  #while loop that counts number of entires passed until a index with a value of 3 is found
    x+= 1
#print(x, "count required to find value less than 3")
    
"""
# 1c
11
"""
#%%
## 1(d) Repeat 1(c) 1000 times, then compute the average for the
##      number of random entries required.
samparray = np.zeros(1000)
totalvalue = 0
for v in range(1000):
    oneCarray = np.random.uniform(low=0,high=50,size=10000)
    x = 0
    while(oneCarray[x] >= 3 and x < 10000):
        x+= 1
    samparray[v] = x
for index in samparray: #adds up values in in array
    indexvalue = samparray[int(index)]
    totalvalue = indexvalue + totalvalue
    average = totalvalue/1000 #creates the average by dividing the total by 1000
#print(average)
"""
#1d
19.418
"""
#%%
## 1(e) For the array x in 1(a), use a while loop to determine 
##      the number of random entries required to find the
##      third entry that exceeds 36.
ct = 0 #counter variable
x = 0
oneAarray = np.random.uniform(low=0,high=50,size=10000) #Creates an single array of 10000 different elements in uniform distribution between 0 and 50. 
while(ct < 3 and x < 10000):
    if oneAarray[x] > 36: #if index value is over 36, add 1 to count and indexing value
        ct+=1
        x+=1
    else:
        x+=1 #else just add 1 to indexing value
#print(x, "entries required to find a 3 entry that exceeds 36")
"""
#1e
14
"""
#%%
## 1(f) Repeat 1(e) 5000 times, then compute the average for the
##      number of random entries required.
ct = 0 #counter variable
x = 0
runningtotal = 0.0
samparray = np.zeros(5000)
for v in range(5000):
    oneAarray = np.random.uniform(low=0,high=50,size=10000) #Creates an single array of 10000 different elements in uniform distribution between 0 and 50. 
    while(ct < 3 and x < 10000):
        if oneAarray[x] > 36: #if index value is over 36, add 1 to count and indexing value
            ct+=1
            x+=1
        else:
            x+=1 #else just add 1 to indexing value
    samparray[v] = x
for index in samparray: #totals up array
    runningtotal = samparray[int(index)] + runningtotal 
average = runningtotal/5000 #finds average of the sum of the array elements
#print(average, "average of 5000 samples")
"""
#1f
10
"""
#%%
## 2.   For this problem you will draw samples from a normal
##      population with mean 40 and standard deviation 12.
##      Run the code below to generate your population, which
##      will consist of 1,000,000 elements.

p1 = np.random.normal(40,12,size=1000000)
#%%
## 2(a) The formula for a 95% confidence interval for the 
##      population mean is given by
##     
##      [xbar - 1.96*sigma/sqrt(n), xbar + 1.96*sigma/sqrt(n)]
##
##      where xbar is the sample mean, sigma is the population
##      standard deviation, and n is the sample size.
##
##      Select 10,000 random samples of size 10 from p1.  For
##      each sample, find the corresponding confidence 
##      interval, and then determine the percentage of
##      confidence intervals that contain the population mean.
##      (This is an estimate of the confidence level.)
count = 0
for x in range(10000):
    confidenceinterval = 0
    s = np.random.choice(p1, size=10) #Selects a random sample
    xbar = np.mean(s) #finds the mean of the sample
    confidenceintervalhigh = xbar+(1.96*12/math.sqrt(10))  #upper confidence interval
    confidenceintervallow = xbar-(1.96*12/math.sqrt(10)) #lower confidence interval
    if confidenceintervalhigh > 40 and confidenceintervallow < 40:
        count+= 1 #increments count if sample mean is between confidence intervals
Confidencelevel = (count/10000)*100 #finds confidence level via averaging confidence interval count from previous line
#print(Confidencelevel)
"""
#2a
95.23
"""

#%%
## 2(b) Frequently in applications the population standard
##      deviation is not known. In such cases, the sample
##      standard deviation is used instead.  Repeat part 2(a)
##      replacing the population standard deviation with the
##      standard deviation from each sample, so that the
##      formula is
##
##      [xbar - 1.96*stdev/sqrt(n), xbar + 1.96*stdev/sqrt(n)]
##
##      Tip: Recall the command for the standard deviation is 
##           np.std(data, ddof=1)
count = 0
for x in range(10000):
    confidenceinterval = 0
    s = np.random.choice(p1, size=10) #Selects a random sample
    xbar = np.mean(s) #finds the mean of the sample
    standardDev = np.std(s, ddof=1) #finds standard deviation from sample
    confidenceintervalhigh = xbar+(1.96*standardDev/math.sqrt(10))  #upper confidence interval
    confidenceintervallow = xbar-(1.96*standardDev/math.sqrt(10)) #lower confidence interval
    if confidenceintervalhigh > 40 and confidenceintervallow < 40:
        count+= 1 #increments count if sample mean is between confidence intervals
Confidencelevel = (count/10000)*100
#print(Confidencelevel)
"""
#2b
91.84
"""
#%%
## 2(c) Your answer in part 2(b) should be a bit off, in that
##      the estimated confidence level isn't quite 95%.  The 
##      problem is that a t-distribution is appropriate when
##      using the sample standard deviation.  Repeat part 2(b),
##      this time using t* in place of 1.96 in the formula,
##      where: t* = 2.262 for n = 10.
count = 0
t = 2.262
for x in range(10000):
    confidenceinterval = 0
    s = np.random.choice(p1, size=10) #Selects a random sample
    xbar = np.mean(s) #finds the mean of the sample
    standardDev = np.std(s, ddof=1) #finds standard deviation from sample
    confidenceintervalhigh = xbar+(t*standardDev/math.sqrt(10))  #upper confidence interval
    confidenceintervallow = xbar-(t*standardDev/math.sqrt(10)) #lower confidence interval
    if confidenceintervalhigh > 40 and confidenceintervallow < 40:
        count+= 1 #increments count if sample mean is between confidence intervals
Confidencelevel = (count/10000)*100
print(Confidencelevel)
"""
#2c
95.28
"""

#%%
## 3.   Suppose that random numbers are selected one at a time
##      with replacement from among the set 0, 1, 2, ..., 8, 9.
##      Use 10,000 simulations to estimate the average number 
##      of values required to select three identical values in 
##      a row.
samparray = np.zeros(10000)
totalcount = 0;


Set = [0,1,2,3,4,5,6,7,8,9] #set of 0 to 9
for x in range(10000): #10000 simulations
    count = 0 #resets count and x for each simulation
    x = 0
    while(x != 3): #for each loop it picks 3 random values
        randompick1 = np.random.choice(Set, 1)
        randompick2 = np.random.choice(Set, 1)
        randompick3 = np.random.choice(Set, 1)
        count+=1 #adds a count
        if randompick1 == randompick2 == randompick3: #if all 3 values are equal the sentinel value is changed to 3 to exit while loop
            x = 3
    samparray[x] = count
for i in samparray:
    totalcount = samparray[x]+totalcount #totals up and then averages the counts
average = totalcount/10000
print(average)
"""
#3
63.0
"""

#%%
## 4.   Jay is taking a 20 question true/false quiz online.  The
##      quiz is configured to tell him whether he gets a question
##      correct before proceeding to the next question.  The 
##      responses influence Jay's confidence level and hence his 
##      exam performance.  In this problem we will use simulation
##      to estimate Jay's average score based on a simple model.
##      We make the following assumptions:
##    
##      * At the start of the quiz there is a 80% chance that 
##        Jay will answer the first question correctly.
##      * For all questions after the first one, if Jay got 
##        the previous question correct, then there is a
##        88% chance that he will get the next question
##        correct.  (And a 12% chance he gets it wrong.)
##      * For all questions after the first one, if Jay got
##        the previous question wrong, then there is a
##        70% chance that he will get the next question
##        correct.  (And a 30% chance he gets it wrong.)
##      * Each question is worth 5 points.
##
##      Use 10,000 simulated quizzes to estimate the average 
##      score.
quizArray = np.zeros(10000) #quiz score array
for quiz in range(10000): #10,000 simulations
#for quiz in range(10000):
    firstQuestion = np.random.choice([0,1], size=1, p=[0.2,0.8])
    counter = 0
    answeredQuestions = np.zeros(21) #individual quiz score array
    answeredQuestions[0] = firstQuestion[0] #first qeustion in answeredQuestions is filled with the firstQuestion's answer (0 = wrong, 1 = right)
    while counter < 19:
        if answeredQuestions[counter] == 1: #If question before was correct, the next question is answered based upon a 0.88 probability of answering correctly
            questionCorrect = np.random.choice([0,1], size = 1, p = [0.12, 0.88])
            counter+= 1
            answeredQuestions[counter] = questionCorrect[0] #answer score (0 = wrong, 1 = right) is added to the answered question array
        if answeredQuestions[counter] == 0: #if question answered previously was wrong (0) then the next question is answered based upon a 0.7 chance of a correct answer
            questionWrong = np.random.choice([0,1], size = 1, p = [0.3, 0.7])
            counter+= 1
            answeredQuestions[counter] = questionWrong #answer is added toquiz score array 
    finalGrade = np.sum(answeredQuestions)*5 #quiz score array is summed then multiplied by 5 to get the proper grade
    quizArray[quiz] = finalGrade #quiz is added to the 10,000 quiz array
quizAverage = np.sum(quizArray)/10000 #average is found by summing array then dividing by index total

"""
#4

85.3955

"""

#%%
## 5.   The questions in this problem should be done without the 
##      use of loops.  They can be done with NumPy functions.
##      The different parts use the array defined below.

import numpy as np # Load NumPy
arr1 = np.array([[2,5,7,0,2,5,-6,8,1,-9],[-1,3,4,2,0,1,3,2,1,-1],
                [3,0,-2,-2,5,4,5,9,0,7],[1,3,2,0,4,5,1,9,8,6],
                [1,1,0,1,5,3,2,9,0,-9],[0,1,7,7,7,-4,0,2,5,-9]])

## 5(a) Extract a submatrix arr1_slice1 from arr1 that consists of
##      the second and third rows of arr1.
arr1_slice1 = arr1[1:3]
'''
#5a
[[-1  3  4  2  0  1  3  2  1 -1]
 [ 3  0 -2 -2  5  4  5  9  0  7]]
'''
## 5(b) Find a one-dimensional array that contains the entries of
##      arr1 that are less than -2.
arr1[arr1 < -2]
"""
#5b

[-6 -9 -9 -4 -9]
"""
np.mean(arr1[arr1 <= 2])
## 5(c) Determine the number of entries of arr1 that are greater
##      than 4.
numberlessthan4 = np.sum(arr1 > 4)
"""
#5c
18
"""
## 5(d) Find the mean of the entries of arr1 that are less than
##      or equal to -2.
np.mean(arr1[arr1 <= 2])
"""
#5d
-0.5882352941176471
"""
## 5(e) Find the sum of the squares of the odd entries of arr1.
##      (Note: This is the entries that are odd numbers, not the
##       entries indexed by odd numbers.)

np.sum(np.square(arr1[arr1%2 != 0]))

"""
#5e

962
"""
## 5(f) Determine the proportion of positive entries of arr1 
##      that are greater than 5.

arrPositive = arr1[arr1 > 0] #array of values larger than 0
arrGreaterthan5 = arrPositive[arrPositive > 5] #array of values larger than 5
proportion = np.size(arrGreaterthan5)/np.size(arrPositive) #size of greater than 5 array over positive array
"""
#5f
0.2619047619047619
"""














