# Big Data MapReduce in Python (TPC-H Dataset)

## Overview
This project implements three MapReduce-style data processing jobs in Python using the TPC-H 1GB dataset.  
Although MapReduce is typically executed on Hadoop, here it is simulated locally using standard input/output piping and sorting.

## Jobs Implemented
1. **Revenue by Region**  
   - Joins LINEITEM, SUPPLIER, NATION, and REGION tables  
   - Calculates total revenue per region

2. **Orders per Customer**  
   - Counts the number of orders placed by each customer

3. **Average Discount by Nation**  
   - Calculates average discount given by suppliers in each nation

## Repository Structure
scripts/ # Python mapper and reducer scripts
data/ # (Optional) Sample CSV data for quick testing
README.md # Documentation and usage instructions
requirements.txt # Python dependencies (if any)


