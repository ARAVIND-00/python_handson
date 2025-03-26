import random
import csv
from datetime import datetime, timedelta

# Define ranges for each parameter
# power_outage_range = (15000, 45000)
# power_downtime_range = (5, 120)  # Represented in minutes
# temperature_range = (15, 45)
# current_load_options = [11, 22]  # Represented in kW
# usage_stats_range = (11, 22)
# region_stats_options=["East","West","North","South"]
# date_range = (datetime(2020, 1, 1), datetime(2024, 12, 31))
Class_of_Outlets=['H','L','M','SH','VL']
Type_of_Outlets=['RE','DE','HA']
Outlet_IDs=[50000]

# Function to generate random data
def generate_random_data(outlet_id):
    # power_outage = random.randint(power_outage_range[0], power_outage_range[1])
    # power_downtime = random.randint(power_downtime_range[0], power_downtime_range[1])
    # temperature = random.randint(temperature_range[0], temperature_range[1])
    # current_load = random.choice(current_load_options)
    # usage_stats = random.randint(usage_stats_range[0], usage_stats_range[1])
    # region_stats=random.choice(region_stats_options)
    # random_date = date_range[0] + timedelta(days=random.randint(0, (date_range[1] - date_range[0]).days))

    Class_of_Outlet=random.choice(Class_of_Outlets)
    Type_of_Outlet=random.choice(Type_of_Outlets)
    Outlet_ID = f'CD{outlet_id:05d}'
    
    # return [power_outage, power_downtime, temperature, current_load, usage_stats,region_stats,random_date]
    return Class_of_Outlet,Type_of_Outlet,Outlet_ID

# Generate 20,000 random data points
num_data_points = 10000
data = [generate_random_data(_) for _ in range(num_data_points)]

# Write data to CSV file
with open('outlet_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    # Write header
    writer.writerow(['Class_of_Outlet','Type_of_Outlet','Outlet_ID'])
    # Write data rows
    writer.writerows(data)
