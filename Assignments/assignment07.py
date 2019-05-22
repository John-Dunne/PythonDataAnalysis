##
## File: assignment07.py (STAT 3250)
## Topic: Assignment 7 
## John Dunne (jd5an)

##  This assignment requires data from four files: 
##
##      'movies.txt':  A file of over 3900 movies
##      'users.dat':   A file of over 6000 reviewers who provided ratings
##      'ratings.dat': A file of over 1,000,000 movie ratings
##      'zips.txt':    A file of zip codes and location information
##
##  The file 'readme.txt' has more information about the first three files.
##  You will need to consult the readme file to answer some of the questions.

##  Note: You will need to convert the zip code information in 'users.dat' into
##  state (or territory) information for one or more of the questions below.
##  You must use the information in 'zips.txt' for this purpose, you cannot
##  use other conversion methods. 
import pandas as pd
import re
import numpy as np

'''
I am going to use this section before the first question to set up a dataframe with all the information from the different files (I am assuming this is alright).
This will make each question cleaner and the variables referenced in each question when not created locally for created up here.
'''
usersSeries = pd.Series(open('users.dat').read().split('\n')) #reads in users for user.dat file
userID = usersSeries.str.split("::").str[0]
userGender = usersSeries.str.split("::").str[1]
userAge = usersSeries.str.split("::").str[2].astype(float)
userOccupation = usersSeries.str.split("::").str[3].astype(float)
userZip = usersSeries.str.split("::").str[4].astype(str)
useroccupdict = {  0:  "other or not specified",  
                 1:  "academic/educator", 
                 2:  "artist", 
                 3:  "clerical/admin", 
                 4:  "college/grad student",
                 5:  "customer service",
                 6:  "doctor/health care", 
                 7:  "executive/managerial", 
                 8:  "farmer", 
                 9:  "homemaker", 
                 10:  "K-12 student", 
                 11:  "lawyer",
                 12:  "programmer",
                 13:  "retired",
                 14:  "sales/marketing",
                 15:  "scientist",
                 16:  "self-employed",
                 17:  "technician/engineer",
                 18:  "tradesman/craftsman",
                 19:  "unemployed",
                 20:  "writer"}
#Dictionary to convert occupation codes to their strings

userTable = pd.DataFrame({'UserID':userID, 'Gender':userGender, 'Age':userAge, 'Occupation':userOccupation, 'Zip-code':userZip})
userTable['Occupation Name'] = userTable['Occupation'].map(useroccupdict)
#Lines above split user dat into categories then combine them into a dataframe with corresponding columns
movielines = pd.Series(open('movies.txt', encoding="utf8").read().splitlines())
movieID = movielines.str.split('::').str[0]
movieTitle = movielines.str.split('::').str[1]
years = movieTitle.str[-5:-1].astype(float)
titles = movieTitle.str[:-7]
genrestrings = movielines.str.split("::").str[2] # genres for each movie, as string
genrelists = genrestrings.str.split('|') # list of genres for each movie
movieGenre = movielines.str.split('::').str[2]
movieTable = pd.DataFrame({'Movie ID':movieID, 'Movie Title':titles, 'year':years, 'genre':genrelists, 'Movie Title & Year':movieTitle})
#The above lines create a data table for the movies
ratinglines = pd.Series(open('ratings.dat').read().splitlines())
rusersID = ratinglines.str.split('::').str[0]
rmovieID = ratinglines.str.split('::').str[1]
ratings = ratinglines.str.split('::').str[2].astype(float)
timestamp = ratinglines.str.split('::').str[3]
timestampyear = (ratinglines.str.split('::').str[3])
propertime = pd.to_datetime(timestampyear, unit='s')

ratingTable = pd.DataFrame({'UserID':rusersID, 'Movie ID':rmovieID, 'Rating':ratings, 'Timestamp':propertime})
#Lines above place the ratings into a dataframe


zips = pd.read_csv('zipcodes.txt',
                  usecols = [1,4],
                  converters={'Zipcode':str})
zips = zips.drop_duplicates()
zipSer = pd.Series(zips['State'].values, index=zips['Zipcode'])


#%%
## 1.  Determine the percentage of users that are female.  Do the same for the
##     percentage of users in the 35-44 age group.  In the 18-24 age group,
##     determine the percentage of male users.

