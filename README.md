# Project1BillionRowsETL

## Overview
Project1BillionRowsETL is an experimental project designed to test and compare different ETL (Extract, Transform, Load) methods for handling massive datasets. The goal is to evaluate performance, scalability, and efficiency across various Python-based ETL approaches.

## Technologies Used
This project tests the following ETL approaches:

- **DuckDB** – A fast, in-process SQL OLAP database optimized for analytical workloads.
- **Pandas** – A popular data analysis library in Python, often used for small to mid-sized data transformations.
- **Pure Python** – Implementing ETL without external libraries to assess baseline performance.
- **PySpark** – The Python API for Apache Spark, ideal for distributed processing of large datasets.

## Objectives
- Compare performance and execution time across different ETL approaches.
- Identify the best method for handling large-scale data transformations.
- Measure resource utilization such as memory and CPU consumption.
- Provide benchmark results for real-world use cases.

## Installation
To run the project locally, install the required dependencies using the following:

```bash
pip install pandas duckdb pyspark
```

Alternatively, set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

## Dataset
The dataset used consists of **one billion rows**, either synthetically generated or sourced from publicly available large datasets. The data structure includes:

- **Station** (string)
- **Temperature** (decimal)

## ETL Implementations
Each ETL method follows a similar workflow:
1. **Extract** – Load data from a CSV file.
2. **Transform** – Apply filtering, aggregation, and data cleansing.
3. **Load** – Output the processed data and measure execution time.


## Conclusion
This project provides a comparative analysis of different ETL strategies for large datasets. Depending on the use case:
- **DuckDB** is great for fast SQL queries on structured data.
- **Pandas** is effective for smaller datasets but has memory limitations.
- **Pure Python** is slow but useful for custom optimizations.
- **PySpark** is best suited for large-scale distributed processing.

