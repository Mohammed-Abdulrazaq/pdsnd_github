import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    name_of_cities=("chicago","new york city","washington")
    while True:
        city=input("\nWhich city would you like to discover its data? Chicago,New York City, or Washington.\n").lower()
        if city not in name_of_cities:
            print("\nOops you typed a wrong entry. Try again please.")
            continue
        else:
            break

    # get user input for month (all, january, february, ... , june)
    name_of_months=("january","february","march","april","may","june","all")
    while True:
        month=input("\nWhich month would you like to look for? January,February,March,April,May,June,or not at all. Type (all) for no month filter.\n ").lower()
        if month not in name_of_months:
            print("\nOops you typed a wrong entry. Try again please.")
            continue
        else:
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
    name_of_days=("sunday","monday","tuesday","wednesday","thursday","friday","saturday","all")
    while True:
        day=input("\nWhich day would you want to select? Sunday,Monday,Tuseday,Wednesday,Thursday,Friday,Saturday, or not at all. Type (all) for no day filter.\n ").lower()
        if day not in name_of_days:
            print("\nOops you typed a wrong entry. Try again please")
            continue
        else:
            break

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

    # extract month from the Start Time column to create a month column
    df['month'] = df['Start Time'].dt.month

    # extract day from the Start Time column to create a day column
    df['day'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day'] == day.title()]



    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]

    print('The most common month is: ', common_month)


    # display the most common day of week
    common_day = df['day'].mode()[0]

    print('The most common day is: ', common_day)

   

    # extract hour from the Start Time column to create an hour column 
    df['hour'] = df['Start Time'].dt.hour

    # display the most common start hour
    common_hour = df['hour'].mode()[0]

    print('Most common Start Hour:', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]

    print('The most common Start Station is: ', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]

    print('The most common End Station is: ', common_end_station)


    # display most frequent combination of start station and end station trip
    df['Frequent Route'] = df['Start Station'] + ' to ' + df['End Station']
    common_combination_routes = df['Frequent Route'].mode()[0]
    print('The most common combination routes are:', common_combination_routes)
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time (by day)
    total_travel_time= df['Trip Duration'].sum()
    print('The total travel time is: ',total_travel_time/86400, 'days')

    # display average travel time (by hour)
    average_travel_time= df['Trip Duration'].mean()
    print('The average travel time is: ',average_travel_time/3600, 'hours')

    # display maximum travel time (minute)
    max_travel_time= df['Trip Duration'].max()
    print('The maximum travel time is: ',max_travel_time/60, 'minutes')


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    counts_of_user_types = df['User Type'].value_counts()

    print('The counts of user types are: \n',counts_of_user_types)

    # Display counts of gender
    try:
        counts_of_gender = df['Gender'].value_counts()
        print('\nThe counts of gender are: \n',counts_of_gender)
    except KeyError:
        print('\nThere is no information about the counts of gender')

    
    # Display earliest year of birth
    try:
        earliest_year_of_birth = int(df['Birth Year'].min())
        print('\nThe earliest year of birth is: \n',earliest_year_of_birth)
    except KeyError:
        print('\nThere is no information about the earliest year of birth')

    # Display most recent year of birth
    try:
        recent_year_of_birth = int(df['Birth Year'].max())
        print('\nThe recent year of birth is: \n',recent_year_of_birth)
    except KeyError:
        print('\nThere is no information about the recent year of birth')

    # Display most common year of birth
    try:
        common_year_of_birth = int(df['Birth Year'].mode())
        print('\nThe common year of birth is: \n',common_year_of_birth)
    except KeyError:
        print('\nThere is no information about the common year of birth')

    # Display the average year of birth
    try:
        average_year_of_birth = int(df['Birth Year'].mean())
        print('\nThe average year of birth is: \n',average_year_of_birth)
    except KeyError:
        print('\nThere is no information about the average year of birth')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

                
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
