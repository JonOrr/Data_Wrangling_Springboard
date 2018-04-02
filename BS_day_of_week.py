# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 00:41:34 2018

Ride count on different days of the week.

@author: Jon
"""
# Import common packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#Change the working directory
# ATTN: You will need to change this locally.
os.chdir('C:/Users/Jon/Documents/Springboard/Capstone1/Bike-Sharing-Dataset')

# Read in the csv's for day.csv and hour.csv
day_df = pd.read_csv('day.csv')
hour_df = pd.read_csv('hour.csv')

# Make an array for each table
day_array = np.array(day_df.values)
hour_array = np.array(hour_df.values)


# =============================================================================
# # Sort into seasonal dataframes
# Spring_hour_df = hour_df.loc[hour_df['season'] == 1]
# Summer_hour_df = hour_df.loc[hour_df['season'] == 2]
# Fall_hour_df   = hour_df.loc[hour_df['season'] == 3]
# Winter_hour_df = hour_df.loc[hour_df['season'] == 4]
# 
# #Make annual data frames
# day_df_2011 = day_df.loc[day_df['yr'] == 0]
# day_df_2012 = day_df.loc[day_df['yr'] == 1]
# 
# #Make annual data frames
# hour_df_2011 = hour_df.loc[hour_df['yr'] == 0]
# hour_df_2012 = hour_df.loc[hour_df['yr'] == 1]
# 
# hour_counts    = hour_df['cnt'].values
# hour_counts_11 = hour_df_2011['cnt'].values
# hour_counts_12 = hour_df_2012['cnt'].values
# =============================================================================

day_df.plot(y = 'cnt')
plt.title('2011-2012 count of users per hour')
plt.xlabel('Windspeed (mph) ')
plt.ylabel('User count')
plt.show()
plt.clf()

day_df_holiday = day_df.loc[day_df['holiday'] == 1]
day_df_NonHoliday = day_df.loc[day_df['holiday'] == 0]

day_holiday_mean = day_df_holiday.mean()
day_NonHoliday_mean = day_df_NonHoliday.mean()


hour_df_holiday = hour_df.loc[hour_df['holiday'] == 1]
hour_df_NonHoliday = hour_df.loc[hour_df['holiday'] == 0]

hour_holiday_mean  = hour_df_holiday.mean()
hour_holiday_NonHoliday = hour_df_NonHoliday.mean()


hour_df_holiday.plot(y = 'cnt')
plt.title('2011-2012 count of users per hour')
plt.xlabel('index')
plt.ylabel('User count')
plt.show()
plt.clf()


hour_df_NonHoliday.plot(y = 'cnt')
plt.title('2011-2012 count of users per hour')
plt.xlabel('Windspeed (mph) ')
plt.ylabel('User count')
plt.show()
plt.clf()


# Holidays are not causing the issues


day_0 = day_df.loc[day_df['weekday'] == 0] 
day_1 = day_df.loc[day_df['weekday'] == 1] 
day_2 = day_df.loc[day_df['weekday'] == 2] 
day_3 = day_df.loc[day_df['weekday'] == 3] 
day_4 = day_df.loc[day_df['weekday'] == 4] 
day_5 = day_df.loc[day_df['weekday'] == 5] 
day_6 = day_df.loc[day_df['weekday'] == 6] 


# Day of the week also does not seem to cause the problem
plt.plot(day_0['cnt'], label = 'Sunday', color = 'pink')  # Sunday
plt.plot(day_1['cnt'], label = 'Monday')                  # Monday
plt.plot(day_2['cnt'], label = 'Tuesday')                  # Tuesday
plt.plot(day_3['cnt'], label = 'Wednesday')                  # Wednesday
plt.plot(day_4['cnt'], label = 'Thursday')                  # Thursday
plt.plot(day_5['cnt'], label = 'Friday')                  # Friday
plt.plot(day_6['cnt'], label = 'Saturday' , color = 'gray')  # Saturday
plt.legend()
plt.show()
plt.clf()


# Weather conditions cause outliers, as seen in other files