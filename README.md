# JBG050-DC2-Grp21

## Clone Repository
> Navigate to your directory of choice to clone the repository

Execute the following command in your command line of choice:

  ```
  git clone git@github.com:HNagouda/JBG050-DC2-Grp21.git
  ```

## Environment Setup
>***NOTE:*** This codebase utilizes python 3.10 - i.e, ensure your environment has a pre existing installation of python 3.10

> Package manager of choice - `conda`. Feel free to use any package manager you like.

- activate your environment of choice and install dependencies

    ```
    pip install -r requirements.txt
    ```
    
---

## Data Download

### Step 1: Download Data
Head over to the [data.police.uk/data/](https://data.police.uk/data/) website and select the following options:
  1. Date range
     - [X] January 2023 - February 2024
  2. Forces
     - [X] 'Metropolitan Police Service'
  3. Data Sets 
     - [X] 'Include crime data'
     - [X] 'Include outcomes data'
     - [X] 'Include stop and search data'

Then, click 'generate file' and then download the generated data

### Step 2: Organize Data
1. Create a directory in the cloned repository called `data`
2. Extract the downloaded zip file and rename it to `crimes_outcomes_stopnsearch`
3. Move the `crimes_outcomes_stopnsearch` into under `data`

---

## Data Aggregation

The file [data_aggregation.py](src/exploration/data_aggregation.py) sorts through all data files under `data/crimes_outcomes_stopnsearch` and constructs singular CSV / Parquet files for each of the following categories:
  1. Crimes
  2. Crime Outcomes
  3. Stop and Search actions.

Stores curated files under `data/curatad_data`

---
