##
## File: assignment05.py (STAT 3250)
## Topic: Assignment 5
## Name: John Dunne (jd5an)

##  This assignment requires the data file 'diabetic_data.csv'.  This file
##  contains records for over 100,000 hospitalizations for people who have
##  diabetes.  The file 'diabetic_info.csv' contains information on the
##  codes used for a few of the entries.  Missing values are indicated by
##  a '?'.  You should be able to read in this file using the usual 
##  pandas methods.

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit. 
import pandas as pd
import numpy as np 
import math

data = pd.read_csv('diabetic_data.csv')
#%%
## 1.  Determine the average number of medications ('num_medications') for 
##     males and for females.
print(data['num_medications'].groupby(data['gender']).mean()[0:2]) #Displays  male and female average
'''
1.
Female    16.187888
Male      15.828775
'''
#%%
## 2.  Determine the average length of hospital stay ('time_in_hospital')
##     for each race classification.  (Omit those unknown '?' but include 
##     those classified as 'Other'.)
print(data['time_in_hospital'].groupby(data['race']).mean()[1:]) #displays races, omits index 0 which is ?
'''
2.

race
AfricanAmerican    4.507860
Asian              3.995320
Caucasian          4.385721
Hispanic           4.059892
Other              4.273572
'''
#%%
## 3.  Among males, find a 95% confidence interval for the proportion that 
##     had at 2 or more procedures ('num_procedures').  Then do the same 
##     for females.
datagreaterthan2 = data[data['num_procedures'] > 1] #keep rows that have 2 or more operations  
femaledata = datagreaterthan2[datagreaterthan2['gender'] == "Female"] #isolate females
maledata = datagreaterthan2[datagreaterthan2['gender'] == "Male"] #isolate males
femalepopmean = femaledata['num_procedures'].groupby(femaledata['gender']).mean() #male and female pop means found
malepopmean = maledata['num_procedures'].groupby(maledata['gender']).mean()
samplefemale = femaledata.sample(n = 376) #random sample taken from female dataframe
femalexbar = femaledata['num_procedures'].groupby(femaledata['gender']).mean() #sample mean of female dataframe found
malexbar = maledata['num_procedures'].groupby(maledata['gender']).mean() #same mean of male dataframe
samplemale = femaledata.sample(n = 376) #random male sample from male population
femalesigma = femaledata["num_procedures"].std() #signma/standard deviation of male and female dataframes found
malesigma = maledata["num_procedures"].std()
n = 376 #sample size
print((femalexbar - 1.96*femalesigma/math.sqrt(n)))
print((femalexbar + 1.96*femalesigma/math.sqrt(n)))
print(femalepopmean, "female pop mean")
print((malexbar - 1.96*malesigma/math.sqrt(n)))
print( (malexbar + 1.96*malesigma/math.sqrt(n)))
print(malepopmean, "male popmean")

'''
3.
        low,high
Male [3.329338, 3.624546] with pop mean of 3.476942
Female [3.114328, 3.391286] with pop mean of 3.252807
'''
#%%
## 4.  Among the patients in this data set, what percentage had more than
##     one recorded hospital visit?  (Each distinct record can be assumed 
##     to be for a distinct hospital visit.)
print(((data['patient_nbr'].value_counts() > 1).sum()/(data['patient_nbr'].nunique()))*100) #sum of number of unique ids that appear more than once / total number of unique ids * 100
'''
4.

23.452837048015883
'''
#%%
## 5.  List the top-10 most common diagnoses, based on the codes listed in
##     the columns 'diag_1', 'diag_2', and 'diag_3'.
diagdata = data[['diag_1','diag_2','diag_3']]
print(diagdata.stack().value_counts().head(10)) #stack the values together then count them up across columns, show the top 10
'''
5.
code|Sum
428    18101
250    17861
276    13816
414    12895
401    12371
427    11757
599     6824
496     5990
403     5693
486     5455
'''

#%%
## 6.  The 'age' in each record is given as a 10-year range of ages.  Assume
##     that the age for a person is the middle of the range.  (For instance,
##     those with 'age' [40,50) are assumed to be 45.)  Determine the average
##     age for each classification in 'insulin'.
datainsulinage = data[['age','insulin']]

steadyinsulin = datainsulinage[datainsulinage['insulin'] == "Steady"] 
steady = steadyinsulin['insulin'].groupby(steadyinsulin['age']).value_counts()

Downinsulin = datainsulinage[datainsulinage['insulin'] == "Down"]
Down = Downinsulin['insulin'].groupby(Downinsulin['age']).value_counts()

Upinsulin = datainsulinage[datainsulinage['insulin'] == "Up"]
Up = Upinsulin['insulin'].groupby(Upinsulin['age']).value_counts()

Noinsulin = datainsulinage[datainsulinage['insulin'] == "No"] 
No = Noinsulin['insulin'].groupby(Noinsulin['age']).value_counts()



print((steady[0]*5+steady[1]*15+steady[2]*25+steady[3]*35+steady[4]*45+steady[5]*55+steady[6]*65+steady[7]*75+steady[8]*85+steady[9]*95)/steadyinsulin.count()[0],"|Average steady insulin age")
print((No[0]*5+No[1]*15+No[2]*25+No[3]*35+No[4]*45+No[5]*55+No[6]*65+No[7]*75+No[8]*85+No[9]*95)/Noinsulin.count()[0],"|Average No insulin age")

