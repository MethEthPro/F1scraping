PYTHON F1 SCRAPER

BRIEF INTRO
So on a random day i was fascinated by the statistics the F1 fan pages put out , I thought how do they keep the track and all .So i visited a git repository that had some f1 scraping done and i deep dived into it , 

I didnt knew anything about beautiful soup but now i have scraped almost the entire information available on the https://www.formula1.com/en/results.html/2024/races.html  page , it took me like 4-5 days idk 


ABOUT THE REPOSITORY 
in the repository you will find three folders 
RACES,DRIVERS,TEAMS just like the F1 results page
![Screenshot (358)](https://github.com/user-attachments/assets/2a7bddfe-2a40-4a56-b762-f96a7f993c71)

In each folder there is a python file and some example csv files , so that you can get idea as to what you are going to extract 

I have used the datetime module to update the year everytime the program is ran , so even if you run it in 2027 it should work fine

In each program you have the option to enter a range of years like 2018,2022 so the program will scrape for each year 
In each program you will have options in many case '0' stands 'for all' so if you want stats of the entire 2021 season you could press 0 

HOW TO BEGIN 

In races program you have two option either you want to see some basic data or advanced data like qualifying and fastest lap data(other stats like practice sessions and starting grid are not available as of now)
you can choose and run the program accordingly 

In teams program you get information about the teams , either individual performance of the team over the year or the performance of all teams over the year , i.e. constructor standings 

In drivers program you again have two choices whether you want the individual performance of a driver over the year or you want the performance of all the drivers over the year i.e. driver standings


In the everything folder you will find a jupyter notebook and some sample CSVs on which I have performed some basic data analysis with whatever little knowledge i had 

KEY POINTS 
=== UP TO DATE
=== CSV FORMAT
=== ALMOST ALL USEFUL DATA SCRAPED 
=== CAN BE USED TO MAKE PREDICTIONS AND COME OUT WITH INTERESTING STATISTICS

NEGATIVE POINTS
=== the f1 site has changed the html files in recent years , so chances are you will get an error for like years before 2015 , although I am working on it 
=== in F1 team names change very often and it leads to confusion and hampers the data


