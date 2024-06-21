# JBG050-DC2-Grp21
> Repository for the project of Group 21 for the Data Challenge 2 of the course JBG050 at the Technical University of Eindhoven

## Collaborators
- Harsh Nagouda *#1893580*
- Szymon Kozak *1881329*
- Petya Petrova *#1917838*
- Evangelos Matzavino *#1781871*
- Tino aan den Boom *#1890808*

## Clone Repository
> Navigate to your directory of choice to clone the repository

Execute the following command in your command line of choice:

  ```
  git clone git@github.com:HNagouda/JBG050-DC2-Grp21.git
  ```

## 0. Environment Setup
>***NOTE:*** This codebase utilizes python 3.10 - i.e, ensure your environment has a pre existing installation of python 3.10

> Package manager of choice - `conda`. Feel free to use any package manager you like.

- activate your environment of choice and install dependencies

    ```
    pip install -r requirements.txt
    ```
    
---

## 1. Data Download

### Dataset 1: Crimes, Outcomes, Stop and Search Data

#### 1.1: Download Data
Head over to the [data.police.uk/data/archive/](https://data.police.uk/data/archive/) website and select the following options:
  1. [December 2018](https://data.police.uk/data/archive/2018-12.zip )
     - Contains crimes, outcomes, stop and search data from Jan 2016 - Dec 2018
  2. [December 2020](https://data.police.uk/data/archive/2020-12.zip)
     - Contains crimes, outcomes, stop and search data from Jan 2018 - Dec 2020

There's some overlap between the two datasets, especially during the period of Jan 2018 - Dec 2018. 
Upon downloading and extracting the zip files, you should have the following directories:
  - `2018-12`
  - `2020-12`

Navigate into the `2020-12` directory and delete all directories related to 2018. This is to ensure that there's no overlap between the two datasets. These are namely:
  - `2018-01`, `2018-02`, `2018-03`, `2018-04`, `2018-05`, `2018-06`, `2018-07`, `2018-08`, `2018-09`, `2018-10`, `2018-11`, `2018-12`

Now, combine contents of `2018-12` and `2020-12` into a single directory called `crimes_outcomes_stopnsearch`

#### 1.2: Organize Data
1. Create a directory in the cloned repository called `data`
2. Move the newly created `crimes_outcomes_stopnsearch` into under `data`


### Dataset 2: Demographics data

#### 2.1: Download Data
Head over to the London Datastore for [MOPAC Surveys](https:data.london.gov.uk/mopac-surveys) and download the file:
   1. [PAS_T&Cdashboard_toQ3 23-24.xlsx](https://data.london.gov.uk/download/mopac-surveys/c3db2a0c-70f5-4b73-916b-2b0fcd9decc0/PAS_T%26Cdashboard_to%20Q3%2023-24.xlsx)

#### 2.2: Organize Data
1. In the `data` directory, create a new directory called `demographic_data`
2. Move the downloaded excel file into the `demographic_data` directory


### Dataset 3: PAS Ward level data
This was provided to us as part of a canvas module (now unavailable). Please gather the data from the module and place it in the `data` directory under a new directory called `pas_data_ward_level`

### Dataset 4: Use of Force data

#### 4.1: Download Data
Head over to the [London Datastore](https://data.london.gov.uk/dataset/use-of-force) and download the following:
  1. [MPS Use of Force.xlsx (Apr 2017 - Mar 2018)](https://data.london.gov.uk/download/use-of-force/cba04655-0562-4631-ad14-0f3c9f244bbd/MPS%20Use%20of%20Force%20-%20FY17-18.xlsx)
  2. [MPS Use of Force.xlsx (Apr 2018 - Mar 2019)](https://data.london.gov.uk/download/use-of-force/727e768a-a8fe-4c06-bfa3-ac61930bfa78/MPS%20Use%20of%20Force%20-%20FY18-19.xlsx)
  2. [MPS Use of Force.xlsx (Apr 2019 - Mar 2020)](https://data.london.gov.uk/download/use-of-force/2aa0d839-add7-46c1-a168-e62d33323228/MPS%20Use%20of%20Force%20-%20FY19-20.xlsx)


#### 4.2: Organize Data
1. In the `data` directory, create a new directory called `use_of_force`
2. Move the downloaded excel files into the `use_of_force` directory

### Final Data Directory Structure
Your data directory should now look like this:

```
├── data
│   ├── curated_crimes_outcomes
│   │   ├── 2016-01
│   │   ├── 2016-02
│   │   ├── 2016-03
│   │   ├── 2016-04
│   │   ├── 2016-05
│   │   ├── 2016-06
│   │   ├── 2016-07
│   │   ├── 2016-08
│   │   ├── 2016-09
│   │   ├── 2016-10
│   │   ├── 2016-11
│   │   ├── 2016-12
│   │   ├── 2017-01
│   │   ├── 2017-02
│   │   ├── 2017-03
│   │   ├── 2017-04
│   │   ├── 2017-05
│   │   ├── 2017-06
│   │   ├── 2017-07
│   │   ├── 2017-08
│   │   ├── 2017-09
│   │   ├── 2017-10
│   │   ├── 2017-11
│   │   ├── 2017-12
│   │   ├── 2018-01
│   │   ├── 2018-02
│   │   ├── 2018-03
│   │   ├── 2018-04
│   │   ├── 2018-05
│   │   ├── 2018-06
│   │   ├── 2018-07
│   │   ├── 2018-08
│   │   ├── 2018-09
│   │   ├── 2018-10
│   │   ├── 2018-11
│   │   ├── 2018-12
│   │   ├── 2019-01
│   │   ├── 2019-02
│   │   ├── 2019-03
│   │   ├── 2019-04
│   │   ├── 2019-05
│   │   ├── 2019-06
│   │   ├── 2019-07
│   │   ├── 2019-08
│   │   ├── 2019-09
│   │   ├── 2019-10
│   │   ├── 2019-11
│   │   ├── 2019-12
│   │   ├── 2020-01
│   │   ├── 2020-02
│   │   ├── 2020-03
│   │   ├── 2020-04
│   │   ├── 2020-05
│   │   ├── 2020-06
│   │   ├── 2020-07
│   │   ├── 2020-08
│   │   ├── 2020-09
│   │   ├── 2020-10
│   │   ├── 2020-11
│   │   └── 2020-12
│   ├── demographic_data
│   │   ├── datadownload.xlsx
│   ├── pas_data_ward_level
│   │   ├── PAS_ward_level_FY_15_17.csv
│   │   ├── PAS_ward_level_FY_17_18.csv
│   │   ├── PAS_ward_level_FY_18_19.csv
│   │   ├── PAS_ward_level_FY_19_20.csv
│   │   └── PAS_ward_level_FY_20_21.csv
│   └── use_of_force
│       ├── MPS Use of Force - FY17-18.csv
│       ├── MPS Use of Force - FY18-19.csv
│       └── MPS Use of Force - FY19-20.csv
```



---

## 2. Data Aggregation

The file [data_aggregation.py](src/exploration/data_aggregation.py) sorts through all data files under `data/crimes_outcomes_stopnsearch` and constructs singular CSV / Parquet files for each of the following categories:
  1. Crimes
  2. Crime Outcomes
  3. Stop and Search actions.

Stores curated files under `data/curatad_data`

---

## 3. Analysis

The file [analysis.ipynb](src/analysis.ipynb) contains the analysis of the data. It is a Jupyter notebook that can be run in any Jupyter notebook environment (Make sure to use the same environment as the one where the requirements were downloaded!). 

All our analysis is done in this notebook - from data cleaning to data visualization, to modelled predictions.