print ((userTable['Gender'].value_counts()[1]/userTable['Gender'].count())*100)
print((userTable['Age'].value_counts()[2]/userTable['Age'].count())*100)
print((((userTable['Gender'].groupby(userTable['Age'])).value_counts()[2])/((userTable['Age'].value_counts()[2])))*100)

'''
##1

28.294701986754966 -> Percentage of users that are female
18.26158940397351 -> Percentage of users 35-44
72.98277425203989 -> Percentage of male users in the 18-24 age group
'''

#%%
## 2.  Give a year-by-year table of counts for the number of ratings, sorted by
##     year in ascending order.
print((ratingTable['Timestamp'].dt.year).value_counts(ascending=True))
'''
##2

2003      3348
2002     24046
2001     68058
2000    904757
'''
#%%
## 3.  Determine the average rating for females and the average rating for 
##     males.
userANDratings = pd.merge(userTable, ratingTable, on='UserID') #Merge the two tables on UserID
print(userANDratings.groupby('Gender', as_index=False).Rating.mean()) #Group by gender then find the average rating by gender
'''
##3

Gender    Rating
0      F  3.620366
1      M  3.568879
'''
#%%
## 4.  Find the top-10 movies based on average rating.  (Movies and remakes 
##     should be considered different.)  Give a table with the movie title
##     (including the year) and the average rating, sorted by rating from
##     highest to lowest.  (Include ties as needed.)
moviesANDratings = pd.merge(movieTable, ratingTable, on='Movie ID') #Merge the two tables on movieID
topmovies = (moviesANDratings.groupby(['Movie ID', 'Movie Title & Year'], as_index=False).Rating.mean()).sort_values(by = 'Rating', ascending = False) #find average rating then sort values by ratings from top to lowest
#print(topmovies.drop(['Movie ID'], axis = 1)[0:10]) prints out the top 10 movies
'''
##4

                             Movie Title & Year  Rating
2317                       Smashing Time (1967)     5.0
2767                               Lured (1947)     5.0
2475                     Song of Freedom (1936)     5.0
2715                   One Little Indian (1973)     5.0
807                     Follow the Bitch (1998)     5.0
3013                   Bittersweet Motel (2000)     5.0
2256                    Ulysses (Ulisse) (1954)     5.0
3695  Schlafes Bruder (Brother of Sleep) (1995)     5.0
2366                           Baby, The (1973)     5.0
3492         Gate of Heavenly Peace, The (1995)     5.0
'''

#%%
## 5.  Determine the number of movies listed in 'movies.txt' for which there
##     is no rating.  Determine the percentage of these unrated movies for
##     which there is a more recent remake.
numberwithoutratings = movieTable["Movie ID"].nunique()-ratingTable['Movie ID'].nunique() #gives # of movies without ratings
movieTable1 = movieTable[movieTable.duplicated(subset=['Movie Title'], keep=False)] #finds movies that have duplicates
moviedroppeddups = (movieTable1.sort_values(by= 'year', ascending = True).drop_duplicates('Movie Title')) #orders duplicated movies and drops newest ones
NotinRatings = movieTable[~movieTable['Movie ID'].isin(ratingTable['Movie ID'])] #Finds movies that do not have ratings
print(((moviedroppeddups['Movie ID'].isin(NotinRatings['Movie ID'])).count()/numberwithoutratings)*100) #Compares movie IDs between Notinratings and droppedduplicated to find the number of movies with which the nonrated movie was had a newer remake
'''
##5

177 -> unrated movies
21.468926553672315% -> unrated movies with a newer remake
'''
#%%
## 6.  Determine the average rating for each occupation classification 
##     (including 'other or not specified'), and give the results in a
##     table sorted from highest to lowest average and including the
##     occupation title.

userANDratings = pd.merge(userTable, ratingTable, on='UserID') #Merge the two tables on movieID
topOccupations = (userANDratings.groupby(['Occupation Name'], as_index=False).Rating.mean()).sort_values(by = 'Rating', ascending = False)
#print(topOccupations)
'''
##6

           Occupation Name    Rating
13                 retired  3.781736
15               scientist  3.689774
6       doctor/health care  3.661578
9                homemaker  3.656589
3           clerical/admin  3.656516
12              programmer  3.654001
14         sales/marketing  3.618481
10                  lawyer  3.617371
17     technician/engineer  3.613574
7     executive/managerial  3.599772
16           self-employed  3.596575
1        academic/educator  3.576642
2                   artist  3.573081
11  other or not specified  3.537544
5         customer service  3.537529
4     college/grad student  3.536793
0             K-12 student  3.532675
18     tradesman/craftsman  3.530117
20                  writer  3.497392
8                   farmer  3.466741
19              unemployed  3.414050
'''
#%%
## 7.  Determine the average rating for each genre, and give the results in
##     a table listing genre and average rating in descending order.

