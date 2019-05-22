
## File: assignment06.py (STAT 3250)
## Topic: Assignment 6
## John Dunne (jd5an)

##  This assignment requires the data file 'movies.txt'.  This file
##  contains records for nearly 4000 movies, including a movie ID number, 
##  the title (with year of release, which is not part of the title), and a 
##  list of movie genre classifications (such as Romance, Comedy, etc). 

##  Note: All questions on this assignment should be done without the explicit
##        use of loops in order to be eliglble for full credit.  
import numpy as np 
import pandas as pd 
## 1.  Are there any repeated movies in the data set?  A movie is repeated 
##     if the title is exactly repeated and the year is the same.  List any 
##     movies that are repeated, along with the number of times repeated.
lines = open('movies.txt', encoding = "utf8").read().splitlines()
lines = pd.Series(lines) 
movies = lines.str.split('::').str[1] #split the movies between :: and :: to find the title of the movie and the year
print(movies.value_counts(ascending = False)) #From what I can find there are no repeated movies with same year AND title
'''
#1

I could not find any repeated via the method shown above
'''
 #%%   
## 2.  Determine the number of movies included in genre "Action", the number
##     in genre "Comedy", and the number in both "Children's" and "Animation".
movies = lines.str.split('::').str[2] #Extracts genre
print(movies.str.contains('Action').value_counts()) #extracts count of genre
print(movies.str.contains('Comedy').value_counts())
print(movies.str.contains("Children's" and 'Animation').value_counts())
'''
2.
Action Movies: 503
Comedy Movies: 1200
Children's and Animation: 105
'''
#%%   
## 3.  Among the movies in the genre "Horror", what percentage have the word
##     "massacre" in the title?  What percentage have 'Texas'? (Upper or lower
##     cases are allowed here.) 
moviesgenre = lines.str.split('::').str[2] #isolates title
moviestitle = lines.str.split('::').str[1] #isolates genre
#print((moviesgenre.str.contains('Horror')).value_counts()) #counts up the number of movies under the Horror genre
print(((lines.str.contains('Horror' and 'Massacre')).value_counts()[1]/(moviesgenre.str.contains('Horror').value_counts()[1]))*100) #percentage of Horror movies that have Massacre in their title (No titles had lower case massacre and were horror)
print(((lines.str.contains('Horror' and 'Texas')).value_counts()[1]/(moviesgenre.str.contains('Horror').value_counts()[1]))*100) #percentage of movies that contain the word Texas and are considered horror movies (No movies that included lower case texas that were horror movies)
'''
#3

2.623906705539359 -> massacre
2.3323615160349855 -> Texas
'''
#%%   
## 4.  How many titles are exactly one word?
moviestitle = lines.str.split('::').str[1] 
print((moviestitle.str.split().str.len()-1).value_counts()[1]) #finds the number of words in the titles (subtracts by 1 to account for the year of the title then displays the count of movies with 1 word titles)
'''
#4

690
'''
#%%   
## 5.  Among the movies with exactly one genre, determine the top-3 genres in
##     terms of number of movies with that genre.
print((lines.str.split('|').str[1]).value_counts(ascending=False)[:3]) #Give the top 3 genre counts, automatically throws out movies with more than one genre
'''
#5

Drama       381
Romance     327
Thriller    228
'''
#%%   
## 6.  Determine the number of movies with 0 genres, with 1 genre, with 2 genres,
##     and so on.  List your results in a table, with the first column the number
##     of genres and the second column the number of movies with that many genres.
totalcount = 3883 - (lines.str.split('|').str[1]).count() + (lines.str.split('|').str[2]).count() + (lines.str.split('|').str[3]).count() + (lines.str.split('|').str[4]).count() + (lines.str.split('|').str[5]).count() # The zero genre includes all the movies without any 
print('0 genre,', totalcount)
print('1 genre,', (lines.str.split('|').str[1]).count())
print('2 genre,', (lines.str.split('|').str[2]).count())
print('3 genre,', (lines.str.split('|').str[3]).count())
print('4 genre,', (lines.str.split('|').str[4]).count())
print('5 genre,', (lines.str.split('|').str[5]).count()) #I printed a table for you without a regular series print out thatd youd get with .value_counts()
'''
#6

0 genre, 2692
1 genre, 1858
2 genre, 536
3 genre, 115
4 genre, 15
5 genre, 1
'''

