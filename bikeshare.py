
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
    valid = ['chicago', 'new york city', 'washington']
    while True:
        city=input("Please Enter City").lower()
        if city in valid:
            break             
        else:
            print("Please Enter 'washington', 'new york city', or 'chicago'")     

            
    while True:
        date_filter=input("Would you like to filter the data by month, day, or both?")
        if date_filter.lower() not in ['month', 'day', 'both']:
            print("Please enter, month, day, or both")
        else:
            break
                
                
    # TO DO: get user input for month (all, january, february, ... , june)
    valid_months = ['all','january', 'february', 'march', 'april', 'may', 'june']   
    while True:        
        month=input("Please Enter Month").lower()
        if date_filter =='month' or date_filter == 'both':
            if month in valid_months:
                break
            else:
                print('please enter a different month')
        else: 
            break 
    
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    valid_days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']  
    while True:
        day=input("Please Enter Day of Week").lower()
        if date_filter == 'day' or date_filter == 'both':
            if day in valid_days:
                break
            else:
                print('please enter a different day')
        else:
            break
    
            
    print('-'*40)
    return city, month, day, date_filter





def load_data(city,month,day,date_filter):
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
    df['day'] = df['Start Time'].dt.weekday_name
   
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]

   
    if day != 'all':
      
        df = df[df['day'] == day.title()]
        
  
    return df
       
    
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
            
           
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
  

    # TO DO: display the most common month

    common_month = df['month'].mode()[0]
    print('Most Common Month:', common_month)

        

    # TO DO: display the most common day of week
    common_day = df['day'].mode()[0]
    print('Most Common Day:', common_day)

    # TO DO: display the most common start hour
    df['start_hour'] = df['Start Time'].dt.hour
    common_hour = df['start_hour'].mode()[0]
    print('Most Common Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = df['Start Station'].astype(str) + ' and '+ df['End Station']
    common_combo = df['route'].mode()[0]
    print('Most Common Combo:', common_combo)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['start_hour'] = df['Start Time'].dt.hour
    df['end_hour'] = df['End Time'].dt.hour
    df['route_time'] = df['end_hour'] - df['start_hour']
    total_time = df['route_time'].sum()
    print('Total Time:', total_time)
    
    


    # TO DO: display mean travel time
    mean_time=df['route_time'].mean()
    print('Mean Time:', mean_time)
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    count_types = df['User Type'].value_counts()
    print('Count of User Types:', count_types)
        


    # TO DO: Display counts of gender
    if 'Gender' not in df.columns:
        print('Count of Gender: Data Not Available')
    else:
        count_gender = df['Gender'].value_counts()
        print('Count of Gender:', count_gender)



    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' not in df.columns:
        print('Birth Year: Data Not Available')
    else:
        oldest = df['Birth Year'].min()
        youngest = df['Birth Year'].max()
        common_birth = df['Birth Year'].mode()
        print('Earliest Year of Birth:', oldest)
        print('Latest Year of Birth:', youngest)
        print('Common Year of Birth:', common_birth)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day, date_filter = get_filters()
        df = load_data(city, month, day, date_filter)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        raw_data=input('Would you like to see 5 rows of raw data based on your input?')
        current_row=0
        while raw_data.lower() != 'no':
            print(df.iloc[current_row:current_row+5])
            current_row += 5
            raw_data = input('Would you like to see the next 5 rows of raw data? Enter yes or no. ')

        print("You have viewed all of the raw data.")
        
                           

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
