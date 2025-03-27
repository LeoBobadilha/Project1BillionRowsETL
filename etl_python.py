from csv import reader 
from collections import defaultdict
import time 
from pathlib import Path

TXT_FILE_PATH = "data\measurements.txt"

def process_temperatures(TXT_FILE_PATH: Path):
    print("Starting file processing.")

    start_time = time.time()  # Start time

    temperature_by_station = defaultdict(list)  # Example of defaultdict {hamburg:{15,17,35,41}}  
                                                # This is important as it avoids errors when inserting  
                                                # the same value into the dictionary.

    with open(TXT_FILE_PATH, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            station_name, temperature = str(row[0]), float(row[1])
            temperature_by_station[station_name].append(temperature)

    print("Data loaded. Calculating statistics...")

    # Dictionary to store the calculated results
    results = {}

    for station, temperatures in temperature_by_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print("Statistics calculated. Sorting...")
    # Sorting results by station name
    sorted_results = dict(sorted(results.items()))

    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()  # End time
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")

    return formatted_results

# Replace "data/measurements10m.txt" with the correct path to your file
if __name__ == "__main__":  # Ensures the script runs only when executed directly
    TXT_FILE_PATH: Path = Path("data/measurements.txt")
    # 100m > 5 minutes
    results = process_temperatures(TXT_FILE_PATH)
