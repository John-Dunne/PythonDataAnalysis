
## File: assignment04.py (STAT 3250)
## Topic: Assignment 4
##computing id: jd5an
## John Dunne

##  This assignment requires the data file 'airline_tweets.csv'.  This file
##  contains records of over 14000 tweets and associated information related
##  to a number of airlines.  You should be able to read this file in using
##  the usual pandas methods.
import pandas as pd
import numpy as np
import re
import math

airlinetweets = pd.read_csv("airline_tweets.csv")
#%%
##  Note: Questions 1-9 should be done without the use of loops.  
##        Questions 10-13 can be done with loops.

## 1.  Determine the number of tweets for each airline, indicated by the
##     name in the 'airline' column of the data set.  Give the airline 
##     name and number of tweets in table form.
print(airlinetweets.groupby(['airline'])["text"].count())
'''
1.
American          2759
JetBlue           2222
Southwest         2420
US Airways        2913
United            3822
Virgin America     504
'''
#%%
## 2.  For each airlines tweets, determine the percentage that are positive,
##     based on the classification in 'airline_sentiment'.  Give a table of
##     airline name and percentage, sorted from largest percentage to smallest.

#
data = airlinetweets[['airline','airline_sentiment']]
group = (data['airline_sentiment'].groupby(data['airline']).value_counts()/data['airline_sentiment'].groupby(data['airline']).count())*100 #gives table of positive, neutral and negative tweet percentages of total tweets
print(group.sort_values(ascending=False)) #orders the table from largest to smallest
'''
2.

Virgin America  positive             30.158730
JetBlue         positive             24.482448
Southwest       positive             23.553719
United          positive             12.872841
American        positive             12.178325
US Airways      positive              9.234466
'''
#%%
## 3.  List all user names (in the 'name' column) with at least 20 tweets
##     along with the number of tweets for each.  Give the results in table
##     form sorted from most to least.
data = airlinetweets['name'] #Gather just the names
print(data.value_counts(ascending=False).iloc[0:11]) #find out how many times a name appears to count the number of tweets by the user
'''
3.

JetBlueNews        63
kbosspotter        32
_mhertz            29
otisday            28
throthra           27
rossj987           23
weezerandburnie    23
MeeestarCoke       22
GREATNESSEOA       22
scoobydoo9749      21
jasemccarty        20
'''
#%%
## 4.  Determine the percentage of tweets from users who have more than one
##     tweet in this data set.
print((((airlinetweets['name'].value_counts() > 1).value_counts()/(airlinetweets['name'].value_counts() > 1).value_counts().sum()).iloc[1])*100) #This long, convoluted line finds the count values of the number of names that have over 1 tweet, divides the sum of these value by the total number of users to find the ratio of individuals with 1 or more tweets, than multiplies it by 100 to give the percentage....essentially.
'''
4.

38.955979742890534
'''
#%%
## 5.  Among the negative tweets, which five reasons are the most common?
##     Give the percentage of negative tweets with each of the five most 
##     common reasons.  Sort from most to least common.

data = airlinetweets[['negativereason']] #gather the negative tweet reasons
print(data['negativereason'].value_counts(ascending=False).iloc[0:5])#display the top 5
'''
5.

Customer Service Issue    2910
Late Flight               1665
Can't Tell                1190
Cancelled Flight           847
Lost Luggage               724
'''
#%%
## 6.  How many of the tweets for each airline include the phrase "on fleek"?
text = airlinetweets['text']
print(text.str.count('on fleek').sum()) #search and sum the count of the times "on fleek is mentioned"
'''
6.

147
'''
#%%
## 7.  What percentage of tweets included a hashtag?
text = airlinetweets['text'] #separate the text column
print(((text.str.count('#').sum())/text.count())*100) #sum the hashtag count over total tweet count * 100
'''
7.

24.938524590163937
'''
#%%
## 8.  How many tweets include a link to a web site?
text = airlinetweets['text']
print(text.str.count('http').sum()) #look for http as a sign for a hyper link, then sum up its number of occurences
'''
8.

1211
'''
#%%
## 9.  How many of the tweets include an '@' for another user besides the
##     intended airline?
text = airlinetweets['text']
print((text.str.count('@') > 1).sum()) #Only count tweets with more than 1 @ and sum the count
'''
9.

1645
'''
#%%
## 10. Suppose that a score of 1 is assigned to each positive tweet, 0 to
##     each neutral tweet, and -1 to each negative tweet.  Determine the
##     mean score for each airline, and give the results in table form with
##     airlines and mean scores, sorted from highest to lowest.

data = airlinetweets[['airline','airline_sentiment']]

data.loc[data['airline_sentiment'] == 'positive','airline_sentiment'] = 1 #change the tweets from 'positive' to 1
data.loc[data['airline_sentiment'] == 'negative','airline_sentiment'] = -1 #change tweets from 'negative' to -1
data.loc[data['airline_sentiment'] == 'neutral','airline_sentiment'] = 0  #change tweets from 'neutral' to 0


