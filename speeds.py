"""
Distribution of upload speeds of overall and 5G networks of T-Mobile, AT&T, and Verizon.
For each device, we will select a random provider, a random network, and a speed.
We will then determine if the speed will be 'throttled' based on a random chance.

Device speeds pulled from OpenSignal report: https://www.opensignal.com/reports/2024/07/usa/mobile-network-experience
Filtering to Texas report since mobility data models Austin, TX.
"""

import numpy as np

# Upload speeds in Mbps
# 4G
speeds_4G = {
    'att': 7.2,
    't_mobile': 14.8,
    'verizon': 7.8
}

# 5G
speeds_5G = {
    'att': 15.8,
    't_mobile': 18.7,
    'verizon': 20.3
}

# 5G availability in Texas
availability_5G = {
    'att': 16.7,
    't_mobile': 69.4,
    'verizon': 8.2
}

def select_speed(seed=None):
    if seed is not None:
        np.random.seed(seed)
    is_throttled = np.random.choice([True, False], p=[0.1, 0.9])
    provider = np.random.choice(['att', 't_mobile', 'verizon'], p=[1/3, 1/3, 1/3])
    is_5G = np.random.choice([True, False], p=[availability_5G[provider]/100, 1-availability_5G[provider]/100])
    speed = speeds_5G[provider] if is_5G else speeds_4G[provider]
    throttle_reduction = np.random.uniform(0.3, 0.5)
    speed = speed*throttle_reduction if is_throttled else speed
    return speed

# # Test the function
# import matplotlib.pyplot as plt

# speeds = [select_speed() for i in range(1000)]
# plt.hist(speeds, bins=20)
# plt.xlabel('Speed (Mbps)')
# plt.ylabel('Frequency')
# plt.title('Upload Speeds')
# plt.show()
