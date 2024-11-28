## Readme.md

Scrapes the IMDB.com website for the top movies. 

uses helpers to do the work.

gets the list of movies, then saves a .csv file of the data

sets the data to a datafrom

sends the data to a sqlite3 database and returns the data to a new dataframe.

uses a technique to only ask the website once, saves the response to a file.  After the first time it only uses the file rather than requests the website.