countVirginAmerica = data[data['airline'] == 'Virgin America'].count() #Find the total number of tweets for each airline
countAmerican = data[data['airline'] == 'American'].count()
countJetBlue = data[data['airline'] == 'JetBlue'].count()
countSouthwest = data[data['airline'] == 'Southwest'].count()
countUS_Airways = data[data['airline'] == 'US Airways'].count()
countUnited = data[data['airline'] == 'United'].count()

JetBlueSum = data[data['airline'] == 'JetBlue'].sum() #sum up the positive and negative tweets (-1, 0, 1)
SouthwestSum = data[data['airline'] == 'Southwest'].sum()
US_AirwaysSum = data[data['airline'] == 'US Airways'].sum()
UnitedSum = data[data['airline'] == 'United'].sum()
VirginAmericaSum = data[data['airline'] == 'Virgin America'].sum()
AmericanSum = data[data['airline'] == 'American'].sum()

JetBlueMean = JetBlueSum[1]/countJetBlue[1] #find the averages for each airline from the previous calculations
SouthwestMean = SouthwestSum[1]/countSouthwest[1]
US_AirwaysMean = US_AirwaysSum[1]/countUS_Airways[1]
UnitedMean = UnitedSum[1]/countUnited[1]
VirginAmericaMean = VirginAmericaSum[1]/countVirginAmerica[1]
AmericanMean = AmericanSum[1]/countAmerican[1]

meanFrame = pd.DataFrame({'airlines':['JetBlue','Soutwest','US Airways','United','Virgin America','American'],
                   'mean score':[JetBlueMean, SouthwestMean, US_AirwaysMean, UnitedMean, VirginAmericaMean, AmericanMean]}) #create the new data frame
print(meanFrame.sort_values(by = 'mean score', ascending=False)) #display the dataframe (sorted)

'''
10.

      airlines  mean score
  Virgin America   -0.057540
         JetBlue   -0.184968
        Soutwest   -0.254545
          United   -0.560178
        American   -0.588619
      US Airways   -0.684518

'''
#%%
## 11. Among the tweets that "@" a user besides the indicated airline, 
##     what percentage include an "@" directed at the other airlines 
##     in this file? (Note: Twitterusernames are not case sensitive, 
##     so '@MyName' is the same as '@MYNAME' which is the same as '@myname'.)
data = airlinetweets[['airline','text']]

data = airlinetweets[['airline','text']] #takes the airline and text columns from the airlinetweets.csv
text = data['text'] #goes throught the text

airlinecount = (((text.str.count('@American')).sum()+ (text.str.count('@american')).sum())- 2759) + (((text.str.count('@JetBlue')).sum()+(text.str.count('@jetBlue')).sum() )- 2222) + (((text.str.count('@Virgin')).sum() + (text.str.count('@virgin')).sum()) - 504) + (((text.str.count('@USAirway')).sum() + (text.str.count('@USairway')).sum()) - 2913) + (((text.str.count('@Southwest')).sum()+ (text.str.count('@southwest')).sum()) - 2420) + (((text.str.count('@United')).sum() + (text.str.count('@united')).sum() )- 3822)  # Finds the mentions of each airlines and then subtracts the total tweet number for each airline from the mentions
#regex would have been nice to use for the above expression but I didn't want to use it at the time (because I wanted to use the tools given in class, ended up using regex for 13.)
print((airlinecount/airlinetweets.groupby(['airline'])["text"].count().sum())*100) #gives the final percentage
''''
11.

2.260928961748634
'''
#%%
## 12. Suppose the same user has two or more tweets in a row, based on how they 
##     appear in the file. For such tweet sequences, determine the percentage
##     for which the most recent tweet (which comes nearest the top of the
##     file) is a positive tweet.
data = airlinetweets[['name','airline_sentiment']]
data1 = data[data.duplicated(subset=['name'], keep=False)] #get rid of users who only tweeted once
data2 = data1.drop_duplicates(subset=['name']) #keep only the first tweet from the remaining users
print((data2['airline_sentiment'].value_counts()/data2.name.count())*100) #divide by total number of first tweets from users who tweeted more than once then multiply by 100 to get the percentage
'''
12.

positive    23.200000
'''
#%%
## 13. Give a count for the top-10 hashtags (and ties) in terms of the number 
##     of times each appears.  Give the hashtags and counts in a table
##     sorted from most frequent to least frequent.  (Note: Twitter hashtags
##     are not case sensitive, so '#HashTag', '#HASHtag' and '#hashtag' are
##     all regarded as the same. Also ignore instances of hashtags that are
##     alone with no other characters.)
data = airlinetweets[['text']] #isolates just the texts from the tweets
search = r'(\#\w+)' #regex formula that catches # with some non whitespace after it
print(data.text.str.extractall(search)[0].value_counts()[0:10]) #extracts all the strings that match the regex and then counts them up with the greatest at the top
'''
13.
#DestinationDragons    75
#fail                  57
#UnitedAirlines        35
#jetblue               35
#customerservice       34
#usairwaysfail         26
#AmericanAirlines      24
#disappointed          22
#avgeek                19
#badservice            19
'''



