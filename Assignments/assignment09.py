##
## File: assignment09.py (STAT 3250)
## Topic: Assignment 9 
## John Dunne (jd5an)

##  This assignment requires data from the file 
##
##      'ncaa.csv':  NCAA Men's Tournament Scores, 1985-2019
##
##  The organization of the file is fairly clear.  Each record has information
##  about one game, including the year, the teams, the final score, and each 
##  team's tournament seed.  All questions refer only to the data in this
##  file, not to earlier tournaments.

##  Note: The data set is from Data.World, with the addition of the 2019
##  tournament provided by your dedicated instructor.
import numpy as np # load numpy as np
import pandas as pd # load pandas as pd
pd.set_option('display.max_columns', 500) #Allows us to see all columns
ncaa = pd.read_csv('ncaa.csv')
df = pd.DataFrame(ncaa)
#print(df[df.columns[9]])

leftTeam = pd.DataFrame({'Year':ncaa['Year'], 'MatchID':df.index, 'Region Number':df["Region Number"], 'Region Name':df['Region Name'], 'Seed':df['Seed'],'Score':df['Score'], 'Team':df['Team']}) #create table for right teams of table
rightTeam = pd.DataFrame({'Year':ncaa['Year'], 'MatchID':df.index, 'Region Number':ncaa["Region Number"], 'Region Name':ncaa['Region Name'], 'Seed':df[df.columns[9]],'Score':df[df.columns[8]], 'Team':df[df.columns[7]]}) #table for left side teams
#matchID is used to link the two teams to a match, used initial index to its own column
#print(df[df.columns[9]])
leftTeam['victoryMargin'] = abs(df[df.columns[5]] - df[df.columns[8]]) #victory margin per team (negative means defeat), used for later questions
rightTeam['victoryMargin'] = abs(df[df.columns[8]] - df[df.columns[5]]) 
teams = [leftTeam, rightTeam]

matches = pd.concat(teams) #left and right teams table concat into one table

#%%
## 1.  Find all schools that have won the championship, and make a table that
##     incluldes the school and number of championships, sorted from most to
##     least.
FinalGames = matches.loc[matches['Region Name'] == 'Championship'] #look for championships only
Winners = (FinalGames.groupby(['Region Name','Team', 'MatchID'], as_index=False).Score.max()).sort_values(by = 'MatchID').drop_duplicates(subset = 'MatchID')
#Groupby Region name, Team, and match ID, find max scores, sort the matches by MatchID, then drop duplicates by matchID, the winning team will always be the first unique matchID so it will not be dropped. 
print(Winners['Team'].value_counts()) #Give count of teams
'''
##1
North Carolina    3
Michigan          3
Duke              3
UCLA              2
Connecticut       2
Louisville        2
Indiana           2
Syracuse          2
Kansas            2
Arizona           2
Wisconsin         1
Virginia          1
UNLV              1
Oklahoma          1
Georgia Tech      1
Utah              1
Villanova         1
Illinois          1
Memphis           1
Michigan St       1
Florida           1
Ohio St           1
'''
#%%
## 2.  Find the top-10 schools based on number of tournament appearances.
##     Make a table that incldes the school name and number of appearances,
##     sorted from most to least.  Include all that tie for 10th position
##     if necessary.
FinalGames = matches.loc[matches['Region Name'] == 'Championship'] #Look for only championship games
print(FinalGames['Team'].value_counts()[0:16]) #top 10 (10th ties included)
'''
##2

Duke              9
Michigan          5
North Carolina    5
Kansas            5
Kentucky          5
Connecticut       4
Villanova         3
Syracuse          3
Florida           3
Arizona           2
Louisville        2
Butler            2
UCLA              2
Michigan St       2
Arkansas          2
Indiana           2
'''
#%%
## 3.  Determine the average tournament seed for each school, then make a
##     table with the 10 schools that have the lowest average (hence the
##     best teams). Sort the table from smallest to largest, and include
##     all that tie for 10th position if necessary.
print(matches.groupby(['Team']).Seed.mean().sort_values()[0:10])
'''
##3.
Average Tournment Seed

Team
Duke              1.801587
North Carolina    2.294118
Kansas            2.333333
Kentucky          2.909091
Massachusetts     2.947368
Connecticut       3.309859
Arizona           3.435294
Ohio St           3.537037
Oklahoma          3.822581
UNLV              3.842105
'''
#%%
## 4.  Give a table of the average margin of victory by round, sorted by
##     round in order 1, 2, ....

