[![Python application test with Github Actions](https://github.com/nogibjj/PlutoZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/PlutoZ/actions/workflows/main.yml)
# Overview
This project uses the Spark on Databricks to query a dataset (from Kaggle). After connecting the Databricks to the Github codespace, users can query the dataset through CLI and Fastapi. 


# Content
1.Download a dataset which describes unemployment rates of worldwild countries from 1999-2021 from Kaggle. 
2. Create a csv table in Databricks
<img width="1431" alt="Screen Shot 2022-09-18 at 01 22 18" src="https://user-images.githubusercontent.com/112578482/190887411-14b4cfcf-add9-45aa-88ab-8ee4201635ba.png">

# Connect Databricks cluster to Github Codespace
```
DATABRICKS_HOST
DATABRICKS_HTTP_PATH
DATABRICKS_SERVER_HOSTNAME
DATABRICKS_TOKEN
```
# Scaffolds
```
README.md
Makefile
requirements.txt
querydb.py
unemployment_query_db.py
```
# Fastapi 
```
fastapi-app.py
```


# Test out CLI
```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```




