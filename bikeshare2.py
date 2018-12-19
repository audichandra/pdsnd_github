<<<<<<< current
import time
import pandas as pd
import numpy as np
import random

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    list_city = ['chicago', 'new york', 'washington']
    while True:
        city = str(input("Which city do you want to analyze (chicago, new york, washington)? "))
        if city not in list_city:
            print('That\'s not a valid answer!')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    list_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = str(input("\nWhich month(january, february, march, april, may, june or all) do you want to analyze? "))
        if month not in list_month:
            print('That\'s not a valid answer!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    list_dayofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = str(input("\nWhich day of the week(monday, tuesday, wednesday, thursday, friday, saturday, sunday or all) do you want to analyze? "))
        if day not in list_dayofweek:
            print('That\'s not a valid answer!')
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
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('the most popular month:', common_month)
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    common_day = df['day'].mode()[0]
    print('\nthe most popular day:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nthe most popular hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('the most popular Start Station:', common_sstation)

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('\nthe most popular End Station:', common_estation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' and ' + df['End Station']
    common_cstation = df['Combined Station'].mode()[0]
    print('\nthe most popular Start and End Station together:', common_cstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total = df['Trip Duration'].sum()
    print('total travel duration: %d hours' % Total)

    # TO DO: display mean travel time
    Mean = df['Trip Duration'].mean()
    print('\nmean travel duration: %d hours' % int(Mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user types:\n', user_types)

    # TO DO: Display counts of gender
    gender_array = df['Gender'].value_counts()
    print('\ncount of gender:\n', gender_array)

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    common_birth = df['Birth Year'].mode()[0]
    print('\nthe earliest birth: year', int(earliest_birth))
    print('\nthe most recent birth: year', int(recent_birth))
    print('\nthe most popular birth: year', int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    z = 0
    while True:
        data_input = input('\nwould you like to display individual raw data? Enter yes or no.\n')
        message = "\n'id':'{}',\n'Birth Year':'{}',\n'End Station':'{}',\n'End Time':'{}',\n'Gender':'{}',\n'Start Station':'{}',\n'Start Time':'{}',\n'Trip Duration':'{}',\n'User Type':'{}'"
        if data_input.lower() == 'yes':
            input_count = 0
            i = 0 + z
            while input_count < 1:
                input_count += 1
                df1 = df[[df.columns[0], 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']]
                print(df.iloc[0+i:5+i])
                i += 1
            z += 5
        elif data_input.lower() == 'no':
            break
        else:
            print('yes or no only')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
||||||| after discard
import time
import pandas as pd
import numpy as np
import random

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    list_city = ['chicago', 'new york', 'washington']
    while True:
        city = str(input("Which city do you want to analyze (chicago, new york, washington)? "))
        if city not in list_city:
            print('That\'s not a valid answer!')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    list_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = str(input("\nWhich month(january, february, march, april, may, june or all) do you want to analyze? "))
        if month not in list_month:
            print('That\'s not a valid answer!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    list_dayofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = str(input("\nWhich day of the week(monday, tuesday, wednesday, thursday, friday, saturday, sunday or all) do you want to analyze? "))
        if day not in list_dayofweek:
            print('That\'s not a valid answer!')
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
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('the most popular month:', common_month)
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    common_day = df['day'].mode()[0]
    print('\nthe most popular day:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nthe most popular hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('the most popular Start Station:', common_sstation)

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('\nthe most popular End Station:', common_estation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' and ' + df['End Station']
    common_cstation = df['Combined Station'].mode()[0]
    print('\nthe most popular Start and End Station together:', common_cstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total = df['Trip Duration'].sum()
    print('total travel duration: %d hours' % Total)

    # TO DO: display mean travel time
    Mean = df['Trip Duration'].mean()
    print('\nmean travel duration: %d hours' % int(Mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user types:\n', user_types)

    # TO DO: Display counts of gender
    gender_array = df['Gender'].value_counts()
    print('\ncount of gender:\n', gender_array)

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    common_birth = df['Birth Year'].mode()[0]
    print('\nthe earliest birth: year', int(earliest_birth))
    print('\nthe most recent birth: year', int(recent_birth))
    print('\nthe most popular birth: year', int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    z = 0
    while True:
        data_input = input('\nwould you like to display individual raw data? Enter yes or no.\n')
        message = "\n'id':'{}',\n'Birth Year':'{}',\n'End Station':'{}',\n'End Time':'{}',\n'Gender':'{}',\n'Start Station':'{}',\n'Start Time':'{}',\n'Trip Duration':'{}',\n'User Type':'{}'"
        if data_input.lower() == 'yes':
            input_count = 0
            i = 0 + z
            while input_count < 1:
                input_count += 1
                df1 = df[[df.columns[0], 'Start Time', 'End Time', 'Trip Duration', 'Start Station', 'End Station', 'User Type', 'Gender', 'Birth Year']]
                print(df.iloc[0+i:5+i])
                i += 1
            z += 5
        elif data_input.lower() == 'no':
            break
        else:
            print('yes or no only')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
=======
import time
import pandas as pd
import numpy as np
import random

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    list_city = ['chicago', 'new york', 'washington']
    while True:
        city = str(input("Which city do you want to analyze (chicago, new york, washington)? "))
        if city not in list_city:
            print('That\'s not a valid answer!')
        else:
            break


    # TO DO: get user input for month (all, january, february, ... , june)
    list_month = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
    while True:
        month = str(input("\nWhich month(january, february, march, april, may, june or all) do you want to analyze? "))
        if month not in list_month:
            print('That\'s not a valid answer!')
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    list_dayofweek = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
    while True:
        day = str(input("\nWhich day of the week(monday, tuesday, wednesday, thursday, friday, saturday, sunday or all) do you want to analyze? "))
        if day not in list_dayofweek:
            print('That\'s not a valid answer!')
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
    df = pd.read_csv(CITY_DATA[city])

     # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    common_month = df['month'].mode()[0]
    print('the most popular month:', common_month)
    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    common_day = df['day'].mode()[0]
    print('\nthe most popular day:', common_day)
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('\nthe most popular hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_sstation = df['Start Station'].mode()[0]
    print('the most popular Start Station:', common_sstation)

    # TO DO: display most commonly used end station
    common_estation = df['End Station'].mode()[0]
    print('\nthe most popular End Station:', common_estation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] + ' and ' + df['End Station']
    common_cstation = df['Combined Station'].mode()[0]
    print('\nthe most popular Start and End Station together:', common_cstation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total = df['Trip Duration'].sum()
    print('total travel duration: %d hours' % Total)

    # TO DO: display mean travel time
    Mean = df['Trip Duration'].mean()
    print('\nmean travel duration: %d hours' % int(Mean))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('count of user types:\n', user_types)

    # TO DO: Display counts of gender
    gender_array = df['Gender'].value_counts()
    print('\ncount of gender:\n', gender_array)

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year'].value_counts()
    earliest_birth = df['Birth Year'].min()
    recent_birth = df['Birth Year'].max()
    common_birth = df['Birth Year'].mode()[0]
    print('\nthe earliest birth: year', int(earliest_birth))
    print('\nthe most recent birth: year', int(recent_birth))
    print('\nthe most popular birth: year', int(common_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_input(df):
    z = 0
    while True:
        data_input = input('\nwould you like to display individual raw data? Enter yes or no.\n')
        message = "\n'id':'{}',\n'Birth Year':'{}',\n'End Station':'{}',\n'End Time':'{}',\n'Gender':'{}',\n'Start Station':'{}',\n'Start Time':'{}',\n'Trip Duration':'{}',\n'User Type':'{}'"
        if data_input.lower() == 'yes':
            input_count = 0
            i = 0 + z
            while input_count < 1:
                input_count += 1
                print(df.iloc[0+i:5+i])
                i += 1
            z += 5
        elif data_input.lower() == 'no':
            break
        else:
            print('yes or no only')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_input(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
>>>>>>> before discard
