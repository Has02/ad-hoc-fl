"""
Distribution of initial battery life and battery life reduction functions for devices.
For each device, we will select a random phone model and a random initial battery life.
After each communication round, we will reduce battery life based on the training time and average power consumption of the phone.

Average battery life percentage is fairly uniform between 60% and 70%
https://www.researchgate.net/publication/225256651_Understanding_Human-Smartphone_Concerns_A_Study_of_Battery_Life/figures?lo=1


TODO: Could be worth looking into how energy consumption by 5G vs 4G networks adds to decrease.
https://www.alcansystems.com/files/news/2019-12-27_5G-and-Beyond.pdf
For now, implement based on hardware consumption.

Can use the equation from the MOHAWK paper to calculate battery life reduction, caveat is it only
accounts for upload speed

https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=37cbd5bf8c460f057d30cbdd01a97d5aefe6fa92

Power can also be modeled something like section 4.4 in the batteryfl paper:
Function of baseline power, number of cores, utilization of the core, frequency of the core, and a power coefficient.

Pi = P_baseline + sum[0 to n](P_core * U_core * F_core * Y) where n is the number of cores and Y is the power coefficient.

Then just multiply Pi by training time to get the power consumption for that round of training.
"""

import numpy as np

battery_life = np.random.uniform(0.6, 0.7, 1000)

"""
Dictionary of phone models:
 - Name : model name (str)
    - Power consumption: average power consumption in watts (float)
    - Battery Capacity: battery capacity in watt-hours (float)

"""
phone_models = {
    'samsung_galaxy_s20': {
        'battery_capacity': 4.0
    },
    'apple_iphone_15': {
        'battery_capacity': 12.98,
        'cores': 6,
        'power_coefficient': 0.1,
        'baseline_power': 0.5,
        'frequency': 2.5
    },
    'google_pixel_5': {
        'battery_capacity': 4.1
    }
}


"""
Initialize phone and battery life.
"""

def init_battery(seed=None):
    if seed is not None:
        np.random.seed(seed)
    phone = np.random.choice(list(phone_models.keys()))
    battery = np.random.choice(battery_life)
    return phone, battery

def reduce_battery(phone, battery, training_time):
    model = phone_models[phone]
    power_consumption = model['baseline_power'] + model['cores'] * model['power_coefficient'] * model['frequency'] * training_time
    battery -= power_consumption
    return battery