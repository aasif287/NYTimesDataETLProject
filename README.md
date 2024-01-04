# Data ETL Pipeline Projectfor New York Times API

This project involves designing, executing, and presenting the results of a Data ETL (Extract, Transform, Load) pipeline using the New York Times API Article Search endpoint.

### Project Summary

Employ Python knowledge and skills to design, execute, and present the results of a Data ETL pipeline project. For this project, the data necessary was retrieved from the New York Times API website. The API endpoint is Article Search, which searches through articles to find information based on the user’s inputted keyword. In the Python code submitted, “Instagram” was searched from April 25, 2018, to April 01, 2022. Instagram has had a substantial social presence since its launch data in 2010, allowing users to capture multimedia and share it with millions of other users worldwide. Using the Article Search endpoint, it will extract the data needed for the keyword ‘Instagram.’ The data extracted is the number of times “Instagram” was found in general articles and articles in the “Arts” section of the search. The data presented is filtered so that only articles searched would be shown and no other multimedia. Then, values like dates, article URLs, and different keywords were appended to a dictionary. The API key added has multiple APIs enabled, like Archive, Article Search, Semantic, and Time Tags APIs that will give me the data I want, which will be processed and outputted on the terminal screen. 

#### Goal
The goal of this project is to analyze the presence of the keyword "Instagram" in articles retrieved from the New York Times API, specifically focusing on the general articles and those in the "Arts" section. The analysis spans from April 25, 2018, to April 01, 2022.

#### Data Source
The data is obtained from the New York Times API using the Article Search endpoint. The API key used enables access to multiple APIs, including Archive, Article Search, Semantic, and Time Tags APIs.

#### Data Transformation
The data is filtered to include only articles containing the keyword "Instagram." Additional filtering is applied to separate articles in the "Arts" section. Dates, article URLs, and other relevant keywords are extracted and organized into a dictionary.

#### Data Storage
The processed data is loaded into a CSV file. The code utilizes packages such as requests, pretty print, pathlib, and csv to obtain data from the New York Times, customize outputs, and import necessary libraries.

### Code Execution

To execute the code, follow these steps:

1. Install required packages:
   ```bash
   pip install requests pprint pathlib csv

   
