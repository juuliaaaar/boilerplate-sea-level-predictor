import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('/workspace/boilerplate-sea-level-predictor/epa-sea-level.csv')

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data')

    # Create first line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_values = list(range(1880, 2051))  # Extend to 2050
    y_values = [intercept + slope*x for x in x_values]
    plt.plot(x_values, y_values, 'r', label='Best Fit Line (All Data)')

    # Create second line of best fit using data from year 2000
    recent_data = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(recent_data['Year'], recent_data['CSIRO Adjusted Sea Level'])
    x_values_recent = list(range(2000, 2051))  # Extend to 2050
    y_values_recent = [intercept_recent + slope_recent*x for x in x_values_recent]
    plt.plot(x_values_recent, y_values_recent, 'g', label='Best Fit Line (Since 2000)')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()