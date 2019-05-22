##
## Random
## John Dunne (jd5an)
##

#jd5an

## 'airline-stats.txt' required.  This file contains
##  over 50,000 records of aggregated flight information, organized by airline, 
##  airport, and month.  The first record is shown below.

# =============================================================================
# airport
#     code: ATL 
#     name: Atlanta GA: Hartsfield-Jackson Atlanta International
# flights 
#     cancelled: 5 
#     on time: 561 
#     total: 752 
#     delayed: 186 
#     diverted: 0
# number of delays 
#     late aircraft: 18 
#     weather: 28 
#     security: 2 
#     national aviation system: 105 
#     carrier: 34
# minutes delayed 
#     late aircraft: 1269 
#     weather: 1722 
#     carrier: 1367 
#     security: 139 
#     total: 8314 
#     national aviation system: 3817
# dates
#     label: 2003/6 
#     year: 2003 
#     month: 6
# carrier
#     code: AA 
#     name: American Airlines Inc.
# =============================================================================
import pandas as pd
pd.set_option('display.max_columns', 500)
import numpy as np

airlines1 = open('airline-stats.txt').read().split('##########')
airlines = pd.Series(airlines1)

#%%
## 1.  Give the total number of hours delayed for all flights in all records.

total = (np.sum(airlines.str.split('total').str[2].str.split(" ").str[1].astype(float)))/60 #takes second total (which is total time delayed in minutes) for each airport, sums the total delayed minutes and divides by 60 to give hours
#print(total)
'''
#1

9991285.583333334 total hours delayed
'''
#%%

## 2.  Which airlines appear in at least 1000 records?  Give a table of airline
##     names and number of records for each, in order of record count (largest
##     to smallest).
carrier = (airlines.str.split('month').str[1].str.rstrip().str.split("name").str[1]).value_counts()[0:18] #splits series down to carrier, then to name, from there you just need index 1 of the remaining string for each entry to yield the name of the airline before you call value_count
#Also threw an rstrip in the line above to remove the pesky newlines
#print(carrier)
'''
#2

: Delta Air Lines Inc.            4370
: American Airlines Inc.          4296
: United Air Lines Inc.           4219
: US Airways Inc.                 3918
: ExpressJet Airlines Inc.        3174
: Southwest Airlines Co.          2900
: JetBlue Airways                 2857
: Frontier Airlines Inc.          2821
: Continental Air Lines Inc.      2815
: AirTran Airways Corporation     2801
: Alaska Airlines Inc.            2678
: SkyWest Airlines Inc.           2621
: American Eagle Airlines Inc.    2379
: Northwest Airlines Inc.         2288
: Mesa Airlines Inc.              1682
: Comair Inc.                     1671
: Atlantic Southeast Airlines     1460
: Hawaiian Airlines Inc.          1073
'''
 #%%   
## 3.  For some reason, the entry under 'flights/delayed' is not always the same
##     as the total of the entries under 'number of delays'.  (The reason for
##     this is not clear.)  Determine the percentage of records for which 
##     these two values are different.
 
delayed = airlines.str.split('flights').str[1].str.split("delayed").str[1].str.split(" ").str[1].astype(float) #each of these lines acquires the number from each category
lateaircraft = airlines.str.split('number of delays').str[1].str.split("late aircraft").str[1].str.split(" ").str[1] .astype(float)
weather = airlines.str.split('number of delays').str[1].str.split("weather").str[1].str.split(" ").str[1].astype(float)
nationalaviation = airlines.str.split('number of delays').str[1].str.split("national aviation system").str[1].str.split(" ").str[1].astype(float)
carrierdelay = airlines.str.split('number of delays').str[1].str.split("carrier").str[1].str.split(" ").str[1].str.split("\n").str[0].astype(float)
part1 = lateaircraft.add(weather)
part2 = part1.add(nationalaviation)
final = part2.add(carrierdelay) #add the series together
totalsum = sum((delayed.sub(final)).value_counts()[0:])

equalto = delayed.sub(final).value_counts()[0]
#print((equalto/totalsum)*100) #find the percentages by dividing how many were not equal to zero after comparing the delayed total and delayed numbers by total number of records of delayed...if that makes sense
'''
#3

60.6668764926962
'''

#%%
## 4.  Determine the number of records for which the number of delays due to
##     late aircraft exceeds the number of delays due to weather.
lateaircraft = airlines.str.split('number of delays').str[1].str.split("late aircraft").str[1].str.split(" ").str[1] .astype(float)
weather = airlines.str.split('number of delays').str[1].str.split("weather").str[1].str.split(" ").str[1].astype(float)

#print((lateaircraft > weather).value_counts())
'''
#4

46890
'''
#%%
## 5.  Find the top-10 airports in terms of the total number of minutes delayed.
##     Give a table of the airport names and the total minutes delayed, in 
##     order from largest to smallest.

