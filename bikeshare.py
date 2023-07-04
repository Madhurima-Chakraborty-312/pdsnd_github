import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv', 
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv' }

cities = ['chicago', 'new york', 'washington']

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] 

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
    while True:
        city = input("Enter City : ").lower()  
        if city in cities:
            break
        else:
            print("Not a valid city")

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        choice = input("Enter your choice to filter the data by month, day, or none : ").lower()
        if choice == 'month':
            month = input("Enter Month : ").lower()
            day = 'all'
            if month in months:
                break
            else:
                print('Not a valid month')
        elif choice == 'day':
            day = input("Enter Day : ").lower()
            month = 'all'
            if day in days:
                break
            else:
                print('Not a valid day')
        elif choice == 'none':
            month = 'all'
            day = 'all'
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
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    if popular_month == 1:
        popular_month = "january"
    elif popular_month == 2:
        popular_month = "february"
    elif popular_month == 3:
        popular_month = "march"
    elif popular_month == 4:
        popular_month = "april"
    elif popular_month == 5:
        popular_month = "may"
    elif popular_month == 6:
        popular_month = "june"
    print('Most Common Month : ', popular_month)

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0] 
    print('Most Common Day of the Week : ', popular_day) 
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour #PB
    popular_hour = df['hour'].mode()[0] #PB
    if popular_hour < 12:
        print('Most Common Start Hour : ', popular_hour, ' AM')
    elif popular_hour >= 12:
        if popular_hour > 12:
            popular_hour -= 12
        print('Most Common Start Hour : ', popular_hour, ' PM')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print("Most Common Start Station : ", popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print("Most Common End Station : ", popular_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    combo_station = df['Start Station'] + " to " +  df['End Station']
    common_combo_station = combo_station.mode()[0]
    print("Most Common Trip from Start to End : {}".format(common_combo_station))    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    minute, second = divmod(total_duration, 60)
    hour, minute = divmod(minute, 60)
    print("Total Travel Time is {} : {} : {}".format(hour, minute, second))

    # TO DO: display mean travel time
    average_duration = round(df['Trip Duration'].mean())
    minute, second = divmod(average_duration, 60)
    if minute> 60:
        hour, minute = divmod(minute, 60)
        print('Average Travel Time is {} : {} : {}'.format(hour, minute, second))
    else:
        print('Average Trip Duration is {} : {} : {}'.format(hour, minute, second))
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types : ", user_types)

    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(' ' * 40)
        print('Counts of User Gender:', gender)
    except:
        print('Gender not found')

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest = df['Birth Year'].min()
        recent = df['Birth Year'].max() 
        common = df['Birth Year'].mode() 
        print(' ' * 40)
        print('Count of User Birth Year : ')
        print('Oldest User : ', int(earliest))
        print('Youngest User : ', int(recent))
        print('Most Common : ', int(common))
    except:
        print('Birth year not found')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    show = 5
    start = 0
    end = show - 1  

    print('Would you like to see some raw data from the current dataset?')
    while True:
        raw_data = input('(y or n) :  ')
        if raw_data.lower() == 'y':
            print('Displaying rows {} to {}:'.format(start + 1, end + 1))
            print('\n', df.iloc[start : end + 1])
            start += show
            end += show
            print('-'*40)
            print(' Would you like to see the next {} rows?'.format(show))
            continue
        else:
            break

def main():
    print("Explore US Bikeshare Data")
    while True:
        print('Cities : chicago, new york, washington')
        print('Months : january, february, march, april, may, june, all')
        print('Days : sunday, monday, tuesday, wednesday, thursday, friday, saturday, all')
        print()
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