df['victoryMargin'] = abs(df[df.columns[8]] - df[df.columns[5]]) #Create a new column for victory margin
print(df.groupby(['Round']).victoryMargin.mean()) #find the average of victory margin by round
'''
##4

Round
1    12.956250
2    11.275000
3     9.917857
4     9.707143
5     9.485714
6     8.257143
'''
#%%

## 5.  Give a table of the percentage of wins by the higher seed by round,
##     sorted by round in order 1, 2, 3, ...

df['highervictoryseed'] = ((leftTeam.Seed < rightTeam.Seed) & (leftTeam.Score > rightTeam.Score)) | ((rightTeam.Seed < leftTeam.Seed) & (rightTeam.Score > leftTeam.Score)) #create a highervictoryseed column based upon whether the higher seed won their respective match
groupedwins = (df.groupby(['Round']).highervictoryseed.mean())#find the ratio of higher seeds that won their match by Round then finds the mean
print(groupedwins*100) #keep only the ratio of wins by higher seeds then multiply by 100 for percentage
'''
##5

Round
1    74.285714
2    71.250000
3    71.428571
4    55.000000
5    48.571429
6    57.142857
'''


#%%
## 6.  Determine the average seed for all teams in the Final Four for each
##     year.  Give a table of the top-5 in terms of the lowest average seed
##     (hence teams thought to be better) that includes the year and the
##     average, sorted from smallest to largest.
FinalFourGames = matches.loc[matches['Region Name'] == 'Final Four'] #Look for only final four games
print(FinalFourGames.groupby(['Year']).Seed.mean().sort_values(ascending = True)[0:8]) #Finds average seed per year for these games
'''
##6
There was a tie for 5th place at an average of 1.75 seed.

Year
2008    1.00
1993    1.25
2007    1.50
2001    1.75
1999    1.75
1997    1.75
1991    1.75
2009    1.75
'''

#%%
## 7.  For the first round, determine the percentage of wins by the higher
##     seed for the 1-16 games, for the 2-15 games, ..., for the 8-9 games.
##     Give a table of the above groupings and the percentage, sorted
##     in the order given.
roundgroupingdict = {  1:  "1-16",  
                 2:  "2-15", 
                 3:  "3-14", 
                 4:  "4-13", 
                 5:  "5-12",
                 6:  "6-11",
                 7:  "7-10", 
                 8:  "8-9", } #dictionary to create grouping labels
                 
df['highervictoryseed1'] = ((leftTeam.Seed < rightTeam.Seed) & (leftTeam.Score > rightTeam.Score)) | ((rightTeam.Seed < leftTeam.Seed) & (rightTeam.Score > leftTeam.Score)) #create a highervictoryseed column based upon whether the higher seed won their respective match
round1 = df.loc[df['Round'] == 1]  #gather only round 1 rows
round1['Grouping'] = round1['Seed'].map(roundgroupingdict) #map the groupings to the seed match ups
winningtopseeds = round1.groupby(['Grouping']).highervictoryseed.mean()*100 #find the ratio of higher seeds winning to lower seeds winning then multiply by 100
'''
##7

Grouping
1-16    99.285714
2-15    94.285714
3-14    85.000000
4-13    79.285714
5-12    64.285714
6-11    62.857143
7-10    60.714286
8-9     48.571429
'''

#%%
## 8.  For each champion, determine the average margin of victory in all
##     games played by that team.  Make a table to the top-10 in terms of
##     average margin, sorted from highest to lowest.  Include all that tie
##     for 10th position if necessary.
def ChampionTeam(row):
    if row['Score'] > row['Score.1']:
        return row['Team']
    else:
        return row['Team.1']
Championship = df.loc[df['Region Name'] == 'Championship'] #check to see if the row in question is during a championship match
Championship['Champion'] = Championship.apply(ChampionTeam, axis = 1)  #apply above function
Championlist = Championship['Champion'].tolist() #Adds Champions to a list

