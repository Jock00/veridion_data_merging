# Veridion Data Merging Repository

## Introduction

This repository is designed for completing an interview task at Veridion. The goal was to consolidate data from three different CSV sources into a single, more accurate dataset. The final dataset is easier to read and free of errors such as double quotations and new lines.

## Overview

- **TL;DR**: To view the results, check the files in the `output/` folder.
- **Detailed Process**:
  - **Structure of the Repository**:
    - `src/`: Source files (Python scripts)
    - `data/`: Input and output data
    - `requirements.txt`: Required packages for the application
    - `README.md`: This documentation file

  - **Missing Folder**: An important folder is missing from this repository. You can download it from [this Google Drive link](https://drive.google.com/file/d/1yBUU-7vuqL9YFbdGvsQZe7P67PfgOuTd/view?usp=drive_link). It's too large for Git. Refer [here](#data-folder-structure) for more details.

  - **Setup Instructions**:
    1. Download the missing folder from the provided link.
    2. Create a Python virtual environment:
       ```bash
       python3 -m venv <name_of_environment>
       ```
    3. Activate the environment (for macOS):
       ```bash
       source <name_of_environment>/bin/activate
       ```
    4. Install the required packages:
       ```bash
       pip install -r requirements.txt
       ```
    5. Navigate to the `src/` directory and run the application:
       ```bash
       cd src/
       python main.py
       ```

## Application Logic

1. **Data Reading and Cleaning**:
   - Read data from CSV files and convert them into JSON format.
   - Remove errors such as double quotations and new lines.

2. **Data Merging**:
   - Merge Facebook and Google data by domain (unique identifier).
   - Merge the resultant data with data from the website, using the company name as the key.

3. **Data Structure**:
   - Each entry in the final JSON format is structured as:
     ```json
     {
       "name": {
         "country": {
           "region": [
             {
               "name": "company_name",
               "address": "company_address",
               "phone": "company_phone",
               "category": "company_category"
             }
           ]
         }
       }
     }
     ```
   - In CSV format, the data will be structured as:
     ```
     name, country, region, name, address, phone, category
     ```

## Data Folder Structure

- **`input/`**: Contains the three CSV files used as input.
- **`output/`**: Contains various stages of output files.
  - **`raw_data/`**: Contains data after fixing the CSV files and transforming them into JSON.
  - **`filtered_data/`**: Contains data after removing unnecessary fields and merging data based on domain.
  - **`final/`**: Contains the final merged data.
  - **`testing/`**: Contains test files for validating scripts.

## Links

- [Download Missing Folder](https://drive.google.com/file/d/1yBUU-7vuqL9YFbdGvsQZe7P67PfgOuTd/view?usp=drive_link)

## Note

Since I did not have a clear goal or final destination for the output during the development, I structured the output based on my own interpretation of the requirements. Given this, I am open to adjusting the output format based on further requirements or specifications. Please let me know if there are any changes needed.

## Next Steps

Looking ahead, there are several improvements and extensions that could be made:

1. **Database Integration**:
   - **MongoDB**: For fast query responses and flexible schema, MongoDB could be used. It is well-suited for handling large amounts of data with quick retrieval times, and it is not stored in memory.
   - **Redis**: For even faster response times, Redis could be employed. Redis is an in-memory data store, which makes it ideal for scenarios requiring extremely rapid data access.

2. **Asynchronous Data Processing**:
   - Implementing asynchronous data reading and transformation to improve efficiency and scalability. This would help handle larger datasets and reduce processing time.

3. **Workflow Management**:
   - **Apache Airflow**: Utilize Apache Airflow for orchestrating complex workflows and managing data pipelines. This would automate and streamline the ETL (Extract, Transform, Load) processes.

4. **Web Application**:
   - Build a web application using **Flask** to provide a user interface for viewing and interacting with the data. This would make the data more accessible and user-friendly.

These next steps aim to enhance the functionality and performance of the application, making it more robust and user-centric.
