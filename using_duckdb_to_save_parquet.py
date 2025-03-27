import duckdb
import time

def create_duckdb():
    result = duckdb.sql("""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv("data/measurements.txt", AUTO_DETECT=FALSE, sep=';', columns={'station':VARCHAR, 'temperature': 'DECIMAL(3,1)'})
        GROUP BY station
        ORDER BY station
    """)
    
    result.show()

    # Save the result to a Parquet file
    result.write_parquet("data/measurements_summary.parquet")

if __name__ == "__main__":
    start_time = time.time()
    create_duckdb()
    took = time.time() - start_time
    print(f"DuckDB Took: {took:.2f} sec")

    # Parquet is a file format that stores data in a columnar way, making it very efficient for large volumes of data.


    

    
