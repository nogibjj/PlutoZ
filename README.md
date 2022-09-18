[![Python application test with Github Actions](https://github.com/nogibjj/PlutoZ/actions/workflows/main.yml/badge.svg)](https://github.com/nogibjj/PlutoZ/actions/workflows/main.yml)
# Overview
This project uses the Spark on Databricks to query a dataset (from Kaggle). After connecting the Databricks to the Github codespace, users can query the dataset through CLI and Fastapi. 


# Content
1. Download a dataset which describes unemployment rates of worldwild countries from 1999-2021 from Kaggle. 
<img width="1431" alt="Screen Shot 2022-09-18 at 01 22 18" src="https://user-images.githubusercontent.com/112578482/190887375-cdc581aa-0256-4dfd-880f-8bcfe30f4449.png">2. Create a csv table in Databricks
3. Connect Databricks to Github Codespace
4. Fastapi 

# Test out CLI
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
