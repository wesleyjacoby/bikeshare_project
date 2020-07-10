import time
from humanfriendly import format_timespan
import pandas as pd


# Dictionary with city data files
CITY_DATA = {'Chicago': 'chicago.csv',
             'New York City': 'new_york_city.csv',
             'Washington': 'washington.csv'
             }

# List of available months
months = ['January', 'February', 'March', 'April', 'May', 'June', 'All']

# List of available days
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'All']


def next_stat():
    """Waits for the user to press enter before loading more statistics"""
    
    input('Press Enter to load more statistics...')
    print()
    
    print('-'*40)


def get_city():
    """
    Asks the user which city they would like to analyse.
    
    Returns:
        (str) city - name of the city to analyse.
    """
        
    while True:
        city = input('Would you like to analyse Chicago, New York City or Washington: ').strip().title()
        if city == 'Chicago' or city == 'New York City' or city == 'Washington':
            break
        else:
            print(f'You entered: "{city}". This is not a valid input. Please try again...')
            
    return city
            
            
def get_month():
    """
    Asks the user which month they would like to analyse.
    
    Returns:
        (str) month - name of the month to filter by, or "all" to apply no month filter
    """
    
    month = input('Which month would you like to analyse: January, February, March, April, May, June or all: ').strip().title()
    while month not in months:
        print(f'You entered: "{month}". This is not a valid input. Please try again...')
        month = input('Which month would you like to analyse: January, February, March, April, May, June or all: ').strip().title()
        
    return month
        
        
def get_day():
    """
    Asks the user which day of the week they would like to analyse.
    
    Returns:
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    day = input('Which day would you like to analyse: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ').strip().title()
    while day not in days:
        print(f'You entered: "{day}". This is not a valid input. Please try again...')
        day = input('Which day would you like to analyse: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all: ').strip().title()
        
    return day
        
        
def get_filters():
    """
    Executes the get_city, get_month and get_day functions.

    Returns:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('\nHello! Let\'s explore some US bikeshare data!')
    
    city = get_city()
    month = get_month()
    day = get_day()
    
    print(f'\nYou have selected the city "{city}", the month "{month}" and the day "{day}".')
    
    print('-'*40)
    
    return city, month, day
 


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    df = pd.read_csv(CITY_DATA[city])
    
    # Convert Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    # Delete an unnamed column
    df = df.drop('Unnamed: 0', axis=1)
    
    # Filter by month if applicable
    if month != 'All':
        # use the index of the months list to get the corresponding int
        month = months.index(month) + 1
        
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
        
    # filter by day of week if applicable
    if day != 'All':
        # use the index of the days list to get the corresponding int
        day = days.index(day)
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
    return df


def time_stats(df, city, month, day):
    """
    Displays statistics on the most frequent times of travel.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
        (str) month - name of the month to filter by, or "all"
        (str) day - name of the day of week to filter by, or "all"
    """
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # Displays the most common month
    if month == 'All':
        popular_month = df['month'].mode()[0]
        popular_month = months[popular_month - 1]
    
    # Displays the most common day of the week
    if day == 'All':
        popular_day = df['day_of_week'].mode()[0]
        popular_day = days[popular_day - 1]
    
    # Displays the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    if month == 'All' and day == 'All':
        print(f'The most popular hour is {popular_hour}:00 on a {popular_day} in {popular_month}.')
    elif month == 'All':
        print(f'The most popular hour is {popular_hour}:00 on a {day} in {popular_month}.')
    elif day == 'All':
        print(f'The most popular hour is {popular_hour}:00 on a {popular_day} in {month}.')
    else:
        print(f'The most popular hour is {popular_hour}:00 on a {day} in {month}.')
    
    print(f'\nThis took {round((time.time() - start_time), 3)} seconds.')
    print('-'*40)
    
    
def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # Displays the most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print(f'The most commonly used start station is: {popular_start_station}.')
    
    # Displays the most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print(f'\nThe most commonly used end station is: {popular_end_station}.')
    
    # Displays the most frequent combination of start station and end station route
    df['route'] = df['Start Station'] + ' TO ' + df['End Station']
    popular_route = df['route'].mode()[0]
    print(f'\nThe most popular route is: {popular_route}.')
    
    print(f'\nThis took {round((time.time() - start_time), 3)} seconds.')
    print('-'*40)
    
    
def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # Displays the total travel time
    tot_travel_time = df['Trip Duration'].sum()
    
    tot_travel_time = format_timespan(tot_travel_time, max_units=6)
    print(f'The total travel time is: {tot_travel_time}.')
    
    # Displays the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    mean_travel_time = format_timespan(mean_travel_time, max_units=6)
    print(f'\nThe mean travel time is: {mean_travel_time}.')

    print(f'\nThis took {round((time.time() - start_time), 3)} seconds.')
    print('-'*40)
    
    
def user_stats(df, city):
    """
    Displays statistics on bikeshare users.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        (str) city - name of the city to analyse
    """
    
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # Displays the count of user types
    user_types = df['User Type'].value_counts()
    print(user_types.to_string())
    print()
    
    # Displays the count of gender
    try:
        gender_types = df['Gender'].value_counts()
        print(gender_types.to_string())
    except KeyError:
        print(f'{city} does not have a "Gender" column.')
    print()
    
    # Displays the earliest, most recent, and most common year of birth
    try:
        earliest_year = int(df['Birth Year'].min())
        print(f'Earliest Year: {earliest_year}')
        
        recent_year = int(df['Birth Year'].max())
        print(f'\nMost Recent Year: {recent_year}')
        
        common_year = int(df['Birth Year'].mode()[0])
        print(f'\nMost Common Year: {common_year}')
    except KeyError:
        print(f'{city} does not have a "Birth Year" column.')
        
    print(f'\nThis took {round((time.time() - start_time), 3)} seconds.')
    print('-'*40)
    
    
def display_data(df, current_row):
    """
    Displays five lines of data if selected by the user.
    After displaying five lines, the user is asked if they would like to see another five.
    Continues asking until they select no.
    
    Args:
        (DataFrame) df - Pandas DataFrame containing city data filtered by month and day
        (int) current_row - The starting row. Initialised to zero.
        
    Returns:
        If the user selects yes, then this function returns the next five lines
        of the dataframe and then asks the question again by calling this
        function again.
        If the user selects no, then this function returns no value.
    """
    
    # Displays 5 rows of raw data at a time
    display = input('\nWould you like to view 5 rows of raw data? (Y/N): ').strip().lower()
    print()
    if display == 'yes' or display == 'y':
        print(df.iloc[current_row:current_row + 5])
        current_row += 5
        return display_data(df, current_row)
    if display == 'no' or display == 'n':
        return
    else:
        print("\nThat's not a valid input. Please try again...")
        return display_data(df, current_row)
    
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df, city, month, day)
        next_stat()
        station_stats(df)
        next_stat()
        trip_duration_stats(df)
        next_stat()
        user_stats(df, city)
        display_data(df, 0)
    
    
    
        restart = input('Would you like to restart? (Y/N): ').strip().lower()
        if restart.lower() == 'n' or restart.lower() == 'no':
            print('\nYou either don\'t want to restart, or entered an incorrect command.')
            print('\nEither way, this program is terminating...')
            print('-'*40)
            break
        
        
if __name__ == "__main__":
	main()