print((Up[0]*5+Up[1]*15+Up[2]*25+Up[3]*35+Up[4]*45+Up[5]*55+Up[6]*65+Up[7]*75+Up[8]*85+Up[9]*95)/Upinsulin.count()[0],"|Average Up insulin age")
print((Down[0]*5+Down[1]*15+Down[2]*25+Down[3]*35+Down[4]*45+Down[5]*55+Down[6]*65+Down[7]*75+Down[8]*85+Down[9]*95)/Downinsulin.count()[0],"|Average Down insulin age")
'''
6.

65.57116924373561 |Average steady insulin age
67.46016503809383 |Average No insulin age
63.67355956168257 |Average Up insulin age
63.300049107873626 |Average Down insulin age
'''
#%%
## 7.  Among those whose weight range is given, assume that the actual
##     weight is at the midpoint of the given interval.  If the weight is
##     listed as '>200' then assume the actual weight is 200.  Determine the
##     average weight for those whose 'num_lab_procedures' exceeds 50,
##     then do the same for those that are fewer than 30.
dataweight = data[['num_lab_procedures', 'weight']]
datagreaterthan50 = dataweight[dataweight['num_lab_procedures'] > 50]
datalessthan30 = dataweight[dataweight['num_lab_procedures'] < 30]
dataweightover50 = datagreaterthan50[["weight"]]
datalessthan30 = datalessthan30[["weight"]]

print((dataweightover50['weight'].value_counts()[1]*87.5+dataweightover50['weight'].value_counts()[2]*62.5+dataweightover50['weight'].value_counts()[3]*112.5+dataweightover50['weight'].value_counts()[4]*137.5+dataweightover50['weight'].value_counts()[5]*37.5+dataweightover50['weight'].value_counts()[6]*12.5+dataweightover50['weight'].value_counts()[7]*162.5+dataweightover50['weight'].value_counts()[8]*187.5+dataweightover50['weight'].value_counts()[9]*200)/dataweightover50['weight'].value_counts()[1:].sum(),"|Average weight over 50 operations")

print((datalessthan30['weight'].value_counts()[1]*87.5+datalessthan30['weight'].value_counts()[2]*112.5+datalessthan30['weight'].value_counts()[3]*62.5+datalessthan30['weight'].value_counts()[4]*137.5+datalessthan30['weight'].value_counts()[5]*12.5+datalessthan30['weight'].value_counts()[6]*162.5+datalessthan30['weight'].value_counts()[7]*37.5)/datalessthan30['weight'].value_counts()[1:].sum(),"|Average weight under 30 operations")
'''
7.

85.05018489170628 |Average weight over 50 operations
88.73546511627907 |Average weight under 30 operations
'''
#%%
## 8.  Three medications for type 2 diabetes are 'glipizide', 'glimepiride',
##     and 'glyburide'.  There are columns in the data for each of these.
##     Determine the number of records for which at least two of these
##     are listed as 'Steady'.
datadrugs = data[['glipizide', 'glimepiride', 'glyburide']]
dataglip = datadrugs[datadrugs['glipizide'] == "Steady"]
dataglipglim = dataglip[dataglip['glimepiride'] == "Steady"] #this line and the two above isolate the records which have glim and glip AS well as all three drugs == to steady

datanotglip = datadrugs[datadrugs['glipizide'] != "Steady"]
dataglim = datanotglip[datanotglip['glimepiride'] == "Steady"]
dataglimgly = dataglim[dataglim['glyburide'] == "Steady"] #this line and the two above isolate just the records which have glim and gly == Steady. 

print(dataglipglim['glipizide'].value_counts() + dataglimgly['glyburide'].value_counts()) #Adding the value counts together after the isolating above accounts for all records with at least 2 drugs steady without accounting for some records twice
'''
8.

126
'''
#%%
## 9.  What percentage of reasons for admission ('admission_source_id')
##     correspond to some form of transfer from another care source?

dataAdmission = data[['admission_source_id']] #The instructions to this question are a bit unclear and I am interprettign them as 'find the percentage of records that were admitted after coming from other sources of care'
datatransferedfromcare = dataAdmission[(dataAdmission['admission_source_id']  == 1) | (dataAdmission['admission_source_id'] == 2) | (dataAdmission['admission_source_id'] == 4) | (dataAdmission['admission_source_id'] == 5) | (dataAdmission['admission_source_id'] == 6) | (dataAdmission['admission_source_id'] == 7) | (dataAdmission['admission_source_id'] == 10) | (dataAdmission['admission_source_id'] == 25) | (dataAdmission['admission_source_id'] == 26)]
#The line above collects all records that have admission_source_id == 1,2,4,5,6,7,10, 25, 26. The instruction were not clear on "care source" so I chose these as reasonably constituting other care sources.
print(((datatransferedfromcare['admission_source_id'].value_counts().sum())/dataAdmission['admission_source_id'].value_counts().sum())*100) #The percentage of admissions that were transfers from other sources of care
'''
9.

92.83945522080066
'''
#%%
## 10. The column 'discharge_disposition_id' gives codes for discharges.
##     Determine which codes (and the corresponding outcomes from the ID
##     file) resulted in no readmissions ('NO' under 'readmitted').  Then
##     find the top-5 outcomes that resulted in readmissions, in terms of
##     the percentage of times readmission was required.
dataDischarge = data[['discharge_disposition_id', 'readmitted']]
noReadmit = dataDischarge[dataDischarge['readmitted'] == "NO"]
Readmit = dataDischarge[dataDischarge['readmitted'] != "NO"]
print(Readmit['discharge_disposition_id'].value_counts()) #The items not in this are the codes that resulted in no readmission (codes = 11,19,20,21,26,29)
print(((Readmit['discharge_disposition_id'].value_counts()/dataDischarge['discharge_disposition_id'].value_counts())*100).sort_values(ascending=False).head(5)) #prints top discharge reasons based upon percentage of times readmission was required
'''
10.

No readmission codes = 11,19,20,21,26,29

discharge reason|percentage
15    73.015873
12    66.666667
10    66.666667
28    61.151079
16    54.545455
'''
