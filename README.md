# Sales-Data-Pipeline

## Summary
A data pipeline for sales data.

## Architecture
![architecture image](https://github.com/xuwenyihust/Sales-Data-Pipeline/blob/master/resource/sales_data_pipeline.png "Sales Data Pipeline Architecture")

### Mock Data Producer
Keep generating mock sales data for later analysis.

### Kafka
Core of the data pipeline. Has 3 topics for input data: `invoice`, `product`, `customer`. With some other topics for transformed data.

### Kafka Streams (To Do)
Pre-transform data in real-time. Perform the early anomaly detection and alert.

### MySQL
The database in the data pipeline.

### Airflow
Schedule hourly/daily tasks for more detailed analysis and reports.

### Spark
The Spark cluster receives submitted jobs from Airflow.

## How to use
Run the start script:
`. bin/start.sh`

## To Do List
- [ ] More reasonable mock data
- [ ] Kafka Streams anomaly detection
- [ ] Per customer analysis
- [x] Daily sales statistics analysis

## References
[Predictive Analytics with Airflow and PySpark](https://www.slideshare.net/rjurney/predictive-analytics-with-airflow-and-pyspark)

[Data’s Inferno: 7 Circles of Data Testing Hell with Airflow](https://medium.com/@ingwbaa/datas-inferno-7-circles-of-data-testing-hell-with-airflow-cef4adff58d8)

[TIPS FOR TESTING AIRFLOW DAGS](https://blog.antoine-augusti.fr/2018/01/tips-testing-airflow-dags/)