airport = airlines.str.split('\n').str[4] #gets names of airports
totalminutesdelayed = airlines.str.split('total').str[2].str.split(" ").str[1].astype(float) #gathers total delayed time for each airport
newtable = pd.concat([airport, totalminutesdelayed], axis = 1) #creates table out of delayed time and airport
sortedtable = newtable.sort_values(by = 0).dropna() #sorts table, drops NAN values
df = pd.DataFrame({'airport name':sortedtable[0], 'minutes delayed':sortedtable[1],}) #creates a new dataframe with designated headers
print((df.groupby('airport name').sum()/60).sort_values(by = 'minutes delayed', ascending = False)[0:10]) #sums airport delay totals by airport names, divides by 60 to get hours, then shops top 10 airports

'''
##5
              
airport name                                        minutes delayed          
    name: Chicago IL: Chicago O'Hare International     1.101326e+06
    name: Atlanta GA: Hartsfield-Jackson Atlant...     1.030170e+06
    name: Dallas/Fort Worth TX: Dallas/Fort Wor...     6.541089e+05
    name: Newark NJ: Newark Liberty International      5.551116e+05
    name: San Francisco CA: San Francisco Inter...     4.830045e+05
    name: Denver CO: Denver International              4.503481e+05
    name: Los Angeles CA: Los Angeles Internati...     4.482878e+05
    name: Houston TX: George Bush Intercontinen...     4.020210e+05
    name: New York NY: LaGuardia                       3.722549e+05
    name: New York NY: John F. Kennedy Internat...     3.330950e+05

'''
#%%
## 6.  Find the top-10 airports in terms of percentage of on time flights.
##     Give a table of the airport names and percentages, in order from 
##     largest to smallest.
airportnames = airlines.str.split('\n').str[4] #gather airport names
ontime = airlines.str.split('flights').str[1].str.split("on time:").str[1].str.split(" ").str[1].astype(float) #gather ontime numbers
total = airlines.str.split('flights').str[1].str.split("total:").str[1].str.split(" ").str[1].astype(float) #gather total flights

newtable = pd.concat([airportnames, ontime], axis = 1)  #create a series out of airport and on time
totalnewtable = pd.concat([airportnames, total], axis = 1) #create a series out of airports and total 
df = pd.DataFrame({'airport name':newtable[0], 'ontime':newtable[1], 'total':totalnewtable[1]})  #create a dataframe from the two series above

sorteddataframe = (df.groupby('airport name').sum()) #condense the data table down to just the airports
sorteddataframe['percentage of on time flights'] = (sorteddataframe['ontime']/sorteddataframe['total'])*100 #create a percentage column
#print((sorteddataframe.drop(columns=['ontime', 'total'])).sort_values(by = 'percentage of on time flights', ascending=False)[0:10]) #drop total and ontime columns and sort by top percentages

'''
##6
                                                    percentage of on time flights
airport name                                                  
    name: Salt Lake City UT: Salt Lake City Int...   84.249328
    name: Phoenix AZ: Phoenix Sky Harbor Intern...   82.423895
    name: Portland OR: Portland International        80.759415
    name: Minneapolis MN: Minneapolis-St Paul I...   80.342827
    name: Chicago IL: Chicago Midway International   80.317165
    name: Charlotte NC: Charlotte Douglas Inter...   80.310017
    name: Baltimore MD: Baltimore/Washington In...   80.268309
    name: Denver CO: Denver International            80.236443
    name: Detroit MI: Detroit Metro Wayne County     80.182134
    name: Houston TX: George Bush Intercontinen...   80.117228
'''



#%%
## 7.  Find the top-10 airlines in terms of percentage of on time flights.
##     Give a table of the airline names and percentages, in order from 
##     largest to smallest.

airlinenames = airlines.str.split('\n').str[30] #gather airline names
ontime = airlines.str.split('flights').str[1].str.split("on time:").str[1].str.split(" ").str[1].astype(float) #gather ontime numbers
total = airlines.str.split('flights').str[1].str.split("total:").str[1].str.split(" ").str[1].astype(float) #gather total flights

newtable = pd.concat([airlinenames, ontime], axis = 1)  #create a series out of airline and on time
totalnewtable = pd.concat([airlinenames, total], axis = 1) #create a series out of airline and total 
df = pd.DataFrame({'airline name':newtable[0], 'ontime':newtable[1], 'total':totalnewtable[1]})  #create a dataframe from the two series above