newmovieTable = (((((movieTable.genre.apply(pd.Series)).merge(movieTable, right_index = True, left_index = True)).drop(["genre"], axis = 1)).melt(id_vars = ['Movie ID', 'Movie Title', 'year', 'Movie Title & Year'], value_name = "genre")).dropna())
#The line above is really long but in short it breaks the list of genres for each entry into their own series, keeping the appropriate index to the movie table, afterwards each movie has x # of rows created for the x # of genres in its genre list.
#Essentially each movie is duplicated by the number of genres it has in its genre list and the each of these new rows only has the genre changed between movies.
newmoviesANDratings = pd.merge(newmovieTable, ratingTable, on='Movie ID')
genreratings = (newmoviesANDratings.groupby(['genre'], as_index=False).Rating.mean()).sort_values(by = 'Rating', ascending = False) #Finds average rating per genre
#print(genreratings)
'''
##7

         genre    Rating
9     Film-Noir  4.075188
6   Documentary  3.933123
16          War  3.893327
7         Drama  3.766332
5         Crime  3.708679
2     Animation  3.684868
12      Mystery  3.668102
11      Musical  3.665519
17      Western  3.637770
13      Romance  3.607465
15     Thriller  3.570466
4        Comedy  3.522099
0        Action  3.491185
1     Adventure  3.477257
14       Sci-Fi  3.466521
8       Fantasy  3.447371
3    Children's  3.422035
10       Horror  3.215013
'''
#%%
## 8.  For the user age category, assume that the user has age at the midpoint
##     of the given range.  (For instance '35-44' has age (35+44)/2 = 39.5)
##     For 'under 18' assume an age of 16, and for '56+' assume an age of 60.
##     For each possible rating (1-5) determine the average age of the raters.

userANDratings = pd.merge(userTable, ratingTable, on='UserID') #Merge the two tables on movieID
def midage(age):  # function to convert the age ranges into mean age
    if age == 1:
        return 16
    if age == 18:
        return 21
    if age == 25:
        return 29.5
    if age == 35:
        return 39.5
    if age == 45:
        return 47
    if age == 50:
        return 52.5
    if age == 56:
        return 60
    
userANDratings['midage'] = userANDratings['Age'].apply(midage) # apply 'midage' to column 'Age'

print((userANDratings.groupby(['Rating'], as_index=False).midage.mean()).sort_values(by = 'Rating', ascending = False))
'''
##8

   Rating     midage
4     5.0  34.368274
3     4.0  34.270909
2     3.0  33.840672
1     2.0  32.769485
0     1.0  31.710783
'''
#%%
## 9.  Find all combinations (if there are any) of occupation and genre for 
##     which there are no ratings.  

newmovieTable = (((((movieTable.genre.apply(pd.Series)).merge(movieTable, right_index = True, left_index = True)).drop(["genre"], axis = 1)).melt(id_vars = ['Movie ID', 'Movie Title', 'year', 'Movie Title & Year'], value_name = "genre")).dropna())
#The line above is really long but in short it breaks the list of genres for each entry into their own series, keeping the appropriate index to the movie table, afterwards each movie has x # of rows created for the x # of genres in its genre list.
#Essentially each movie is duplicated by the number of genres it has in its genre list and the each of these new rows only has the genre changed between movies.

newmoviesANDratings = pd.merge(newmovieTable, ratingTable, on='Movie ID') #merge newmovies table onto rating table
moviesusersratings = pd.merge(newmoviesANDratings, userTable, on='UserID') #merge user table onto ratings and movie table created in the line above.
#print(((moviesusersratings.groupby(['Occupation', 'genre'], as_index=False).Rating.sum())).sort_values(by = 'Rating', ascending = False))
#line above prints out answer
'''
##9
There are no occupations/genre combinations with no ratings.

From my interpretation there is not an occupation with zero ratings in any genre. The lowest rating total include per genre by occupation include:
            occupation|genre|total sum of ratings
153         8.0    Film-Noir     159.0
168         9.0  Documentary     133.0
150         8.0  Documentary      39.0

This means every occupation had rated each genre. I doubled checked and with 21 occupations and 18 genres there should be 378 rows. The table = [378 rows x 3 columns], thus every genre and occupation was included.
'''

