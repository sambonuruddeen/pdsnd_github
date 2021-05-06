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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input("Enter a city name (chicago, new york city, washington):")
    while city not in CITY_DATA:
        city = input("Unkown city name. Choose city from this lsit - (chicago, new york city, washington)")
        city = city.casefold()

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    month = input("Enter month from January to June or enter all")
    while month not in months:
        month = input("Error! Enter month from January to June or enter all")
        month = month.casefold()
        
 

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = input("Enter day from Monday to Sunday or enter all")
    while day not in days:
        day = input("Error! Enter day from Monday to Sunday or enter all")


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
    
    # Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extracting month and day of week
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # Filtering by month
    if month != 'all':
        months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
        df = df[df['month']==month]
        
    # Filtering by day of week
    if day != 'all':
            df = df[df['day_of_week']== day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    c_month = df['month'].mode()[0]
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    print('Most Common Month:', months[c_month-1])


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    c_day = df['day'].mode()[0]
    days = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    print('Most Common Day:', days[c_day])


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    c_hour = df['hour'].mode()[0]
    print('Most Common Hour:', c_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("Most Commonly used start station:", df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print("Most Commonly used End station:", df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost Frequent Combination of Start and End Station Trips:\n\n',df.groupby(['Start Station', 'End Station']).size().nlargest(1))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("Total travel time:", df['Trip Duration'].sum())


    # TO DO: display mean travel time
    print("Mean travel time:", df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("User types sum:",df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print("Gender Sum:",df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earliest birth year:",df['Birth Year'].min())
        print("Most recent birth year:",df['Birth Year'].max())
        print("Most common birth year:",df['Birth Year'].mode()[0])


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