sorteddataframe = (df.groupby('airline name').sum()) #condense the data table down to just the airlines
sorteddataframe['percentage of on time flights'] = (sorteddataframe['ontime']/sorteddataframe['total'])*100 #create a percentage column
#print((sorteddataframe.drop(columns=['ontime', 'total'])).sort_values(by = 'percentage of on time flights', ascending=False)[0:10]) #drop total and ontime columns and sort by top percentages

'''
##7

                                     percentage of on time flights
airline name                                    
    name: Endeavor Air Inc.            84.050792
    name: Alaska Airlines Inc.         81.888334
    name: Virgin America               81.492009
    name: Aloha Airlines Inc.          80.934150
    name: Delta Air Lines Inc.         80.411719
    name: SkyWest Airlines Inc.        80.102370
    name: Southwest Airlines Co.       80.061932
    name: America West Airlines Inc.   79.373011
    name: Hawaiian Airlines Inc.       79.308415
    name: US Airways Inc.              78.974549
'''

#%%
## 8.  Determine the average length (in minutes) of a weather-related delay.

weather = airlines.str.split('minutes delayed').str[1].str.split("weather").str[1].str.split(" ").str[1].astype(float) #takes weather related delay time from each entry
#print(np.mean(weather))
'''
##8

512.2644548534612 minutes
'''
#%%
## 9.  For each month, determine which airport had the highest percentage
##     of delays.  Give a table listing the month number, the airport name,
##     and the percentage.
airportnames = airlines.str.split('\n').str[4] #gather airport names
delayed = airlines.str.split('flights').str[1].str.split("delayed").str[1].str.split(" ").str[1].astype(float) #each of these lines acquires the number from each category
total = airlines.str.split('flights').str[1].str.split("total:").str[1].str.split(" ").str[1].astype(float) #gather total flights
month = airlines.str.split('\n').str[27].str.rstrip("\n").str.lstrip("month: ") #gets the month value


delayedtable = pd.concat([airportnames, delayed], axis = 1)  #create a series out of airport and on time
totaltable = pd.concat([airportnames, total], axis = 1) #create a series out of airports and total 
monthtable = pd.concat([airportnames, month], axis = 1)
percentagedelayed = (delayedtable[1]/totaltable[1])

df3 = (pd.DataFrame({'airport name':delayedtable[0], 'delayed':delayedtable[1], 'total':totaltable[1], 'month':monthtable[1]}) ).drop(index = 0)
df4 = df3[['delayed', 'total', 'airport name']].groupby([df3['airport name'],df3['month']])
df5 = df4.sum()

df5['percentage of flights delayed'] = (df5['delayed']/df5['total'])*100
df6 = df5.drop(columns=['delayed', 'total'])
df7 = df6.sort_values(by = ['percentage of flights delayed'], ascending = False)

'''
## 9

                                                          percentage of flights delayed
airport name                                       month                               
name: Newark NJ: Newark Liberty International  12                         33.508850
name: Newark NJ: Newark Liberty International  11                         26.961231
name: Newark NJ: Newark Liberty International  10                         26.140379
name: Newark NJ: Newark Liberty International  9                          23.935120
name: Newark NJ: Newark Liberty International  8                          27.601543
name: Newark NJ: Newark Liberty International  7                          31.445250
name: Newark NJ: Newark Liberty International  6                          32.377593
name: Newark NJ: Newark Liberty International  5                          30.339172
name: Newark NJ: Newark Liberty International  4                          30.250067
name: Newark NJ: Newark Liberty International  3                          31.613341
name: Newark NJ: Newark Liberty International  2                          27.909382
name: Chicago IL: Chicago O'Hare International 1                          27.392193
 
'''

#%%
## 10. For each year, determine the percentage of flights delayed by weather.

security = airlines.str.split('number of delays').str[1].str.split("security").str[1].str.split(" ").str[1].astype(float) #each of these lines acquires the number from each category
lateaircraft = airlines.str.split('number of delays').str[1].str.split("late aircraft").str[1].str.split(" ").str[1] .astype(float)
weather = airlines.str.split('number of delays').str[1].str.split("weather").str[1].str.split(" ").str[1].astype(float)
nationalaviation = airlines.str.split('number of delays').str[1].str.split("national aviation system").str[1].str.split(" ").str[1].astype(float)
carrierdelay = airlines.str.split('number of delays').str[1].str.split("carrier").str[1].str.split(" ").str[1].str.split("\n").str[0].astype(float)
year = airlines.str.split('dates').str[1].str.split("year").str[1].str.split(" ").str[1].str.split("\n").str[0].astype(float)

securitytable = pd.concat([year, security], axis = 1)  #create a series out of airport and on time
latetable = pd.concat([year, lateaircraft], axis = 1) #create a series out of airports and total 
weathertable = pd.concat([year, weather], axis = 1)
nationaltable = pd.concat([year, nationalaviation], axis = 1)
carriertable = pd.concat([year, carrierdelay], axis = 1)

