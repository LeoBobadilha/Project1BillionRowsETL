import pandas as pd
import numpy as np

# Function to create an example DataFrame with 100k rows and 20 cities
def create_measurements(num_rows=100000, num_cities=20, seed=None):
    state = np.random.RandomState(seed)
    cities = [f"City_{i}" for i in range(num_cities)]
    data = {
        "station": state.choice(cities, size=num_rows),
        "measurement": state.uniform(-20, 50, size=num_rows).round(4)
    }
    df = pd.DataFrame(data)
    return df

# Create an example DataFrame
df = create_measurements(seed=0)

# Display data types and memory usage before conversion
print("Data types and memory usage before conversion")
print(df.dtypes)
print(df.memory_usage(deep=True))

# Save the initial memory usage
initial_memory_usage = df.memory_usage(deep=True).sum()

memory_details_before = df.memory_usage(deep=True)

# Transform data types for efficiency
df["station"] = df["station"].astype("category")
df["measurement"] = pd.to_numeric(df["measurement"], downcast="float")

# Display data types and memory usage after conversion
print("Data types and memory usage after conversion")
print(df.dtypes)
print(df.memory_usage(deep=True))

# Save the final memory usage
final_memory_usage = df.memory_usage(deep=True).sum()

# Calculate memory reduction
total_reduction = 1 - (final_memory_usage / initial_memory_usage)
station_reduction = 1 - (df.memory_usage(deep=True)["station"] / memory_details_before["station"])
measurement_reduction = 1 - (df.memory_usage(deep=True)["measurement"] / memory_details_before["measurement"])

print(f"\nTotal memory usage reduction: {total_reduction:.2f}")
print(f"\nMemory usage reduction for the 'station' column: {station_reduction:.2f}")
print(f"\nMemory usage reduction for the 'measurement' column: {measurement_reduction:.2f}")

# Detail memory usage before and after conversion
print("\nMemory usage details before and after conversion")
print(memory_details_before)

print("\nMemory usage details after conversion:")
print(df.memory_usage(deep=True))
