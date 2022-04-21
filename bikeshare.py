import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
MONTHS=['january','february','march','april','may','june','all']
DAYS=['saturday','sunday','monday','tuesday','wednesday','thrusday','friday','all']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    cityq,monthq,dayq=False,False,False
    
    while True:
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        if not cityq:
            city=input("Please Enter the city you want to explore (chicago, new york city, washington): ").lower()
            if city not in CITY_DATA:
                print("Invalid city Please choose one from this (chicago, new york city, washignton): ")
                continue
            else:
                cityq=True
            print('\n')
        
    # TO DO: get user input for month (all, january, february, ... , june)
        if not monthq:
            month=input("Please Enter the month you want to explore or if you want to explore all just Enter all: ").lower()
            if month not in MONTHS:
                print("Invalid month Please choose one from this ( january, february, march, april, may, june, all): ")
                continue
            else:
                monthq=True
            print("\n")
            

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        if not dayq:
            day=input("Please Enter the day you want to explore or all: ").lower()
            if day not in DAYS:
                print("Invalid day Please choose one from this (saturday, sunday, monday, tuesday, wednesday, thrusday, friday, all): ")
                continue
            else:
                dayq=True
                break
            print("\n")

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
    df=pd.read_csv(CITY_DATA[city])
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    
    df['End Time']=pd.to_datetime(df['End Time'])
    df['Month']=df['Start Time'].dt.month
    df['Day']=df['Start Time'].dt.day_name()
    
    if month !='all':
        month=MONTHS.index(month)+1
        df=df[df['Month']==month]
    if day !='all':
        df=df[df['Day']==day.title()]
    
    
    
    

    return df

def time_stats(df,month,day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    Most_Common_Month=df['Month'].dropna()
    if month =='all':
        if Most_Common_Month.empty:
            print("Sorry there is No popular Month")
        else:
            Most_Common_Month=Most_Common_Month.mode()[0]
            print("The Most Common Month is {}".format(MONTHS[Most_Common_Month-1]))

    # TO DO: display the most common day of week
    Most_Common_Day=df['Day'].dropna()
    if day == 'all':
        if Most_Common_Day.empty:
            print("Sorry there is No Popular Day")
        else:
            Most_Common_Day=Most_Common_Day.mode()[0]
            print("The Most Common Day is {}".format(Most_Common_Day))
            
        


    # TO DO: display the most common start hour
    Most_Common_Hour=df['Start Time'].dt.hour.dropna().mode()[0]
    print("The Most Common Hour is {}".format(Most_Common_Hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Most_Common_Sstation=df['Start Station'].dropna().mode()[0]
    print('The Most Frequent Start Station is {}'.format(Most_Common_Sstation))

    # TO DO: display most commonly used end station
    Most_Common_Estation=df['End Station'].dropna().mode()[0]
    print('The Most Frequent End Station is {}'.format(Most_Common_Estation))
    
    
    # TO DO: display most frequent combination of start station and end station trip
    most=(df['Start Station']+"$"+df['End Station']).dropna().mode()[0]
    print("The most frequent start station is: {} \nand end station is: {}\n".format(most[:most.index('$')],most[most.index('$')+1:]))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    DurationTime=df['Trip Duration'].dropna().sum()
    print('Total travel time in seconds is : {}'.format(DurationTime))
    # TO DO: display mean travel time
    MeanTime=df['Trip Duration'].dropna().mean()
    print('Mean travel time in seconds is : {} '.format(MeanTime))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    types=df['User Type'].value_counts()
    print('User type count...\n{}\n'.format(types))

    # TO DO: Diprint("")splay counts of gender
    
    if 'Gender' in df:
        gender=df['Gender'].value_counts()
        print("User Gender count...\n{}\n".format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_year=df['Birth Year'].dropna()
        print('Earliest year is : {}'.format(int(birth_year.min())))
        print('Most recent year is : {}'.format(int(birth_year.max())))
        print('Most common Year is : {}'.format(int(birth_year.mode()[0])))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    rawCounter = 1
    while True:
        raw_data = input('\nWant to see some raw data? Enter yes or no.\n')
        if raw_data.lower() == 'yes':
            print(df[rawCounter:rawCounter+5])
            rawCounter +=5
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df,month,day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()