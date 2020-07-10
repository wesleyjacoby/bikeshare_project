# Data Analysis using Python on Bike share Data
Udacity project using mainly the pandas library in Python for the bike share data analysis.

# Project Overview
In this project, I made use of Python to explore data related to bike share systems for three major cities in the United States — Chicago, New York City, and Washington. I wrote code to import the data and answered questions about it by computing descriptive statistics. I also wrote a script that takes in raw input from the user to create an interactive experience in the terminal to present these statistics.

### How To Run The Program:
Ensure you have Python 3.7 or above installed, either from [Anaconda](https://www.anaconda.com/) or the official [Python](https://www.python.org/) website.
Then run *python bikeshare_project_final.py* in your terminal if you're on Windows, or *python 3 bikeshare_project_final.py* if you're on a Mac.

### Program Details:
The program asks the user which of the three cities they'd like to analyse (Chicago, New York City, or Washington). It then asks if they'd like to further filter the information by month (January - June) and day (Monday - Sunday). The user also has the option to apply no filters.

Once input has been received from the user, the program prints the following details:

* Most popular month
* Most popular day
* Most popular hour
* Most popular start station
* Most popular end station
* Most popular combination of start and end stations
* Total trip duration
* Average trip duration
* Types of users by number
* Types of users by gender (if available)
* The oldest user (if available)
* The youngest user (if available)
* The most common birth year amongst users (if available)

The user is then asked if they'd like to view the raw data, five rows at a time.

Finally, the user is given the choice of restarting the program or not.

# Software Requirements:
* Programming Language: Python 3.7.7
* Libraries: time, pandas, humanfriendly

# Project Data:
* chicago.csv - Dataset containing all bike share information for the city of Chicago.

* new_york_city.csv - Dataset containing all bike share information for the city of New York.

* washington.csv - Dataset containing all bike share information for the city of Washington.

All data files provided by Udacity.

# Built With:
* [Python 3.7.7](https://www.python.org/) - The programming language used.
* [pandas](https://pandas.pydata.org/) - A Python library that was used.
* [time](https://docs.python.org/3/library/time.html) - A Python library that was used.
* [humanfriendly](https://humanfriendly.readthedocs.io/en/latest/#api-documentation) - A Python library that was used, specifically, the format_timespan module.

# Credits:
* [Python Documentation](https://docs.python.org/3/) - Official Python Documentation.
* [Pandas Documentation](https://pandas.pydata.org/docs/) - Official Pandas Documentation.
* [Humanfriendly Documentation](https://humanfriendly.readthedocs.io/en/latest/#api-documentation) - Official humanfriendly Documentation.
* [Udacity Programming for Data Science Nanodegree](https://www.udacity.com/) - Excellent course and material.
* [Aritra96](https://github.com/Aritra96) - Where I took inspiration to write this README document.
