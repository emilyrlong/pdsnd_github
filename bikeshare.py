import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
valid_months = ['january', 'february', 'march', 'april', 'may', 'june']

def user_input(error_message, user_question, var_list):
    """
    Automates the process of asking a user for input (for string inputs).
    Args:
        (str) error_message - string to be printed if user inputs the wrong thing
        (str) user_question - the question the user will be prompted to answer and then input
        (list) var_list - list of possible values for the user input
    Returns:
        (str) new_input - the input from the user, in lowercase form
    """
    while True:
        try:
            new_input = str(input(user_question)).lower().strip()
            # if new_input is in the approved variable list, then we break & return new_input
            if new_input in var_list:
                break
            else:
                print(error_message)
        # Any exception will cause an error message
        except:
            print(error_message)

    return new_input


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_error = "Invalid city. Please enter Chicago, New York, or Washington, and be sure to check your spelling."
    city_question = "Would you like to see data for Chicago, New York, or Washington? "
    city = user_input(city_error, city_question, list(CITY_DATA.keys()))

    # Ask if they would like to filter by month
    month_question = "Would you like to filter the data by month? Please say Yes or No: "
    month_q = user_input("Please say Yes or No", month_question, ['yes','no'])

    # get user input for month (all, january, february, ... , june)
    if month_q == "yes":
        monthQ = 'Which month - January, February, March, April, May, or June? '
        month = user_input('Please input a valid month.', monthQ, valid_months)
    else:
        month = 'all'

    # ask if they would like to filter by day
    day_question = "Would you like to filter the data by day of the week? Please say Yes or No: "
    day_q = user_input("Please say Yes or No", day_question, ['yes','no'])

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if day_q == "yes":
        dayQ = 'Which day of the week - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? '
        day = user_input('Please input a valid day.', dayQ, valid_days)
    else:
        day = 'all'

    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # create column for hour for analysis in time_stats function
    df['hour'] = df['Start Time'].dt.hour

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        month = valid_months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def display_data(df):
    """
    Asks the user if they would like to see the raw data, repeats & adds five more rows each time.

    Args:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Asks the user for the first time if they want to see the data
    data_q = "Would you like to view the raw data? Please say Yes or No: "
    display_q = user_input("Please say Yes or No.", data_q, ['yes','no'])

    if display_q == 'yes':
        i = 0
        # change question to "5 more rows of data"
        new_q = "Would you like to view 5 more rows of data? Please say Yes or No: "
        # while loop will print the next 5 rows of the data so long as the user inputs "yes"
        while display_q == 'yes' and df.shape[0] <= i+5:
            print(df.iloc[i:i+5])
            display_q = user_input("Please say Yes or No.", new_q, ['yes','no'])
            i += 5

    print('-'*40)



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Display the most common month:
    if len(df['month'].unique()) == 1:
        # If there's only one month in the dataset, output this string:
        only_month = df['month'].unique()[0]
        print('\nThe only month in this dataset is: ', str(valid_months[only_month - 1]).title())
    else:
        month_mode = df['month'].mode()[0]
        print('\nThe most common month is: ', str(valid_months[month_mode-1]).title())

    # Display the most common day of week:
    if len(df['day_of_week'].unique()) == 1:
        # If there's only one day of the week in the dataset, output this string:
        print('\nThe only day of the week in this dataset is: {}'.format(df['day_of_week'].unique()[0]))
    else:
        print('\nThe most common day of the week is: {}'.format(df['day_of_week'].mode()[0]))

    # Display the most common start hour:
    popular_hour = df['hour'].mode()[0]
    print('\nThe most common hour is: ', popular_hour)

    print("\nThis took %s seconds. \n" % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_mode = df['Start Station'].mode()[0]
    start_count = df['Start Station'].value_counts()[0]
    print('\nThe Most Common Start Station is {} with {} trips.'.format(start_mode, start_count))

    # display most commonly used end station
    end_mode = df['End Station'].mode()[0]
    end_count = df['End Station'].value_counts()[0]
    print('\nThe Most Common End Station is {} with {} trips.'.format(end_mode, end_count))

    # creating combination strings for the start & end stations to find the most frequent one
    df['Trip Start'] = '\nStart Station: ' + df['Start Station'] + '\nEnd Station: ' + df['End Station']
    trip_mode = df['Trip Start'].mode()[0]
    trip_count = df['Trip Start'].value_counts()[0]

    # display most frequent combination of start station and end station trip
    print('\nThe Most Frequent Combination of Stations is: {} \nwith {} trips.'.format(trip_mode, trip_count))

    print("\nThis took %s seconds. \n" % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel = np.sum(df['Trip Duration'])
    print('\nThe total time spent traveling is {} seconds.'.format(total_travel))

    # If the number of seconds is high enough, output the # of years spent biking:
    total_years = int(total_travel // (60 * 60 * 24 * 7 * 52))
    if total_years > 1:
        print("\nThat's over {} years of biking!".format(total_years))
    elif total_years == 1:
        print("\nThat's over 1 year of biking!")

    # calculate mean travel time in seconds and minutes
    mean_travel = np.mean(df['Trip Duration'])
    mean_mins = round(mean_travel / 60, 2)

    print('\nThe mean travel time is {} seconds (which equals {} minutes.)'.format(round(mean_travel,2), mean_mins))

    print("\nThis took %s seconds. \n" % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_counts = df['User Type'].value_counts()
    print('\nUser Types:\n', user_counts)

    # If statement separates New York & Chicago data from Washington
    if 'Gender' in df.columns:
        # Display counts of gender
        gender_counts = df['Gender'].value_counts()
        print('\nGender Counts:\n',gender_counts)

        # Calculate earliest, most recent, and most common year of birth
        earliest_bday = int(df['Birth Year'].min())
        recent_bday = int(df['Birth Year'].max())
        bday_mode = int(df['Birth Year'].mode()[0])

        # Display earliest, most recent, and most common year of birth
        print('\nThe Earliest Birth Year is {}.'.format(earliest_bday))
        print('\nThe Most Recent Birth Year is {}.'.format(recent_bday))
        print('\nThe Most Common Birth Year is {}.'.format(bday_mode))
    else:
        print('\nGender and birth year information is not available for Washington.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