#%%   
## 7.  How many remakes are in the data?  A movie is a remake if the title is
##     exactly the same but the year is different. (Count one per remake.  For
##     instance, 'Hamlet' appears 5 times in the data set -- count this as one
##     remake.)
movies = lines.str.split('::').str[1] #split the movies between :: and :: to find the title of the movie and the year
moviessplit = movies.str.replace("\(\d\d\d\d\)", "")#remove the years from the titles
print((moviessplit.value_counts().value_counts())) #count up the different values anything with a count greater than 1 had more than one 1 make.
'''
7.

38 movies were remade.
'''
#%%   
## 8.  List the top-5 most common genres in terms of percentage of movies in
##     the data set.  Give the genre and percentage, from highest to lowest.

genres = lines.str.split('::').str[2] #extract genres
lists = genres.str.split("|") #split on | into sublists
listofgenres = sum(lists,[]) #combine the sublists into one big list
seriesofgenres = pd.Series(listofgenres) #make the list back into a series
print((seriesofgenres.value_counts()/movies.count())*100) #find percentage by counting values, dividing by total movies, then multiplying by 100 to get the proper precentage

'''
#8

Drama          41.282514
Comedy         30.903940
Action         12.953902
Thriller       12.670616
Romance        12.129797
Horror          8.833376
Adventure       7.288179
Sci-Fi          7.107906
Children's      6.464074
Crime           5.433943
War             3.682720
Documentary     3.270667
Musical         2.935874
Mystery         2.729848
Animation       2.704095
Fantasy         1.751223
Western         1.751223
Film-Noir       1.133144
'''
#%%   
## 9.  Besides 'and', 'the', 'of', and 'a', what are the 5 most common words  
##     in the titles of movies classified as 'Romance'? (Upper and lower cases
##     should be considered the same.)  Give the number of titles that include
##     each of the words.

Romances = lines[lines.str.contains('Romance')] #No movie titles contained Romance thus this line finds all the movies classified as Romance
Rmovies = Romances.str.split('::').str[1]
noyears = Rmovies.str.replace("\(\d\d\d\d\)", "")
lists = noyears.str.split(" ") #split on | into sublists
listoftitlewords = sum(lists,[]) #creates a list of words in titles
seriesofwords = pd.Series(listoftitlewords ) #turns list into series
print((seriesofwords.value_counts()).drop(['to','To', 'And','and', 'The', 'the', 'of','A','a'])[:6]) #extracts the top 5 values, dropping the designated words
'''
9.

in       25
Love     21
You      10
on       10
&         9
'''
#%%   
## 10. It is thought that musicals have become less popular over time.  We 
##     judge that assertion here as follows: Compute the mean release years 
##     for all movies that have genre "Musical", and then do the same for all
##     the other movies.  Then repeat using the median in place of mean.
Musical = lines[lines.str.contains('Musical')] #isolate musicals, I checked to see if any titles contained "Musical" and pandas returned 0
Mmovies = Musical.str.split('::').str[1] #isolate the movie titles of the musicals
years = Mmovies.str[-5:-1] #take the years from the titles
years = years.astype(float) #find average and mean of the years from just the musicals 
print(np.mean(years), "= Mean release year for Musicals")
print(np.median(years), "= Median release year for Musicals")

allmovies = lines.str.split('::').str[1] #repeat the steps above, but the following lines look through ALL the movies, not just Musicals
allyears = allmovies.str[-5:-1]
allyears = allyears.astype(float)
print(np.mean(allyears), "= Mean release year for all movies")
print(np.median(allyears), "= Median release year for all movies")
'''
#10

1968.7456140350878 = Mean release year for Musicals
1967.0 = Median release year for Musicals
1986.0669585372134 = Mean release year for all movies
1994.0 = Median release year for all movies
'''