#%%
## 10. For each age group, determine the occupation that gave the lowest 
##     average rating.  Give a table that includes the age group, occupation,
##     and average rating.  (Sort by age group from youngest to oldest) 
 
userANDratings = pd.merge(userTable, ratingTable, on='UserID')
print((userANDratings.groupby(['Age', 'Occupation'], as_index=False).Rating.mean()).sort_values(by = 'Rating', ascending = False).drop_duplicates('Age'))

'''
##10

     Age  Occupation    Rating
108  50.0        15.0  4.218478
124  56.0        11.0  4.139785
9     1.0        13.0  4.000000
27   18.0        15.0  3.884386
83   45.0         9.0  3.856867
67   35.0        14.0  3.757257
43   25.0        10.0  3.680000
'''

#%%
## 11. Find the top-5 states in terms of average rating.  Give in table form
##     including the state and average rating, sorted from highest to lowest.
##     Note: If any of the zip codes in 'users.dat' includes letters, then we
##     classify that user as being from Canada, which we treat as a state for
##     this and the next question.
def zipmatch(potentialzip):  #
    if re.search('[a-zA-Z]+', potentialzip):  
        return "Canada"
    if re.search('^(\d\d\d\d\d)', potentialzip):
        return re.search('^(\d\d\d\d\d)', potentialzip).group(1)
    else:
        return 'Not a valid zipcode';

userTable['zipextraction'] = userTable['Zip-code'].apply(zipmatch) #Apply regex to zipcodes and add them to their own column
zipdict = zipSer.to_dict() #create a dictionary from the zip series  
zipdict['Canada'] = 'Canada' #Add Canada as a key to account for the regex if statement
userTable['State'] = userTable['zipextraction'].map(zipdict) #apply the dictionary to the zip extraction column and create a State column for the output
userANDratings = pd.merge(userTable, ratingTable, on='UserID') #merge user table with rating table
print((userANDratings.groupby(['State'], as_index=False).Rating.mean()).sort_values(by = 'Rating', ascending = False)[0:5]) #find the mean rating by grouping by state
'''
##11

 State    Rating
13    GU  4.236842
28    MS  3.996409
1     AK  3.985730
3     AP  3.938967
44    SC  3.807748
'''
#%%
## 12. For each genre, determine which state produced the most reviews.  
##     (Include any ties.)
userTable['zipextraction'] = userTable['Zip-code'].apply(zipmatch) #Apply regex to zipcodes and add them to their own column
zipdict = zipSer.to_dict() #create a dictionary from the zip series  
zipdict['Canada'] = 'Canada' #Add Canada as a key to account for the regex if statement
userTable['State'] = userTable['zipextraction'].map(zipdict) #apply the dictionary to the zip extraction column and create a State column for the output

newmovieTable = (((((movieTable.genre.apply(pd.Series)).merge(movieTable, right_index = True, left_index = True)).drop(["genre"], axis = 1)).melt(id_vars = ['Movie ID', 'Movie Title', 'year', 'Movie Title & Year'], value_name = "genre")).dropna())
#line above is same techinque used in question 9.

newmoviesANDratings = pd.merge(newmovieTable, ratingTable, on='Movie ID') #merge newmovies table onto rating table
moviesusersratings = pd.merge(newmoviesANDratings, userTable, on='UserID') #merge user table onto ratings and movie table created in the line above.
print(((moviesusersratings.groupby(['genre', 'State'], as_index=False).Rating.count())).sort_values(by = 'Rating', ascending = False).drop_duplicates('genre')) #find the count of ratings per genre and state, drop the duplicate genres
'''
##12

           genre State  Rating
388        Drama    CA   66287
226       Comedy    CA   63084
6         Action    CA   46936
828     Thriller    CA   34583
773       Sci-Fi    CA   28928
718      Romance    CA   27294
61     Adventure    CA   24149
281        Crime    CA   14638
553       Horror    CA   12939
171   Children's    CA   12599
883          War    CA   12519
116    Animation    CA    7931
608      Musical    CA    7584
663      Mystery    CA    7570
443      Fantasy    CA    6389
938      Western    CA    3776
498    Film-Noir    CA    3662
335  Documentary    CA    1676
'''
#%%