df = (pd.DataFrame({'year':delayedtable[0], 'security':securitytable[1], 'late aircraft':latetable[1], 'weather':weathertable[1], 'national aviation':nationaltable[1], 'carrier delay':carriertable[1]}).dropna())
newdf = df.groupby('year').sum()
newdf['percentage of flights delayed by weather'] = (newdf['weather']/(newdf['security'] + newdf['late aircraft'] + newdf['weather'] + newdf['national aviation'] + newdf['carrier delay']))*100
#print(newdf.drop(columns=['security', 'weather', 'late aircraft', 'national aviation', 'carrier delay']))

'''
##10

        percentage of flights delayed by weather
year                                            
2003.0                                  3.768937
2004.0                                  4.029022
2005.0                                  3.577066
2006.0                                  3.445933
2007.0                                  3.500137
2008.0                                  3.236351
2009.0                                  3.182635
2010.0                                  2.926723
2011.0                                  2.711382
2012.0                                  2.824133
2013.0                                  2.772830
2014.0                                  2.873415
2015.0                                  3.305040
2016.0                                  3.123764
'''
#%%
## 11. Find the top-10 airports in terms of average length (in minutes) of 
##     security-related flight delays.  Give a table listing the airport name 
##     and average, sorted from largest to smallest.

airportnames = airlines.str.split('\n').str[4]
security = airlines.str.split('minutes delayed').str[1].str.split("security").str[1].str.split(" ").str[1].astype(float)
securitytable = pd.concat([airportnames, security], axis = 1).dropna()
df = (pd.DataFrame({'airport name':securitytable[0], 'security delay (minutes)':securitytable[1]}))
print((df.groupby('airport name').mean()).sort_values(by = 'security delay (minutes)', ascending = False)[1:11])
'''
##11

                                                    security delay (minutes)
airport name                                                                
    name: Los Angeles CA: Los Angeles Internati...                 31.171882
    name: Phoenix AZ: Phoenix Sky Harbor Intern...                 28.088348
    name: Houston TX: George Bush Intercontinen...                 27.581944
    name: Atlanta GA: Hartsfield-Jackson Atlant...                 26.778228
    name: Chicago IL: Chicago Midway International                 25.979872
    name: New York NY: John F. Kennedy Internat...                 25.131987
    name: Chicago IL: Chicago O'Hare International                 24.656299
    name: Las Vegas NV: McCarran International                     21.649906
    name: Seattle WA: Seattle/Tacoma International                 21.353691
    name: Dallas/Fort Worth TX: Dallas/Fort Wor...                 21.238894
'''
#%%
## 12. Determine the top-10 airport/airline combinations that had the lowest
##     percentage of delayed flights.  Give a table listing the airport name,
##     the airline name, and the percentage of delayed flights, sorted in
##     order (smallest to largest) of percentage of delays.
airportnames = airlines.str.split('\n').str[4]
airlinenames = airlines.str.split('\n').str[30]
total = airlines.str.split('flights').str[1].str.split("total:").str[1].str.split(" ").str[1].astype(float) #gather total flights
delayed = airlines.str.split('flights').str[1].str.split("delayed").str[1].str.split(" ").str[1].astype(float) #each of these lines acquires the number from each category
percentagedelayed = (delayed/total)*100
df = (pd.DataFrame({'airport name':airportnames, 'airline name':airlinenames, '% delayed flights':percentagedelayed})).dropna()
print(df.sort_values(by = '% delayed flights')[0:10])
'''
##12

The first value came out as negative 100 so there must have been a negative 1 or something in that index, I included the top 11 to compensate for this discrepancy.

                  airport name                                 airline name                    % delayed flights  
91386                name: Tampa FL: Tampa International     name: ExpressJet Airlines Inc.             -100.0  
49200      name: Newark NJ: Newark Liberty International     name: Atlantic Southeast Airlines             0.0  
46490                name: Tampa FL: Tampa International     name: ExpressJet Airlines Inc.                0.0    
17654                name: Miami FL: Miami International     name: ExpressJet Airlines Inc.                0.0   
6134             name: Orlando FL: Orlando International     name: ExpressJet Airlines Inc.                0.0   
6138                 name: Miami FL: Miami International     name: ExpressJet Airlines Inc.                0.0  
17600       name: Detroit MI: Detroit Metro Wayne County     name: SkyWest Airlines Inc.                   0.0  
46522      name: Philadelphia PA: Philadelphia Intern...     name: Mesa Airlines Inc.                      0.0  
33850      name: Philadelphia PA: Philadelphia Intern...     name: JetBlue Airways                         0.0  
92402      name: San Francisco CA: San Francisco Inte...     name: Hawaiian Airlines Inc.                  0.0  
'''