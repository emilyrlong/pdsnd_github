### Date created
This project was added to GitHub on **Feb. 17, 2020**.

### Bikeshare Project

### Description
The Bikeshare Project is a project in *Python* that analyzes the bikeshare data from three cities: Chicago, New York City, and Washington.
* First, the function **user_input** is created to simplify the process of asking for user input.
* Then this function is used to ask a user to specify a city, month, and day in the **get_filters** function.
* This input is then used to filter the data with the **load_data** function.
* If the user wants to see any of the raw data, they can do so by answering "Yes" to the prompt from the **display_data** function.
* The **time_stats** function then calculates the statistics on the most frequent times of travel.
* The **station_stats** function finds the most popular stations and trip from the specified city, month, and day.
* The **trip_duration_stats** function displays the statistics on the total and average trip duration.
* The **user_stats** function displays the user count, gender, and birth year information.
* Finally, a **main** function is used to run all of the above functions.

### Files used
* bikeshare.py
* .gitignore
  * chicago.csv
  * new_york_city.csv
  * washington.csv

### Credits
This bikeshare project was completed as a part of the Udacity Programming for Data Science with Python [nanodegree][1] on Jan. 29, 2020. The template version of bikeshare.py and the csv files were all provided by [Udacity][2].

[1]: https://www.udacity.com/course/programming-for-data-science-nanodegree--nd104 "Title"
[2]: https://www.udacity.com "Title"