matches['Champion'] = matches['Team'].isin(Championlist) #If team is champion then a new Champion column == True
Champions = matches.loc[matches['Champion'] == True]  #isolates champions
print(Champions.groupby(['Team','Champion']).victoryMargin.mean().sort_values(ascending = False)[0:10])       #finds average victory margin, top 10 champions, looking at all the games the champions (and soon to be champions have every played)       
'''
##8

As a note, the margin of victory factors in negative values as the lines above find and retroactively label the champions since 1985 (for example Virginia is considered a Champion in 1985 though it hasn't won yet).
If the Champion has lost a game in the past then it will have a negative victory margin that will factor into the overall average victory margin.
The lines above look at every game ever played by these Champions or soon to be champions and averages the average victory margin at the end of each of their games.

Team            Champion
North Carolina  True        13.428571
Duke            True        13.301587
Arizona         True        13.188235
Kansas          True        13.102564
UCLA            True        13.000000
Florida         True        13.000000
Kentucky        True        12.572727
UNLV            True        12.473684
Indiana         True        12.372881
Louisville      True        11.849315
'''
#%%
## 9.  For each champion, determine the average seed of all opponents of that
##     team.  Make a table of top-10 in terms of average seed, sorted from 
##     highest to lowest.  Include all that tie for 10th position if necessary.
##     Then make a table of the bottom-10, sorted from lowest to highest.
##     Again include all that tie for 10th position if necessary. 
def OpponentSeed(row):
    return row['Seed']

newleftTeam = pd.DataFrame({'Year':ncaa['Year'], 'MatchID':df.index, 'Region Number':df["Region Number"], 'Region Name':df['Region Name'], 'Seed':df['Seed'],'Score':df['Score'], 'Team':df['Team']}) #create table for right teams of table
newrightTeam = pd.DataFrame({'Year':ncaa['Year'], 'MatchID':df.index, 'Region Number':ncaa["Region Number"], 'Region Name':ncaa['Region Name'], 'Seed':df[df.columns[9]],'Score':df[df.columns[8]], 'Team':df[df.columns[7]]}) #table for left side teams
newleftTeam['OpponentSeed'] = newrightTeam.apply(OpponentSeed, axis = 1)
newrightTeam['OpponentSeed'] = newleftTeam.apply(OpponentSeed, axis = 1)
newteams = [newleftTeam, newrightTeam]
newmatches = pd.concat(newteams) #left and right teams table concat into one table
#The lines above remake the match table (which was created at the very top). The opponent seed column is added to the left and right tables before they are merged so that each row has its opponents seed for each match
def ChampionTeam(row):
    if row['Score'] > row['Score.1']:
        return row['Team']
    else:
        return row['Team.1']
Championship = df.loc[df['Region Name'] == 'Championship'] #check to see if the row in question is during a championship match
Championship['Champion'] = Championship.apply(ChampionTeam, axis = 1)  #apply above function
Championlist = Championship['Champion'].tolist() #Adds Champions to a list

newmatches['Champion'] = newmatches['Team'].isin(Championlist) #If team is champion then a new Champion column == True
Champions = newmatches.loc[newmatches['Champion'] == True]
#The line from the function to Champions is essentially the same as the previous problem
print(Champions.groupby(['Team']).OpponentSeed.mean().sort_values(ascending = False)[0:10]) #prints the lowest average opponent seed per Champion
print(Champions.groupby(['Team']).OpponentSeed.mean().sort_values(ascending = True)[0:10]) #prints higheset average opponent seed per Champion

'''
##9
Top 10 Average 'Low' Seeds
Team
Virginia          8.414634
Florida           8.044776
Kansas            8.042735
UNLV              7.973684
Duke              7.960317
Arizona           7.847059
Maryland          7.830189
Syracuse          7.728395
Indiana           7.694915
North Carolina    7.596639

Top 10 Average 'High' Seeds

Team
Villanova         6.737705
Arkansas          7.000000
Michigan St       7.195402
Kentucky          7.245455
UCLA              7.314286
Michigan          7.430769
Connecticut       7.478873
Louisville        7.520548
North Carolina    7.596639
Indiana           7.694915
'''

#%%
## 10. Determine the 2019 champion.
VIRGINIA = df.loc[df['Team'] == 'Virginia']
print(VIRGINIA['Team'])
'''
##10

GO HOOS, Virginia forever

83      Virginia
130     Virginia
264     Virginia
309     Virginia
321     Virginia
384     Virginia
525     Virginia
573     Virginia
633     Virginia
665     Virginia
686     Virginia
1020    Virginia
1413    Virginia
1433    Virginia
1835    Virginia
1863    Virginia
1877    Virginia
1907    Virginia
1931    Virginia
1977    Virginia
1997    Virginia
2007    Virginia
2012    Virginia
2020    Virginia
2079    Virginia
2142    Virginia
2174    Virginia
2190    Virginia
2198    Virginia
2202    Virginia
2204    Virginia
'''
