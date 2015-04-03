# Maria Miller - Capstone Project - Spring 2015
# Tweeteriffic - A Data Analysis Project Using Twitter

1. Get streaming data from Twitter using Python's Tweepy API.
* getTweets.py
2. Saved to mongodb database
3. Export mongodb database to csv using mongoexport
* Unix command
> mongoexport --csv -o ~/Code/spring15/tweeteriffic/data/valentine.csv - d 
> Valentine -c Tweets -f text,created_at,geo,source --quiet
4. Import csv and save in data structure using pandas 
*  convertCSV.py
5. Analyze data, create word cloud, view word frequencies.
* wordFreq.py, charts.py, createWordCloud.py
